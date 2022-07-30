def InversChV1(ch):
    res=""
    for i in range(len(ch)-1,-1,-1):
        res+=ch[i]
    return res

word=input("Donner un mot : ")
print("l'inverse du mot est : ",InversCh(word))
