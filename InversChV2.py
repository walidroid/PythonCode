def InversChV2(ch):
    res=""
    i=len(ch)-1
    while (i>-1):
        res+=ch[i]
        i-=1
    return res

word=input("Donner un mot : ")
print("l'inverse du mot est : ",InversChV2(word))

