#!/usr/bin/env python
#-*-coding:utf8-*-
"""
Coder:	max.zhang
Date:	2014-03-27
Desc:	calculate expectation, variance and other statistics of word distribution
Update:	2014-03-30
Desc:	use numpy
"""

import numpy
import sys

for lineid, line in enumerate(sys.stdin):
    num_list = [float(num) for num in line.split()]
    if len(num_list) <= 1:
    #0:no occurence, 1:no predict
        array = None
        mean = 0
        std = 0
        var = 0
        incre = 0
    else: 
        array = numpy.array(num_list[:-1])
        mean = array.mean()
        std = array.std(ddof=1)
        var = array.var(ddof=1)
        incre = num_list[-1]-mean-2*std
    #print 'exp:%.3f,std:%.3f,var:%.3f' % (mean,std,var)
    print '%.3f,%.3f,%.3f' % (mean,std,incre)
