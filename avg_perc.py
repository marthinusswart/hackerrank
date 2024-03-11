if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    lst = student_marks[query_name]
    avg = sum(lst) / len(lst)
    avg = format(avg, '.2f')
    print(avg)