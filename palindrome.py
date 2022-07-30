def palindromeV1(ch):
    res=True
    l=len(ch)
    for i in range(l):
        if ch[i]==ch[l-1-i]:
            res=True
        else:
            res=False
    return res
#main programm
mot=input("Donner un mot : ")
print(palindromeV1(mot))

    