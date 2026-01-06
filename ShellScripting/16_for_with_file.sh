#!/bin/bash
#

FILE="/home/leo/ShellScripting/16_iterator_file.txt"

j=0
for i in $(cat $FILE)
do
	echo "$j: $i"
#	j=$(( j+1 ))
	(( j++ ))
done
