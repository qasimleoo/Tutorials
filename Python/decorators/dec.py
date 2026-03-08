# functions that takes another function .. makes changes and returns it

# Why do we need decorators?

# suppose you wanna notify/give a common message to people when any function is called .. 
# you can change the same function .. but what if there are more than 1 functions .. like you have in bigger numbers

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("GoodBye")
    return mfx

@greet
def hello():
    print("Hello peeps")

@greet
def add(a,b):
    print(a+b)

hello()
# greet(hello)() # comment @greet
# greet(hello())

# add(1,2)
# greet(add(4,5))
# greet(add)(4,5) # comment @greet