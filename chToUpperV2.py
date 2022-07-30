def chToUpperV2(ch):
    #if ch contains punctuations signs
    res=""
    signes=" ,;:!?'"
    i=0
    while i<len(ch):
        if ch[i] in signes:
            res+=ch[i]
            i+=1
        else:
            res+=chr(ord(ch[i])-32)
            i+=1
        
    return res

mot=input("Donner un mot : ")
print("En majuscule : ",chToUpperV2(mot))

