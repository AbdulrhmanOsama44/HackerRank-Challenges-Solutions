import numpy as np
n, m = map(int, input().split())

value = np.array([list(map(int, input().split())) for i in range(n)])
print(f'{np.mean(value, axis = 1)}\n{np.var(value, axis = 0)}\n{round(np.std(value), 11)}')