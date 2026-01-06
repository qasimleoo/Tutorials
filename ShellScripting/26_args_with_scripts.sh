#!/bin/bash
#
#

echo "First arg is $1"
echo "First arg is $2"


echo "All args are $@"
echo "Number of args are $#"


echo "Read all args using loop ----------"
for var in $@i
do
	echo $var
done
