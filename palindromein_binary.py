


n= input()
s=n

b = bin(int(n)).replace("0b", "")

if s==s[::-1] and b==b[::-1]:
    print("YES")

else:
    print("NO")
