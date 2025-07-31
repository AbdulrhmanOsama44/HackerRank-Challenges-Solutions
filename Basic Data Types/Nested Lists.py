def lowest_score_student(records_list):
    scores_list = []
    for i in range(len(records_list)):
        scores_list.append(records_list[i][1])
        
    sorted_scores_list = sorted(set(scores_list))
    second_lowest_grade = sorted_scores_list[1]
    
    names_second_lowest_score = []
    for i in records_list:
        if i[1] == second_lowest_grade:
            names_second_lowest_score.append(i[0])
            
    names_second_lowest_score = sorted(names_second_lowest_score)
    for i in names_second_lowest_score:
        print(i)

if __name__ == '__main__':
    lista = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append([name, score])
    lowest_score_student(lista)