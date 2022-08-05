def is_all_upper(ch):
    test=True
    i=0
    while (test==True) & (i<len(ch)):
        if (ch[i]>"A") & (ch[i]<"Z"): 
            i+=1
        else:
            test=False
    return test

print("Donner une chaine : ")
mot=input("==>")
print(is_all_upper(mot))