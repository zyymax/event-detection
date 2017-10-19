#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 20131012
@author:    zyy_max

@brief: get tokens from input file by jieba
'''
import jieba
import os
import sys


class JiebaTokenizer:
    def __init__(self, stop_words_path, mode='s'):
        self.stopword_set = set()
        # load stopwords
        with open(stop_words_path) as ins:
            for line in ins:
                self.stopword_set.add(line.strip().decode('utf8'))
        self.mode = mode

    def tokens(self, intext):
        intext = u' '.join(intext.decode('utf-8').split())
        if self.mode == 's':
            token_list = jieba.cut_for_search(intext)
        else:
            token_list = jieba.cut(intext)
        return [token for token in token_list if token.strip() != u'' and not token in self.stopword_set]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Usage:\t%s <stopword_file> " % sys.argv[0]
        exit(-1)
    stopword_file = sys.argv[1]
    jt = JiebaTokenizer(stopword_file, 'c')
    # extract tokens and filter by stopwords
    for line in sys.stdin:
        tokens = jt.tokens(line)
        print u' '.join(tokens).encode('utf8')
