# introduced in python 3.7
# auto generates special methods like init, repr, eq based on class attributes you define

# init is constructor

from dataclasses import dataclass

@dataclass(frozen=True)
class Person:
    name: str='John'
    age: int=30
    height: float=170

# replaces the manual creation of constructor

# __init__()
# __repr__()
# __eq__()

# p1 = Person('Qasim', 24, 172.3)
# # p1.name = 'Ali' # remove frozen=True
# print(p1)
# print(p1.age)

# p2 = Person()
# print(p2)


# Meta classes - classes that control classes like objects control classes

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Creating class:", name)
        return super().__new__(cls, name, bases, attrs)
    
class Specie(metaclass=MyMeta):
    pass

# s = Specie()
# print(s.)