import re
m = list(map(lambda x: x.group(), re.finditer(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeiouAEIOU]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', input())))
if m == []:
    print(-1)
else:
    for i in m:
        print(i)