n= int(input())
i=0
l=[]
l.append(0)
while(i<n):
    i=i+1
    l.append(i)
    i=i+2
    l.append(i)
    i=i+3
    l.append(i)

if n in l:
    print(1)
else:
    print(0)