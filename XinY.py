def XinY(x,y):
    chx=str(x);chy=str(y)
    ch=chy[0]+chx+chy[1]
    res=int(ch)
    return res
a=int(input("Donner la 1ère valeur : "))
b=int(input("Donner la 2ème valeur : "))
r=XinY(a,b)
print(r)