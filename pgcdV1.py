def pgcd(a,b):
    while not(a*b==0):
        if a>b:
            a=a-b
        else:
            b=b-a
    if a==0:return b
    else : return a

question=input("Tu veux tester ? :")
while question !="non":
    print("Donner a et b pour calculer le pgcd : ")
    a=int(input("a= "))
    b=int(input("b= "))
    print(pgcd(a,b))
    question=input("Tu veux tester autres chiffres ? :")