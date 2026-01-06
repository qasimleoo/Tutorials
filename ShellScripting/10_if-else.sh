#!/bin/bash
#
#
read -p "Enter your marks: " marks

# if [[ $marks -gt 80 ]]
if (( $marks > 80 ))
then 
	echo "You passed"

else 
	echo "You Failed"
fi
