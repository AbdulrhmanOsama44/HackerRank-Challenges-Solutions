string = input().strip()
new_string = ''.join(sorted(string, key = lambda x: (
    x.isdigit() and int(x) % 2 == 0,
    x.isdigit() and int(x) % 2 != 0,
    x.isupper(),
    x
)))
print(new_string)