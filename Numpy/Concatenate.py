import numpy as np

n, m, p = list(map(int, input().split()))

array1 = np.array([list(map(int, input().split())) for i in range(n)])
array2 = np.array([list(map(int, input().split())) for i in range(m)])

print(np.concatenate((array1, array2), axis = 0))