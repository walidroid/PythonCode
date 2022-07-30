def strTosomme(ch):
    pos=ch.find("+")
    if pos<0 : res=eval(ch[:]) # ch[0:len(ch)]
    elif pos==0 : res=eval(ch[:]) #+45 ==> 45 !
    else : res=eval(ch[0:pos])+eval(ch[pos+1:])
    return res
eq=input("Donner une operation d'addition : ")
print(strTosomme(eq))
