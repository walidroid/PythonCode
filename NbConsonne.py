def nbConsonne(ch):
    nbVoy=0
    voyelles="oiyeau"
    signes=" ,;:!?'"
    # or
    #others="oiyeau ,;:!?'"
    #==> ch[i] in others
    for i in range(len(ch)):
        #if ch[i] in others:
        if (ch[i].lower()) in voyelles or (ch[i] in signes):
            nbVoy+=1
    nbCons=len(ch)-nbVoy
    return nbCons

mot=input("Donner un mot :")
print(nbConsonne(mot))

