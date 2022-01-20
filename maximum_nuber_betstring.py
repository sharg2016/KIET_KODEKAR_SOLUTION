n= input()
st=[]
c=0
for i in n:
    if i.isdigit():
        c=0
        st.append(i)
    else:
        c +=1

    if(c==1):
        st.append(" ")
print(st)