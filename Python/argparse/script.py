# CLI interface with argparse
# pip is a cli 
# you can create your own using argparse

# from argparse import ArgumentParser, Namespace
# parser = ArgumentParser()
# parser.add_argument('echo', help="Echos the given string")
# args: Namespace = parser.parse_args()

# print(args.echo)


# import argparse
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     args = parser.parse_args()

# Run using
# python script.py 
# python script.py -h 

# -h comes via argparse here

# Types of arguments:
# 1. Positional
# 2. Optional


# 1. Positional 
# They are mandatory .. you can't skip any

# import argparse
# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("number1", help="First Number")
#     parser.add_argument("number2", help="Second Number")
#     parser.add_argument("operation", help="Operation you wanna perform")
#     args = parser.parse_args()

#     num1 = args.number1
#     num2 = args.number2
#     operation = args.operation

#     if (operation == '+'):
#         print(int(num1) + int(num2))

# python script.py 123 442 +
# python script.py -h           # to get details

# python script.py 123 442      # throws error .. as positional arg


# 2. Optional
# to make them optional you need to add a double dash before args
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--num1", help="First Operand")
    parser.add_argument("--num2", help="Second Operand")
    parser.add_argument("--operation", help="+, -, %%, /, x", choices=['+', '-', '/', '%', '*'])

    args = parser.parse_args()

    operation = args.operation
    num1 = int(args.num1)
    num2 = int(args.num2)

    if (operation == '+'):
        print(num1 + num2)
    elif (operation == '-'):
        print(num1 - num2)
    elif (operation == '/'):
        print(num1 / num2)
    elif (operation == '%'):
        print(num1 % num2)
    elif (operation == '*'):
        print(num1 * num2)
    else:
        print("Please make sure all params are being entered.. `Num1 Operand Num2`")

# For optional args you need to change the input pattern
# for positional it was 
# `python file.py num1 num2 operand`

# for optional it is 
# python file.py --num1 number --num2 number --opration +,-,%..
# python script.py --num1 12 --num2 123 --operation +