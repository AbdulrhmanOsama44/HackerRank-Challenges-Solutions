import re
T = int(input())
pattern = r'^[+-]?[0-9]*\.[0-9]+$'
answers = [bool(re.match(pattern, input().strip())) for i in range(T)]
print(*answers, sep = '\n')