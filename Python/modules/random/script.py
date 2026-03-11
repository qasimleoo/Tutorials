
# to generate random numbers

import random

var = random.random() # random val from 0.0 to 1.0
print(var)

# To generate a random integer value we have randint(start, end).. both are inclusive
var = random.randint(10, 20) 
print(var)

# To generate a random float value we have uniform(start, end).. both are inclusive
var = random.uniform(10, 20)
print(var)

# to get random vals from a list/tuple/string .. or any other sequence
colors = ['pink', 'red', 'green', 'yellow', 'cyan', 'beige']
print(random.choice(colors))

# choices().. want more than one random thing?
print(random.choices(colors)) # gives a list
print(random.choices(colors, k=3)) # gives a list

# to increase the random chance to come more you can use weight against the same list/tuple
colors_weights = [20, 1, 2, 3, 1, 1]
print(random.choices(colors, k=3, weights=colors_weights))

# shuffle - to shuffle vals you need to have a list
random.shuffle(colors) # updates the passed list
print(colors)

# randrange - to generate vals with a range and with allows steps like only evens .. odd.. addition in start value etc..
print(random.randrange(20)) 
print(random.randrange(20, 30)) # exclusive of end value unlike random.randint like range function 
print(random.randrange(20, 32, 4))

print(random.randbytes(8))