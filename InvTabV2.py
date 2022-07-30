from numpy import array
def InvTabV2(t,n):
    for i in range(n//2):
        aux=t[i]
        t[i]=t[n-1-i]
        t[n-1-i]=aux
    return t

t=array([54,1,2,35,42,0],int)
print(t)

InvTabV2(t,len(t)) 
print(t)
