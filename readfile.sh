#!/bin/bash
if [ $# -eq 0 ];
then
	echo "Please input the file name!"
	exit
fi

if [ ! -f $1 ];
then
	echo "error file!"
	exit
fi

n=0
filename=$1
while read line;
do
	echo $line
	let n++
done < $filename
echo -e "\ntotal lines is $n"
