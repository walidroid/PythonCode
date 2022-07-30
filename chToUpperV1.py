def chToUpper(ch):
    res=""
    for i in range(len(ch)):
        res+=chr(ord(ch[i])-32)
        
    return res

mot=input("Donner un mot : ")
print("En majuscule : ",chToUpper(mot))
