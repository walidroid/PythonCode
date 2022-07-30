def deleteUnitaire(n):
    nch=str(n)
    l=len(nch)-1   # 123 ==> 13 || 4356 ==> 436
    res=nch[0:l-1]+nch[l]
    return int(res)

no=int(input('Donner un nombre >=100 : '))
while no<100:
    no=int(input('Donner un nombre >=100 : '))
print("le resultat est : ",deleteUnitaire(no))