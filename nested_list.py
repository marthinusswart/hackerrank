if __name__ == '__main__':
    studentList = []
    minGrade = 100
    min2Grade = 100

    for _ in range(int(input())):
        name = input()
        score = float(input())
        student = [name, score]
        studentList.append(student)
        if (score < minGrade):
            minGrade = score
        elif (((score < min2Grade) and (score > minGrade)) or (min2Grade == 100)):
            min2Grade = score
        elif ((score > min2Grade) and (min2Grade == minGrade)):
            min2Grade = score

    secondLowestGrade = [x for x in studentList if x[1] == min2Grade]
    secondLowestGrade.sort()

    for student in secondLowestGrade:
        print(student[0])
    

