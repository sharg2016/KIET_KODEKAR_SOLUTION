def max(n):
    p=str(n)
    for i in range(len(p)-1):
        if(int(p[i])<int(p[i+1]) or int(p[i])==int(p[i+1])):

          print(True)

        else:
            print(False)



n=int(input())
max(n)
