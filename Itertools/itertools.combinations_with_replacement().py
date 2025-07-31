from itertools import combinations_with_replacement
string, k = input().split()
k = int(k)

for i in list(combinations_with_replacement(sorted(string), k)):
        print(''.join(i))