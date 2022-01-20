n= str(input())
e=n
d=[]
c=""
for i in range(2,len(n)):
    if n[i]==n[i-1] and n[i]==n[i-2]:
        d.append(n[i-2])
        d.append(n[i-1])
        d.append(n[i])
        s="".join(d)

print(s)

