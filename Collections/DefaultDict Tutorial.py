from collections import defaultdict

n, m = list(map(int, input().split()))
a_list = []
b_list = []

for i in range(n):
    a_list.append(input())

for j in range(m):
    b_list.append(input())
    
final_dect = defaultdict()
for k in b_list:
    if k in a_list:
        final_dect[k] = [i + 1 for i, x in enumerate(a_list) if x == k]
        print(' '.join(map(str, final_dect[k])))
    else:
        print(-1)