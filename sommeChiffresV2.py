def sommeChiffresV2(n):
    s=0
    while(n!=0):
        s=s+(n%10)
        n=n//10
    return s

print("Donner l'entier : ")
chiffre=int(input("chiffre="))
print(sommeChiffresV2(chiffre))