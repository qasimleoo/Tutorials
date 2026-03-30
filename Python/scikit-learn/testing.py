
import time
import numpy  as np

col = np.array([[1],
                [2],
                [3]])  # shape (3, 1)
row = np.array([[10, 20]])  # shape (2,)

print(col.shape, row.shape)
result = np.dot(col,row)
print(result)