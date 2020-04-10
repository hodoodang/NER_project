import json
import argparse
import re

# 데이터의 형식을 바꾸는 코드
# 문장 중 <단어:태그> 형태의 데이터를
# 번호    단어  태그
# 번호    단어  태그
# 형태의 데이터로 바꾼다.

re_word = re.compile('<(.+?):[A-Z]{2}>')


def dataEdit(lines, outfile_path):
    with open(outfile_path, 'w', encoding='utf-8-sig') as ef:
        for line in lines:
            """
            한 줄이 통째로 빈 경우
            """
            if line == '\n':
                continue
            words = re.sub(':[A-Z]{2}', '', line).replace('\ufeff', '').replace('<', ' ').replace('>',
                                                                                                  ' ').split()  # 띄어쓰기 단위로 분리(하나의 어절 안에 두개 이상의 tag가 있는 경우를 위해 '>'를 기준으로 띄어쓰기)

            re_result = re_word.finditer(line)
            temp_list = []  # 태깅된 단어 리스트
            ner_list = []  # 태깅된 태그 리스트

            for re_item in re_result:
                # print(re_item.group())
                re_item_list = re_item.group().replace('<', '').replace('>', '').split(':')
                temp_list.append(re_item_list[0].split())
                ner_list.append(re_item_list[-1])
            #     print(re_item_list)
            # print(temp_list, ner_list)
            # print(words)
            flag = 0
            j = 0
            k = 0
            while j != len(words):
                if len(temp_list) != 0 and flag == 0 and words[j] in temp_list[k]:
                    for i_ in range(len(temp_list[k])):
                        if i_ == 0:
                            # print(j, len(words), '|', len(temp_list), k)
                            ef.write(words[j] + '\t' + ner_list[k] + '_B\n')
                            # print(words[j] + '\t' + ner_list[k] + '_B\n')
                            j += 1
                        else:
                            # print(j, len(words), '|', len(temp_list), k)
                            ef.write(words[j] + '\t' + ner_list[k] + '_I\n')
                            # print(words[j] + '\t' + ner_list[k] + '_I\n')
                            j += 1
                    k += 1
                    if k == len(temp_list):
                        flag = 1
                else:
                    ef.write(words[j] + '\t-\n')
                    # print(words[j] + '\t-\n')
                    j += 1
            ef.write('\n')
    return


def get_lines(read_file):
    with open(read_file, 'r', encoding='utf-8-sig') as of:
        lines = of.readlines()
    return lines


def main(args):
    lines = get_lines(args.file)
    dataEdit(lines, args.result_file)
    return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--file', type=str, default='./originData/mergeData.txt')
    parser.add_argument('--result_file', type=str, default='./editData/merge.txt')

    args = parser.parse_args()
    main(args)
