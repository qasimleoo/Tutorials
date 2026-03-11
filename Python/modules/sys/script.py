

# Intro
# Key features of module
    # Important vars and function
# Why is it imp? and when do we use 
# Quiz

# sys module provides functions and vars that are used to interact with the python runtime environment .. it allows you to access and manipulate the system-specific params and functions that control system -specific params and functions that ultimately control the behavior of Python Interpreter.
# this module is especially useful when you need to handle cli args, interact with standard input/output or manage system-level information such as path and env

# Key Features
# 1. Important variables
# - sys.argv # cli args
# - sys.path # python path
# - sys.maxsize # largest supported length of containers
# - sys.version & sys.version_info 
# - sys.platform # for execution based on platform
# - sys.modules # manage imported modules 
# - sys.stdin, sys.stdout, sys.stderr


import sys

# print(type(sys.argv))
# print(f'Size of argv: {len(sys.argv)}')
# print(f'Values: {sys.argv}')

# # has one input at-least.. at 0th index which is file name itself
# # handy in case you wanna pass values via your command line
# # Normally you run `python3 script.py`.. and 0th index is the file itself

# # But with args
# # python3 script.py 12 Hello noway.sh
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])


# Path
# print(sys.path) # path of python in current dir, system, libraries.. 

# Modules
# print(sys.modules) # all imported modules
# print(len(sys.modules))
# import math
# print(len(sys.modules))

# Maxsize
# print(sys.maxsize) # based on system .. the max size that can be made inside this container e.g.,
# li = list(range(sys.maxsize)) # will give memory error as i don't have this much memory in my system - MemoryError
# li = list(range(sys.maxsize + 1)) # OverflowError


# Version info
# print(sys.version)
# print(sys.version_info)
# to run or do something based on version

# Platform
# print(sys.platform)


# Standard Input/Output/Error
# to read/write/error

# for words in sys.stdin:
#     if ('quit') == words.strip():
#         break
#     else:
#         print(f'Input: {words}')

# print("Exit")


# sys.stdout.write('Hello peeps\n')
# sys.stderr.write('Some error occurred\n')

# sys.stdout = open('./sys/output.txt', 'w')
# sys.stderr = open('./sys/error.txt', 'w')

# print("Starting division method")

# try:
#     1 / 0 
# except ZeroDivisionError as e:
#     print(f"Exception: {e}", file=sys.stderr)

# sys.stdout.close()
# sys.stderr.close()


# Important Functions
# - sys.exit()
# - sys.getsizeof() .. to get size of any object
# - sys.getrecursionlimit(), sys.setrecursionlimit(limit)
# Thread interval 
# System Version

# 0 or Empty for normal termination 
# sys.exit() 
# sys.exit(0) 
# any other number for failed termination
# sys.exit(2) 
# sys.exit(-1) 

# Custom message
# sys.exit("Custom message")


# Size of
# a = 'Hello World'
# print(sys.getsizeof(a)) # it won't be 4, 8 bytes as .. everything is object so you will get size of object 

# Recursion limit
print(sys.getrecursionlimit())
sys.setrecursionlimit(10)
print(sys.getrecursionlimit())


# Time to move from one thread to other
print(sys.getswitchinterval())
sys.setswitchinterval(0.001)
print(sys.getswitchinterval())


# When to use?
# - command line scripting
# - exiting/program termination
# - custom input/output
# - environment management
# - debugging and logging