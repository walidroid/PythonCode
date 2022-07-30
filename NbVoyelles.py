def nbVoy(ch):
    res=0
    voyelles="oiyeau"
    for i in range(len(ch)):
        if (ch[i].lower()) in voyelles:
            res+=1
    return res

mot=input("Donner un mot :")
print(nbVoy(mot))
