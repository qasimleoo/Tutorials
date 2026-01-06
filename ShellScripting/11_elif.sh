#!/bin/bash
#
#
read -p "Enter your marks: " marks

if [[ $marks -gt 80 ]]
# if (( $marks > 80 ))
then 
	echo "A"

elif [[ $marks -gt 70 ]]
then 
	echo "B"
elif [[ $makrs -gt 60 ]]
then
	echo "C"
elif [[ $marks -gt 50 ]]
then
	echo "D"
else 
	echo "F"
fi
