def aPuisb(a,b):
    res=1
    for i in range(1,b+1):
        res=res*a
    return res

print("Donner a^n puis tape sur Entrer")
a=int(input("a="))
n=int(input("n="))
print(aPuisb(a,n))
