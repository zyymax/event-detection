#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-04-01
Desc:	turn partition file of metis to token clustering
"""

import sys
import collections

if len(sys.argv) < 2:
    print 'Usage:', sys.argv[0], 'keyword_dict'
    exit(1)

word_list = []
with open(sys.argv[1]) as ins:
    for line in ins:
        # Line: word occur burst
        word = line.split()[0]
        value = line.split()[2]
        word_list.append((float(value), word))
cluster_list = collections.defaultdict(list)
for lineid, line in enumerate(sys.stdin):
    cluster_list[int(line)].append(word_list[lineid])

for cid in sorted(cluster_list.keys()):
    print ','.join(['%s-%s' %(value,word) for value,word in sorted(cluster_list[cid],reverse=True)])
