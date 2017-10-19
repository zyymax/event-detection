#!/bin/bash
# Use keyword to generate co-occurrence matrix
# Usage: launch.sh <content_file> <stopword_file> <keywords_size> <gragh_size>

if [ $# != 4 ]; then
echo 'Usage:' $0 '<content_file> <stopword_file> <keywords_size> <gragh_size>'
exit 1;
fi
content_file=$1
stopword_file=$2
keywords_size=$3
graph_size=$4

prefix=`echo $content_file | cut -d '.' -f1`
ori_file=$prefix.ori
token_file=$prefix.token
tokennum_file=$prefix.tokennum
dict_file=$prefix.dict
gpinput_file=$prefix.gpinput
graph_file=$prefix.graph


#filter chars
#过滤字符
echo '1.过滤字符...'
src/webcontent_filter.sh $content_file $ori_file

#parse chinese tokens by jieba
#用结巴分词工具做中文分词
echo '2.用结巴分词工具进行中文分词...'
cat $ori_file | src/stream_tokens.py $stopword_file > $token_file

#generate dict with topK words
#生成topK单词的词典
echo '3.生成topK单词的词典...'
cat $token_file | src/extract_words.py $keywords_size | sed 's/:/ /g' > $dict_file

#generate tokennum
#将token列表转换为keyId列表
echo '3.将token列表转换为keyId列表...'
cat $token_file | src/token2num.py $dict_file > $tokennum_file

#generate word-graph
#生成词图
echo '4.生成词图...'
cat $tokennum_file | src/build_cooccur_matrix.py $keywords_size > $gpinput_file
gpmetis $gpinput_file $graph_size > $gpinput_file.part.$graph_size.log
cat $gpinput_file.part.$graph_size | src/part2token.py $dict_file > $graph_file
cat $graph_file
