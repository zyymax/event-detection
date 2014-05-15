#!/bin/bash
#该脚本对文本进行必要的处理(去噪,分词,生成特征字典,提取指纹),from filter_duplicate.sh
#author:  max.zhang
#date:    2014-04-02
#usage:   sh page_filter.sh data/22-24_short.content

full_prefix=`echo $1 | awk -F '.' '{print $1}'`

#过滤字符，提取有效文本
sh webcontent_filter.sh $1 "$full_prefix.ori"
cat "$full_prefix.ori" | awk '{if(length($0)>60){print NR"\t"$0}}' > "$full_prefix.rowori"
rm -f "$full_prefix.ori"

