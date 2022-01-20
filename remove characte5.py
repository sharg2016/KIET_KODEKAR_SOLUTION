n= str(input())
p= str(input())
d=""

for i in n:
    if i  in p:
        continue
    else:
        d=d+i

print(d)

