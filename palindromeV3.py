def palindromeV3(ch):
    i=0
    l=len(ch)
    test=True
    while (i<l//2):
        if ch[i]==ch[l-1-i]:
            test=True
        else:
            test=False
        i+=1
    return test

mot=input("Donner un mot : ")
print(palindromeV3(mot))