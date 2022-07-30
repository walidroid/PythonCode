from numpy import array
def NbMots(phrase):
    nb=0
    for i in range(len(phrase)):   #Nb words=Nb spaces+1 ;) 
        if phrase[i]==" ":nb+=1
    return nb+1
def phToTabV3(ph,t):
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
t=array([str]*NbMots(phrase))
phToTabV3(phrase,t)
print(t)

