"""
데이터 병합 + 분리

# import random
# from sklearn.model_selection import train_test_split
# import dataEdit
"""
import argparse


def data_merge(first_file, second_file):

    with open(first_file, 'r', encoding='utf-8-sig') as ft, open(second_file, 'r', encoding='utf-8-sig') as sf:
        flines = ft.readlines()
        slines = sf.readlines()

        flines.append(slines)
    with open()
    result_path = ''
    return result_path

def main():
    print('a')
    data_merge('./originData/EXOBRAIN_NE_CORPUS_10000.txt', './originData/wisenut_final.txt')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--first_file', type=str, default='./originData/EXOBRAIN_NE_CORPUS_10000.txt')
    parser.add_argument('--second_file', type=str, default='./originData/wisenut_final.txt')

    main()