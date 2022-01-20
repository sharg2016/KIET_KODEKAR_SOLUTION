if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    li=student_marks.get(query_name)
    sum=0
    a=len(li)
    for i in li:
        sum=sum+i
        percentage=sum/3

    print("{:.2f}".format(percentage))


