import time

def usingFor():
    for i in range (50000):
        print (i)

def usingWhile():
    i = 0
    while (i < 50000):
        i = i+1
        print(i)

# start = time.time()
# usingFor()
# print('------------------')
# print('For Time')
# print(time.time() - start)
# print('------------------')

# start = time.time()
# usingWhile()
# print('------------------')
# print('While Time')
# print(time.time() - start)
# print('------------------')


# time.sleep(4)
# print("Time sleep")


print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S %Z"))