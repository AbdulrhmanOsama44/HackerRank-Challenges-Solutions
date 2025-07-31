def operations_on_lists(num):
    lista = []
    for i in range(num):
        name_of_func = input().split()
        if name_of_func[0] == 'insert':
            lista.insert(int(name_of_func[1]), int(name_of_func[2]))
        elif name_of_func[0] == 'print':
            print(lista)
        elif name_of_func[0] == 'remove':
            lista.remove(int(name_of_func[1]))
        elif name_of_func[0] == 'append':
            lista.append(int(name_of_func[1]))
        elif name_of_func[0] == 'sort':
            lista.sort()
        elif name_of_func[0] == 'pop':
            lista.pop()
        elif name_of_func[0] == 'reverse':
            lista.reverse()

if __name__ == '__main__':
    N = int(input())
    operations_on_lists(N)