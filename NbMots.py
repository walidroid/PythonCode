def NbMots(phrase):
    nb=0
    for i in range(len(phrase)):   #Nb words=Nb spaces+1 ;) 
        if phrase[i]==" ":nb+=1
    return nb+1


print("Saisir une phrase : ")
ph=input("phrase=")
print("le nombre de mots est : ",NbMots(ph))
    