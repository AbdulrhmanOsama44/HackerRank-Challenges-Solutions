from itertools import product

a = map(int, input().split())
b = map(int, input().split())

list_of_product = list(product(a, b))
for i in list_of_product:
    print(i, end = ' ')