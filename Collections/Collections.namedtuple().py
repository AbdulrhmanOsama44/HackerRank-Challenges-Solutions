from collections import namedtuple

num_of_students = int(input())
fields = input().split()
total_marks = 0
for i in range(num_of_students):
    Data = namedtuple('Data', fields)
    MARKS, CLASS, NAME, ID = input().split()
    i = Data(MARKS, CLASS, NAME, ID)
    total_marks += int(i.MARKS)
    
print('{:.2f}'.format(total_marks / num_of_students))