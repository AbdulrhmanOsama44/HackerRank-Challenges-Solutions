def average(student_set, name):
    for key, value in student_set.items():
        if key == name:
            print('{:.2f}'.format(sum(value) / len(value)))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average(student_marks, query_name)