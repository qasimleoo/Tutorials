#!/bin/bash
#
#
myString="Hello this is a string"

myStringLength=${#myString}


# Length
echo "Length is: $myStringLength"

# Upper Case
echo "Upper case -------- ${myString^^}"

# Lower Case
echo "Lower case -------- ${myString,,}"

# Replace
replaceWord="Hello"
replaceWith="Hi"
myString=${myString/$replaceWord/$replaceWith}
echo "Replaced $replaceWord with $replaceWith --------- ${myString}"
echo "Length is: ${#myString}"


# Slice
echo "Sliced string from Index 4 to 12 ----------- ${myString:4:12}"

