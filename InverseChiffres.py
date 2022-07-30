def inverseInt(n):
    a=n // 100
    b=(n // 10)%10
    c=n % 10
    res=c*100+b*10+a
    return res
chiffre=int(input("Donner l'entier à inverser : "))
print(inverseInt(chiffre))