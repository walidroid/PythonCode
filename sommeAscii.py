def SommeAscii(mot):
    res=0
    for i in range(len(mot)): # or range(0,len(mot))
        res=res+ord(mot[i])
    return res

ch=input("Donner le mot : ")
print("la somme des codes ASCII est : ",SommeAscii(ch))
