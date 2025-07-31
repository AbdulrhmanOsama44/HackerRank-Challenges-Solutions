import numpy as np
n, m = list(map(int, input().split()))

array = np.array([list(map(int, input().split())) for i in range(n)])
print(f'{np.transpose(array)}\n{array.flatten()}')