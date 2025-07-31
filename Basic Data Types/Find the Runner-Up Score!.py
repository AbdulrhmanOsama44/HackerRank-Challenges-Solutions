def runner_up_score(array):
    array = list(array)
    array.sort(reverse =True)
    for i in range(len(array)):
        if array[i] != array[i + 1]:
            runner_up = array[i + 1]
            break
        else:
            continue
    print(runner_up)



if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up_score(arr)