n= int(input())
li=[]
newli=[]
for i in range(1000):
    if i%2==1:
        li.append(i)

for i in range(0,len(li)):
    if i%3==1 or i%3==0:
        newli.append(li[i])

if n in newli:
    print(1)

else:
    print(0)