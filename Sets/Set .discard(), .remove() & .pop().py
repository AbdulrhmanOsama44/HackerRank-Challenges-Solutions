n = int(input())
s = set(map(int, input().split()))
num_of_operations = int(input())
for i in range(num_of_operations):
    operation = input().split()
    if operation[0] == 'remove':
        try:
            s.remove(int(operation[1]))
        except KeyError:
            pass
    elif operation[0] == 'pop':
        try:
            s.pop()
        except KeyError:
            pass
    elif operation[0] == 'discard':
        s.discard(int(operation[1]))
print(sum(s))