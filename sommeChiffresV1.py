def sommeChiffre(n):
    somme=0
    ch=str(n)
    for i in range(0,len(ch)):
        somme+=int(ch[i])
    return somme

w=int(input("Donner le nombre :"))
print("la somme est : ",sommeChiffre(w))