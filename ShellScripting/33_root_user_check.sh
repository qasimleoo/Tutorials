#!/bin/bash
#
#
if [[ $UID -eq 0 ]]
then 
	echo "Yes a root user"
else
	echo "Nah.. not a root user"
fi
