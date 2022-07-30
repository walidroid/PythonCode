def nbchiffres(n):
    ##In one line
    #return len(str(n))
    ##OR
    nb=0
    res=n
    while(res!=0):
        nb=nb+1
        res=res//10
    return nb
        
            

print("Donner un entier :")
a=int(input("a="))
print(nbchiffres(a))