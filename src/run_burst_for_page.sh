#!/bin/bash
# Batch process of building bursty feature

data_path='data/page'
time_prefix='0324-0401'

# Filter and tokenization
echo 'tokenizing original files...'
for file in `ls $data_path/*.rowori`; do
        prefix=`echo $file | awk -F '.' '{print $1}'`
	#python src/tokens.py '-s' $file "$prefix.token" 'c' 'data/stopwords.txt'
done
# Build word dict
echo 'building word dictionary...'
cat $data_path/*.token | src/extract_words.py None | sed 's/ /\n/g'| sort > data/"$time_prefix"_word_dict.txt
echo 'merging tokens for each day...'
for file in `ls $data_path/*.token`; do
        prefix=`echo $file | awk -F '.' '{print $1}'`
	echo -e $prefix'\t'`cat $file | awk '{printf("%s ", $0)}'` ; 
done > data/"$time_prefix"_token_merge.txt

echo 'generating topK words for each day...'
for file in `ls $data_path/*.token`; do
        prefix=`echo $file | awk -F '.' '{print $1}'`
	echo -e $prefix'\t'`cat $file | src/extract_words.py 50`; 
done > data/"$time_prefix"_top50_keyword_merge.txt

echo 'generating word distribution over days...'
cat data/"$time_prefix"_token_merge.txt | awk -F '\t' '{print $2}' | src/get_word_distribution.py data/"$time_prefix"_word_dict.txt > data/"$time_prefix"_word_dist.txt

echo 'generating raw statistical data...'
cat data/"$time_prefix"_word_dist.txt | awk '{for(i=3;i<=NF;i++){printf("%d ",$i)}printf("\n")}'| src/statistic_word.py > data/"$time_prefix"_word_exp.txt

echo 'generating final statistical data...'
paste -d ' ' data/"$time_prefix"_word_dist.txt data/"$time_prefix"_word_exp.txt | awk '{printf("%s %s %s ",$1,$2,$NF);for(i=3;i<NF;i++){printf("%s ",$i)}print ""}' | sed 's/,/ /g' > data/"$time_prefix"_word_stat.txt

sort -n -r -k5 data/"$time_prefix"_word_stat.txt | head -5000 | awk '{printf("%s %s %s\n",$1,$2,$5)}'> data/"$time_prefix"_keyword_dict.txt

