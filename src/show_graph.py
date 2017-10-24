#!/usr/bin/env python
#-*-encoding:utf-8-*-

import sys,os
from wordcloud import WordCloud
import matplotlib.pyplot as plt

if __name__ == "__main__":
   for lineno, line in enumerate(sys.stdin):
       words = line.strip().split(',')
       word_dict = {word.split('-')[1].decode('utf-8'):float(word.split('-')[0]) for word in words}
       wc = WordCloud(font_path='data/black.ttc').generate_from_frequencies(word_dict)
       plt.imshow(wc)
       plt.savefig("graph_"+str(lineno)+".png")
       plt.axis("off")
       #plt.show()
           
