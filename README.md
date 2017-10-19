event-detection
===============

Coder:	max.zhang

Date:	2014-05-15

Desc:	Tools to detect EVENT-keywords and describe event with word-graph

功能：从多个中文文档中生成事件和描述词

原理：基于中文文档中单词之间的共现特征构造词图，并基于metis工具划分词图，生成事件描述信息

Depend:	[metis-5.1.0](http://glaros.dtc.umn.edu/gkhome/metis/metis/download), jieba, numpy
