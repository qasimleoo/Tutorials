#!/bin/bash
#
#

FILEPATH="/home/leo/ShellScripting/test.txt"

if [[ -f $FILEPATH ]]  # add ! for not check - revert the check
then 
	echo "Exists"
else 
	echo "Not exists - Creating file $PATHNAME"
	touch $FILEPATH
	echo "Created"
fi
