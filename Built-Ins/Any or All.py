n = int(input())
numbers = list(map(int, input().split()))
result = all(i > 0 for i in numbers) and any(str(i) == str(i)[ : : -1] for i in numbers)
print(result)