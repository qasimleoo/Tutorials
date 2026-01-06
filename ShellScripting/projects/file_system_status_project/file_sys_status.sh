#!/bin/bash
#

FU=$( df -H | grep nvme0n1p5 | awk '{print $5}' | tr -d % )
echo "$FU"

if [[ $FU -gt 70 ]]
then 
	echo  "Disk space is lower than 30% "
else
	echo "You have more than 30% free disk space"
fi
