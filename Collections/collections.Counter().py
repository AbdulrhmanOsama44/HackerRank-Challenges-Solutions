from collections import Counter

num_of_shoes = int(input())
list_of_sizes = list(map(int, input().split()))
num_of_customers = int(input())
counter_of_sizes = Counter(list_of_sizes)

total = 0
for i in range(num_of_customers):
    size, price = list(map(int, input().split()))
    if size in counter_of_sizes.keys():
        if counter_of_sizes[size] > 0:
            total += price
            counter_of_sizes[size] -= 1
print(total)