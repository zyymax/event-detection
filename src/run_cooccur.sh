#!/bin/bash
# Use keyword to generate co-occurrence matrix

#dict_file='data/0317-0324_keyword_dict.txt'
#data_path='data/sample'
#pred_day='2014-03-24'
dict_file='data/0324-0401_keyword_dict.txt'
data_path='data/page'
pred_day='2014-04-01'
#echo 'generating token-num files...'
#for file in `ls $data_path/*.token`; do
#	prefix=`echo $file | awk -F '.' '{print $1}'`
#	cat $file | src/token2num.py $dict_file > $prefix.tokennum
#done

echo 'generating graph file of metis...'
# V_size: size of vertex
# N_parts: num of partitions
v_size=5000
n_parts=50
cat $data_path/$pred_day*.tokennum | src/build_cooccur_matrix.py $v_size > $pred_day.graph
gpmetis $pred_day.graph $n_parts > $pred_day.graph.part.$n_parts.log
echo 'generating clusters...'
cat $pred_day.graph.part.$n_parts | src/part2token.py $dict_file > "$pred_day"_burst.gp
