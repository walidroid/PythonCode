def SaisirCh():
    ch=input("Donner une chaine : ")
    while ch.isnumeric() :
        ch=input("Donner une chaine : ")
    return ch
a=SaisirCh()
print(a.split("#"))