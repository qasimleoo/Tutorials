# Intro
# Type of Module
# Import/Use modules
# if __name__ == '__main__' : Block 
# Module Search Path

# Module

# a file containing python definitions and statements (functions, variables, classes)
# they are like normal python files .. but contains only functions and classes 
# enables code reuse and organized


# Module Types

# Build-in modules: like math, os, sys, etc.
# User defined modules: Custom python files with .py extensions
# External modules: install via package managers (requests, numpy, pandas, flask, bs4, etc..)

# Definitions from a module can be imported into other modules or into the main module
# Every modules has a global variable __name__ as string

def func():
    pass

class myClass():
    pass

# Prints
# print(__name__)         # root level
# print(func.__name__)    # function level
# print(myClass.__name__) # class level


# How to import?

# i. Basic Import
# import <module_name>

# ii. Import specific functions
# from <module_name> import <name(s)>

# iii. Alias import  # for lengthy module names
# import <module_name> as <alt_name>
# from <module_name> import <name(s)> as <alt_name>

# iv. Wildcard import 
# from <module_name> import * 


# Examples

# import custom_module
# custom_module.greet()
# custom_module.say_yes()

# from custom_module import greet
# from custom_module import say_yes
# greet()
# say_yes()

# import custom_module as cm
# cm.say_yes()
# cm.greet()

# from custom_module import *
# greet()
# say_yes()




# if __name__ == '__main__' : usage/purpose?
# Suppose you make custom module(s) file(s) and they have some lines that don't need functions to run or you run the functions/classes inside the same module file itself.. when imported to other file(s) .. they will run automatically.. so to avoid that run .. we can add a check of if __name__ is __main__ run only then otherwise it won't run
# import custom_module


# module search path

# i. current directory
# ii. Environment variable: PYTHONPATH
# iii. Standard library
# iv. Third-Party pkg directory (site-pkg): like install with pip

