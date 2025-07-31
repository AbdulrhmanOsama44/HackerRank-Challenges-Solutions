n, m = input().split()
my_array = input().split()
set1 = set(input().split())
set2 = set(input().split())

def calculate_happiness(n, m, my_array, set1, set2):

    happiness = 0
    for i in my_array:
        if i in set1:
            happiness += 1
        elif i in set2:
            happiness -= 1

    return happiness
    
print(calculate_happiness(n, m, my_array, set1, set2))