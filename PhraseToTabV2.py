def phToTabV2(ph,t):
    
    ph=ph+" "
    while ph!="":
        pos=ph.find(" ")
        t.append(ph[0:pos])
        ph=ph[pos+1:]
    return t
    
print("Entrer une phrase : ")
phrase=input("phrase=")
t=[]
phToTabV2(phrase,t)
print(t)
