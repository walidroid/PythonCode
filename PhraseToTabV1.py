def phToTabV1(ph,t):
    i=0
    ph=ph+" "
    while ph!="":
        pos=ph.find(" ")
        t[i]=ph[0:pos]
        ph=ph[pos+1:]
        i+=1
    #return t
    
print("Entrer une phrase : ")
phrase=input("phrase=")
t=[0]*8 #list of 8 elements ! bad method
phToTabV1(phrase,t)
print(t)