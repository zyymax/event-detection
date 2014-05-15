#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-03-31
Desc:	build co-occurrence matrix
Update:	2014-04-01
Desc:	Turn co-occurrence into jeccard-coefficient co ==> co*max_df/(a_df+b_df-co); Build input graph file of gpmetis
"""

import numpy
import sys
import itertools
import pprint

if len(sys.argv) < 2:
    print 'Usage:', sys.argv[0], 'v_size'
    exit(1)

v_size = int(sys.argv[1])
#v_size = 5000

# Generate all two-tuples of a list
# [1,2,3] ==> (1,2),(1,3),(2,3)
gene_pair = lambda l: list(itertools.chain.from_iterable([zip(l[:step+1],l[-step-1:]) for step in xrange(len(l)-1)]))

co_matrix = numpy.zeros((v_size,v_size))
df_list = [0]*v_size
# Real size of vertex
real_v_size = 0
# Build co-occurence matrix
for line in sys.stdin:
    #pprint.pprint(sorted(gene_pair(line.strip().split())))
    l = sorted([int(x) for x in line.strip().split()])
    if len(l) == 0:
        continue
    real_v_size = max(real_v_size, l[-1])
    for num in set(l):
        df_list[num] += 1
    for num1,num2 in gene_pair(l):
        co_matrix[num1][num2] += 1
        co_matrix[num2][num1] += 1

real_v_size += 1

max_df = max(df_list)
# Turn co-occurrence into jeccard-coefficient co ==> co*max_df/(a_df+b_df-co)
# Build input graph file of gpmetis
n_edge = 0
lines_list = []
for idxi, listi in enumerate(co_matrix[:real_v_size][:real_v_size]):
    line_list = []
    for idxj, dataj in enumerate(listi):
        if dataj == 0 or idxi == idxj:
            continue
        diff_occur = df_list[idxi]+df_list[idxj]-dataj
        if diff_occur == 0:
            jc = max_df
        else:
            jc = dataj*max_df/diff_occur
        # Jeccard coefficient
        if int(jc) > 0:
            line_list.extend([str(idxj+1), str(int(jc))])
            n_edge += 1
        # Co-occurrence
        #line_list.extend([str(idxj+1), str(int(dataj))])
        n_edge += 1
        co_matrix[idxi][idxj] = dataj/diff_occur
    lines_list.append(' '.join(line_list))
lines_list.insert(0, '%s %s 001' % (len(lines_list), n_edge/2))

#print co_matrix.tolist()
#co_matrix.tofile(sys.argv[1])
numpy.save('co_matrix_jeccard', co_matrix)
print '\n'.join(lines_list)

