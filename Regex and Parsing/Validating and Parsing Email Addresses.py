import re
import email.utils
for i in range(int(input())):
    j = input()
    j = email.utils.parseaddr(j)
    if re.match(r'^[a-zA-Z][a-zA-Z0-9\-\_\.]+@[a-z]+\.[a-z]{1,3}$', j[1]):
        print(email.utils.formataddr((j[0], j[1])))