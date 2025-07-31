from collections import deque

d = deque()
num_of_operations = int(input())
for i in range(num_of_operations):
    command = input().split()
    
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0] == 'pop':
        d.pop()
    elif command[0] == 'popleft':
        d.popleft()
        
print(' '.join(d))