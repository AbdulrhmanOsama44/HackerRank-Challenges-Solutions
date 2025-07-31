num = int(input())
for i in range(num):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as z:
        print('Error Code:', z)
    except ValueError as v:
        print('Error Code:', v)