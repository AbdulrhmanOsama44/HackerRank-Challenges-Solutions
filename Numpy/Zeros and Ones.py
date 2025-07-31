import numpy as np

num = list(map(int, input().split()))
print(np.zeros(num, int), np.ones(num, int), sep = '\n')