def lista(num1, num2, num3, num4):
    new_list = [[i, j ,k] for i in range(num1 + 1) for j in range(num2 + 1)
    for k in range(num3 + 1) if i + j + k != num4]
    print(new_list)

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lista(x, y, z, n)