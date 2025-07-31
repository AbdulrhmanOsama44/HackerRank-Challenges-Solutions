num_of_iterations = int(input())

for i in range(num_of_iterations):
    num_of_elements_in_set_a = int(input())
    elements_in_set_a = set(map(int, input().split()))
    num_of_elements_in_set_b = int(input())
    elements_in_set_b = set(map(int, input().split()))
    print(elements_in_set_a.issubset(elements_in_set_b))