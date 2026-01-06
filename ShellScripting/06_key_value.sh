#!/bin/bash
#
#
# How to store the key value pairs
#

declare -A keyValue

keyValue=([name]=Qasim [age]=20)

echo "Name: ${keyValue[name]}"

echo "All *: ${keyValue[*]}"

echo "All @: ${keyValue[@]}";
