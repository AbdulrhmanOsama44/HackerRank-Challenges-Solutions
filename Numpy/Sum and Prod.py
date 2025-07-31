import numpy as np
n, m = map(int, input().split())

value = np.array([list(map(int, input().split())) for i in range(n)])
print(np.prod(np.sum(value, axis = 0)))