def is_all_upperV2(ch):
    test=True
    i=0
    maj="ABCDEFGHIJKLMNOPQRSTVWUYZ"
    while (test==True) & (i<len(ch)):
        if (ch[i] in maj): 
            i+=1
        else:
            test=False
    return test

print("Donner une chaine : ")
mot=input("==>")
print(is_all_upperV2(mot))