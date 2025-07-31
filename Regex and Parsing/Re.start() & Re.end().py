import re
S = input()
K = input()
pattern = re.compile(K)
r = pattern.search(S)
if not r: print('(-1, -1)')
while r:
    print(f'({r.start()}, {r.end() - 1})')
    r = pattern.search(S, r.start() + 1)