import pickle

# to store objects

cars = ['1', '2', '3', '4', '5']
file = 'mycar.pkl'

fileobj = open(file, 'wb')
pickle.dump(cars, fileobj, protocol=pickle.HIGHEST_PROTOCOL)
fileobj.close()

fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)

print(pickle.LIST)
print(pickle.DEFAULT_PROTOCOL)
print(pickle.EMPTY_DICT)