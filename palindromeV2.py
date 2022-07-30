def InversChV2(ch):
    res=""
    i=len(ch)-1
    while (i>-1):
        res+=ch[i]
        i-=1
    return res
def palindromeV2(ch):
    chInv=InversChV2(ch)
    if ch==chInv:
        return True
    else:
        return False

mot=input("Donner un mot : ")
print(palindromeV2(mot))
    