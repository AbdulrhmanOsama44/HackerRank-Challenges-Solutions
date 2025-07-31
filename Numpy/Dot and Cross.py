import numpy as np
n = int(input())

array_a = np.array([list(map(int, input().split())) for i in range(n)])
array_b = np.array([list(map(int, input().split())) for i in range(n)])
print(np.dot(array_a, array_b))