def RemoveUselessSpaces(ch):
    p=ch.find("  ")
    while (p>0):
        ch=ch[:p]+ch[p+1:]
        p=ch.find("  ")
    return ch

phrase=input("Donner une phrase : ")
cleared=RemoveUselessSpaces(phrase)
print("Before : ",phrase," Length : ",len(phrase))
print("After : ",cleared," Length : ",len(cleared))
