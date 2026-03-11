

# a: int = '10'
# b = 'Qasim'

# print(a, b)


# # Python decides type on runtime
# # we can change type anytime
# a = 'Strong'
# a = 10 
# a = False
# a = 123.23
# # all are valid with not error checks

# we can use type hinting in functions to check it the value passed is valid type

def toUpperCase(val: str): # will start allowing you the suggestions as now it knows which type's data will be actually passed
    print(val)
    print(val.index("."))
    return val.upper()

print(toUpperCase("hello.xyz"))

# It only hints the type but not checks the type so it actually will behave like normal python .. it just helps in
# - readability
# - debugging

# you can install my[py] extension that will warn you if try yo pass an invalid type data to another type

def hello() -> str:
    return None

import typing
names: typing.List[str] = ["one", "two", "three"]

