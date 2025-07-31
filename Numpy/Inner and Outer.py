import numpy as np

array_a = np.array(list(map(int, input().split())))
array_b = np.array(list(map(int, input().split())))

print(np.inner(array_a, array_b))
print(np.outer(array_a, array_b))