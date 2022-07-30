def palindromeV4(ch):
    chinv=ch[::-1]
    return ch==chinv

mot=input("Donner un mot : ")
print(palindromeV4(mot))