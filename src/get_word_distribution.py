#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-03-27
Desc:	get distribution of each word in the given word_dict in different lines
Update:	2014-03-31
Desc:	add 0 to distribution if not exist that day
"""
import sys
import os
import collections

if len(sys.argv) < 2:
    print 'Usage:',sys.argv[0],'word_dict_path'
    exit(1)

word_dict = collections.defaultdict(list)
with open(sys.argv[1]) as ins:
    for line in ins:
        word,count = line.strip().split(':',1)
        word_dict[word].append(int(count))

for line in sys.stdin:
    counter = collections.Counter(line.split())
    for word in word_dict.keys():
        word_dict[word].append(counter.get(word,0))

for word, count_list in word_dict.items():
    print word, ' '.join([str(count) for count in count_list])
