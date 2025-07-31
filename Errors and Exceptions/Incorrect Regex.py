import re

for i in range(int(raw_input())):
    try:
        re.compile(raw_input())
        print('True')
    except:
        print('False')