def estnum(ch):
    res=True
    for i in range(len(ch)):
        if ch[i] in "0123456789" :
            res=res & True
        
        else:
            res=False
    return res

print("Donner une chaine non numérique : ")
chaine=input("chaine=")
print(estnum(chaine))