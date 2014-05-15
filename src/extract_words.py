#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-03-27
Desc:	count top K words from stdin
Usage:	extract_words.py topK
"""

import sys,os
import collections

filter_data = []
if len(sys.argv) < 2:
    print 'Usage:',sys.argv[0],'topK'
    exit(1)
topK = int(sys.argv[1]) if sys.argv[1].isdigit() else None
for line in sys.stdin:
    line_filter_data = []
    data = line.decode('utf8')
    for char in data:
        if char >= u'\u4e00' and char <= u'\u9fb3':
            line_filter_data.append(char)
        else:
            line_filter_data.append(u' ')
    filter_data.append(u''.join(line_filter_data))
word_dict = collections.Counter(u' '.join(filter_data).split())
for word, count in word_dict.most_common(topK):
    print '%s:%s' %(word.encode('utf8'), count),
