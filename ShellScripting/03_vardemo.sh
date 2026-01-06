#! /bin/bash
#
# Script to show how to use variables


# No spaces are allowed
a=10
name="Qasim"
age=28


echo "my name is $name and my age is $age"

name="Ali"

echo "my name is $name and my age is $age"


# Var to store the output the value
HOSTNAME=$(hostname)
whoami=$(whoami)

echo "Hostname of this PC is $HOSTNAME and the username is $whoami"

