if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        line = input()
        line = line.split()
        name = line[0]
        marks = list(map(float, line[1:]))
        student_marks[name] = marks

    name = input()
    scores = student_marks[name]
    sum = 0
    for i in scores:
        sum = sum + i
    print("{:.2f}".format(sum/len(scores)))
