import math
AB = int(input())
BC = int(input())
theta = math.degrees(math.atan2(AB, BC))
print(f'{round(theta)}\u00B0')