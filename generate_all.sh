#!/bin/bash

while read line
do
    IFS=$'\t'
    arr_line=($line)
    book="${arr_line[0]}"
    lang1="${arr_line[1]}"
    lang2="${arr_line[2]}"
    ./generate_tsv.py "src/${book}.yaml" "tsv/${book}.${lang1}-${lang2}.tsv" $lang1 $lang2
done < file_list.tsv
