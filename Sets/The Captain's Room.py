from collections import Counter

K = int(input())
rooms_num = list(map(int, input().split()))
rooms_count = Counter(rooms_num)

for i, j in rooms_count.items():
    if j == 1:
        print(i)