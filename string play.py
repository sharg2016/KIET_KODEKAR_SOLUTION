n = str(input())
p=""
d=0

for i in n:
    if i.isdigit():
        d=d+int(i)

    else:
        p=p+i

print("".join(sorted(p))+str(d))