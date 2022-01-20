n = str(input())
st =[]

for i in n:
    st.append(i)

for i in range(0,len(st)):
    if(st[i]==st[i-1]):
        count+=1
    else:
        count = 0

    if count<2:
        print(st[i],end="")
