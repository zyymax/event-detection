#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-03-31
Desc:	turn tokens into numbers with word dict
"""
import sys

if len(sys.argv) < 2:
    print 'Usage:', sys.argv[0], 'word_dict'
    exit(1)

word_list = []
with open(sys.argv[1]) as ins:
    for line in ins:
        word_list.append(line.split()[0])
token_num_dict = {word:num for num, word in enumerate(word_list)}

for line in sys.stdin:
    num_list = []
    for token in line.strip().split():
        num = token_num_dict.get(token, None)
        if num is not None:
            num_list.append(num)
    print ' '.join([str(num) for num in sorted(set(num_list))])
