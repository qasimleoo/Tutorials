#!/bin/bash
#
#

FREE_SPACE=$(free -mt | grep Total | awk '{print $4}')
THRESHOLD=9000

if [[ $FREE_SPACE -gt $THRESHOLD ]] 
then
	echo "Enough mem"
else
	echo "RAM is lower than 9GBs"
fi
