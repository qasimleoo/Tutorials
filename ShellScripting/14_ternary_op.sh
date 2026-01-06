#!/bin/bash
#
#
# Cond1 && Cond2 || Cond3
#
#
read -p "Enter your age: " age

[[ $age > 18 ]] && echo "Adult" || echo "Minor"
