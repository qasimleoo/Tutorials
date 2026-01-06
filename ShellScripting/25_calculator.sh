#!/bin/bash
#
#

set -x

echo "----------------------"
echo "Welcome to calculator"
echo "----------------------"

echo "a) for addition."
echo "b) for subtraction."
echo "c) for division."
echo "d) for multiplication."
echo "e) for modulus."
echo "f) for square."

read -p "Choose the operation: " operator
read -p "Enter first number: " num1
read -p "Enter second number: "  num2

addition () {
	echo $(( $1 + $2 ))
}

subtract () {
	echo $(( $1 - $2 ))
}

function div {
	echo $(( $1 / $2 ))
}

function product {
	echo $(( $1 * $2 ))
}

function mod {
	echo $(( $1 % $2 ))
}

function sq {
	echo $(( $1 ** $2 ))
}

case $operator in
	a) addition $num1 $num2;;
	b) subtract $num1 $num2;;
	c) div $num1 $num2;;
        d) product $num1 $num2;;
        e) mod $num1 $num2;;
        f) sq $num1 $num2;;
	*) echo "Invalid";;
esac

