from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

combination = list(combinations(letters, k))

counter = 0
for i in combination:
    if 'a' in i:
        counter += 1
        
print(round(counter / len(combination), 3))