#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-04-03
Desc:	generate K nearest neighbours of keywords by setting K / threshold
e.g.:	src/knn_keywords.py co_matrix_jeccard.npy data/0324-0401_keyword_dict.txt 30
"""

import sys
import numpy as np

if len(sys.argv) < 4:
    print 'Usage:', sys.argv[0], 'matrix_file dict_file K'
    exit(1)
topK=int(sys.argv[3])
word_list=[]
with open(sys.argv[2]) as ins:
    for line in ins:
        word_list.append(line.split()[0])

mat = np.load(sys.argv[1])
for rowID, row in enumerate(mat):
    l = [(value,colID) for colID,value in enumerate(row)]
    print word_list[rowID]+':',
    for value, wordID in sorted(l, reverse=True)[:topK]:
        print '%.3f-%s' %(value, word_list[wordID]),
    print ''





