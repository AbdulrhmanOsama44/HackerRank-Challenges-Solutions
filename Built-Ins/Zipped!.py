x, n = map(int, input().split())

marks = []
for i in range(n):
    scores = list(map(float, input().split()))
    marks.append(scores)
    
for j in list(zip(*marks)):
    print(sum(j) / n)