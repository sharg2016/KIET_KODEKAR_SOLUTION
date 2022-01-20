'''n = int(input())
li=[]
ci=[]
for i in range(n):
    li.append(int(input()))

for i in li:
    h=1
    count = 0
    while(i>count):
        i = i-h
        h += 1
        count += 1
    ci.append(count)
    h=1
    count=0

for i in ci:
    print(i)'''

for i in range(int(input())):
    a = int(input())
    count = 0
    s = 0
    i = 1
    while(count<=a):
        count+=i
        i+=1
        s+=1
    s-=1
    print(s)
