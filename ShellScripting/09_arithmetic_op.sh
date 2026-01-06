#!/bin/bash
#
#

# Math calculation

x=5
y=10

let mul=$x*$y

echo "Using let - Product: $mul"

let add=$x+$y
echo "Using let - Addition: $add"

echo "Using paranthesis - Subtraction: $(( $x-$y ))"
