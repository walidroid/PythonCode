def TriTab(t,n):
    for i in range(0,n-1):
        for j in range(i+1,n):
            if t[i]<t[j]:
                aux=t[i]
                t[i]=t[j]
                t[j]=aux
    return t
l=[1,5,0]
print(TriTab(l,len(l)))
