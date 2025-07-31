num_of_elements = int(input())
my_set = set(map(int, input().split()))
num_of_operations = int(input())
for i in range(num_of_operations):
    operation = input().split()[0]
    other_set = set(map(int, input().split()))
    if operation == 'update':
        my_set.update(other_set)
    elif operation == 'intersection_update':
        my_set.intersection_update(other_set)
    elif operation == 'difference_update':
        my_set.difference_update(other_set)
    elif operation == 'symmetric_difference_update':
        my_set.symmetric_difference_update(other_set)
print(sum(my_set))