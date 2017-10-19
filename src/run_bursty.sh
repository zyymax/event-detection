#!/bin/bash
# Batch process of building bursty feature

data_path='data/'
time_prefix='0317-0324'
# Filter and tokenization
# Build word dict
echo 'building word dictionary...'
cat $data_path/*.token | src/extract_words.py None | sed 's/ /\n/g'| sort > data/"$time_prefix"_word_dict.txt
echo 'merging tokens for each day...'
for day in `seq 17 24`; do
	echo -e 03-$day'\t'`cat $data_path/2014-03-$day*.token | awk '{printf("%s ", $0)}'` ; 
done > data/"$time_prefix"_token_merge.txt

echo 'generating topK words for each day...'
for day in `seq 17 24`; do 
	echo -e 03-$day'\t'  `cat $data_path/2014-03-$day*.token | src/extract_words.py 50`; 
done > data/"$time_prefix"_top50_keyword_merge.txt

echo 'merging tokens for positive and negative data of each day...'
for file in `ls $data_path/*.token | sort`; do 
	echo -e $file'\t'`cat $file | awk '{printf("%s ", $0)}'` ; 
done > data/"$time_prefix"_token_sep.txt

echo 'generating topK words for positive and negative data of each day...'
for file in `ls $data_path/*.token`; do
	echo -e $file'\t'`cat $file | src/extract_words.py 50`; 
done > data/"$time_prefix"_top50_keyword_sep.txt

echo 'generating word distribution over days...'
cat data/"$time_prefix"_token_merge.txt | awk -F '\t' '{print $2}' | src/get_word_distribution.py data/"$time_prefix"_word_dict.txt > data/"$time_prefix"_word_dist.txt

echo 'generating raw statistical data...'
cat data/"$time_prefix"_word_dist.txt | awk '{for(i=3;i<=NF;i++){printf("%d ",$i)}printf("\n")}'| src/statistic_word.py > data/"$time_prefix"_word_exp.txt

echo 'generating final statistical data...'
paste -d ' ' data/"$time_prefix"_word_dist.txt data/"$time_prefix"_word_exp.txt | awk '{printf("%s %s %s ",$1,$2,$NF);for(i=3;i<NF;i++){printf("%s ",$i)}print ""}' | sed 's/,/ /g' > data/"$time_prefix"_word_stat.txt
