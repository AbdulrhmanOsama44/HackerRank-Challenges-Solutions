import re
N = int(input())
output = []
for i in range(N):
    current_line = input()
    
    if ':' in current_line:
        m = re.findall(r'#([0-9A-Fa-f]{6}|[0-9A-Fa-f]{3})', current_line)
        if m:
            output.extend(m)

for i in output:
    print(f'#{i}')