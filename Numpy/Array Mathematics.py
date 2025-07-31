import numpy as np

n, m = list(map(int, input().split()))
array1 = np.array([list(map(int, input().split())) for i in range(n)])
array2 = np.array([list(map(int, input().split())) for i in range(n)])

print(f'{array1 + array2}\n{array1 - array2}\n{array1 * array2}\n{array1 // array2}\n{array1 % array2}\n{array1 ** array2}')