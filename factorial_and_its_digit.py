n= int(input())
value=1
count=0

for i in range(1,n+1):
    value=value*i

while value>0:
    value=value//10
    count += 1

print(count)