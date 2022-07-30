def InversChV4(ch):
    res=""
    for i in range(len(ch)):
        res=ch[i]+res  
    return res

word=input("Donner un mot : ")
print("l'inverse du mot est : ",InversChV4(word))


