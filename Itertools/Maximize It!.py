K, M = map(int, input().split())
lists = [list(map(int, input().split()))[1 : ] for i in range(K)]

possible_sums = {0}
for j in lists:
    new_sum = set()
    for h in j:
        for k in possible_sums:
            new_sum.add((k + h ** 2) % M)
    possible_sums = new_sum
        
print(max(possible_sums))