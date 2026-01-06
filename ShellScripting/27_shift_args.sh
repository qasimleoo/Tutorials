#!/bin/bash
#
#
# To create a user .. provide name and description
#
echo "----- Creating user ------"

# use quotes to get 2nd arg full with more than 1 word
echo "Username is: $1"
echo "Description is: $2"


# Or use shift
echo "Using shift ------------------"
echo "Username is: $1"
shift
shift
echo "Decription is: $@"
