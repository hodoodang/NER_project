import bilstm_crf
import argparse
import dataEdit
import torch
import utils
import random
from vocab import Vocab


def make_sentence(lines):
    sentences, tags = [], []
    sent = ['<START>']
    for line in lines:
        line = line.replace('\ufeff', '')
        if line == '\n':
            if len(sent) > 1:
                sentences.append(sent + ['<END>'])
            sent = ['<START>']
        else:
            line = line.split('\t')
            sent.append(line[0].strip())
    return sentences


def batch_iter(data, batch_size=32, shuffle=True):
    """ Yield batch of (sent, tag), by the reversed order of source length.
    Args:
        data: list of tuples, each tuple contains a sentence and corresponding tag.
        batch_size: batch size
        shuffle: bool value, whether to random shuffle the data
    """
    data_size = len(data)
    indices = list(range(data_size))
    if shuffle:
        random.shuffle(indices)
    batch_num = (data_size + batch_size - 1) // batch_size
    for i in range(batch_num):
        batch = [data[idx] for idx in indices[i * batch_size: (i + 1) * batch_size]]
        batch = sorted(batch, key=lambda x: len(x), reverse=True)
        sentences = [x for x in batch]
        yield sentences


def main(args):
    device = torch.device('cuda:0')
    model = bilstm_crf.BiLSTMCRF.load(args.MODEL, device)

    text = dataEdit.get_lines(args.sample_data)
    lines = dataEdit.make_morphs(text)

    sent_vocab = Vocab.load(args.SENT_VOCAB)
    tag_vocab = Vocab.load(args.TAG_VOCAB)
    sentences = utils.words2indices(lines, sent_vocab)

    for sentences in batch_iter(sentences, 64, shuffle=False):
        sentences, sent_lengths = utils.pad(sentences, sent_vocab[sent_vocab.PAD], device)
        predicted_tags = model.predict(sentences, sent_lengths)

    tags = utils.indices2words(predicted_tags, tag_vocab)
    for word, tag in zip(text, tags):
        print(len(word), len(tag))
        for w, t in zip(word, tag):
            print(w, t)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--MODEL', type=str, default='./model/model_merge.pth')
    parser.add_argument('--sample_data', type=str, default='./originData/sample_data.txt')
    parser.add_argument('--SENT_VOCAB', type=str, default='./vocab/merge_sent_vocab.json')
    parser.add_argument('--TAG_VOCAB', type=str, default='./vocab/merge_tag_vocab.json')
    args = parser.parse_args()

    main(args)