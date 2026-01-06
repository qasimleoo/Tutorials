#!/bin/bash
#
#
# arrays
#

# Example 1

# index=2
# myArray=(1 5 12.2 String "Mutiple words String");
# echo "Value at $index index ${myArray[$index]}";


i=2
myArray=(1 4 3.51 String "Mutiple words string" false);

echo "Value at index $i is ${myArray[$index]}"
echo "Printing all: ${myArray[*]}"


echo "Length of the array is ${#myArray[*]}";


echo "values from index 1 to 4 ---- ${myArray[*]:1:4} ----"
echo "values from index 3 to END ---- ${myArray[*]:3} ----"
echo "values from index START to 4 ---- ${myArray[*]::4} ----"


# Updating Arrays
myArray+=(new 5 19);

# * is used to get all values as a single string
echo "New array values ${myArray[*]}"


# @ is used when getting each value as seprate strings
echo "New array values ${myArray[@]}"
