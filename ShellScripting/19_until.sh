#!/bin/bash
#
#

a=10

until [[ $a -ge 20 ]]
do
	echo "$a"
	a=$(( a+1 ))
done
