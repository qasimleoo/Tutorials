#!/bin/bash
#
#
#

read -p "Enter a number: " num

myFunc() {
	echo "----- User -----"
	echo "$1"
	echo "$2"
	echo "$3"
}

myFunc $num 34 21 Qasim New

myFunc Hey My 2 4
