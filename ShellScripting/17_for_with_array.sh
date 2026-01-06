#!/bin/bash
#

myArray=( 1 2 3 Qasim false true 2.31 )
length=${#myArray[*]}

for (( i=0; i<$length; i++ ))
do
	echo "${myArray[$i]}"
done
