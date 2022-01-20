import operator

if __name__ == '__main__':
    li = []
    t = []
    lar =0
    for i in range(int(input())):
        name = input()
        score = float(input())
        t=[name,score]
        li.append(t)

    li.append(t)
    sort_list = sorted(li,key=operator.itemgetter(1))
    print(sort_list)
    for i in sort_list:
        if [i][1]>lar:
            lar = li[i][1]
    print(lar)

