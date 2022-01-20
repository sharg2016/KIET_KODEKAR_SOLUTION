def list_com(x,y,z):
    n=int(input())
    li=[]
    vi=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                a=[i,j,k]
                li.append(a)


    for i in li:
        if i[0] + i[1] + i[2] > n or i[0] + i[1] + i[2] < n:
            b=[i[0], i[1], i[2]]
            vi.append(b)

    print(vi)








list_com(2,2,2)
