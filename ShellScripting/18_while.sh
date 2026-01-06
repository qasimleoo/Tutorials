#!/bin/bash
#
#
# While
#

iter=0
max=10

while [[ $iter -le $max ]]
do
	echo "$iter"
	let iter++
done
