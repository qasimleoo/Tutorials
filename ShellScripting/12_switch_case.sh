#!/bin/bash
#
#

echo "Please choose an option"
echo "a to print date"
echo "b to list the current directory"
echo "c to check the current location of directory"
echo "1 to get running processes"

read choice

case $choice in
	a) date;;
	b) ls;;
	c) pwd;;
        1) ps;;
	*) echo "Invalid option";;
esac
