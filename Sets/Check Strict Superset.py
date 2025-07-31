set_a = set(map(int, input().split()))
print(all(set_a.issuperset(other_sets := set(map(int, input().split()))) and set_a != other_sets for i in range(int(input()))))