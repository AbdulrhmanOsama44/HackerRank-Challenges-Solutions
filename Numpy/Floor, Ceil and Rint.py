import numpy as np
np.set_printoptions(legacy='1.13')
array = np.array(list(map(float, input().split())))
print(f'{np.floor(array)}\n{np.ceil(array)}\n{np.rint(array)}')