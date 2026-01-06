#!/bin/bash
#

read -p "Which site do you wanna check? " site

ping -c 1 $site
# sleep 5s

if [[ $? -eq 0 ]]
then 
	echo "Successfully connected to $site"
else 
	echo "Failed to connect to the $site"
fi
