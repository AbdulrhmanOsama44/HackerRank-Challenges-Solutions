from itertools import permutations

string, k = input().split()
for i in sorted(list(permutations(string, int(k)))):
    print(''.join(i))