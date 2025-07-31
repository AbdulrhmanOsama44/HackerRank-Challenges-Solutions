def check_cubes(cubes):
    left = 0
    right = len(cubes) - 1
    current_top = float('inf')
    
    while left <= right:
        if cubes[left] >= cubes[right]:
            chosen_cube = cubes[left]
            left += 1
        else:
            chosen_cube = cubes[right]
            right -= 1
        
        if chosen_cube > current_top:
            return 'No'
        
        current_top = chosen_cube
    
    return 'Yes'
    
T = int(input())
for i in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    print(check_cubes(cubes))