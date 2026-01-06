#!/bin/bash
#
#
# AND OPERATOR

read -p "What is your age? " age
read -p "Are you a Pakistani? (y (yes) - n (no)) " passport

if [[ $age -gt 18 ]] || [[ $passport == "y" ]]
then
	echo "Yes you can vote"
else 
	echo "You can not vote"
fi
