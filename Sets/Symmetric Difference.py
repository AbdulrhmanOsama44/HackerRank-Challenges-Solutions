m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))

symmetric_difference = sorted(set_a.symmetric_difference(set_b))
for i in symmetric_difference:
    print(i)