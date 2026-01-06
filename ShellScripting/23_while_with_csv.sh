#!/bin/bash
#
#
cat test.csv | awk "NR!=1 {print}" | while IFS="," read c1 c2 c3 c4 c5 c6
do
	echo "--------"
	echo $c1
	echo $c2		
	echo $c3
	echo $c4
        echo "--------"
done < test.csv
