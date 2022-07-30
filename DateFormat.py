def DateFormat(date):
    ch=str(date)
    return ch[0:2]+"/"+ch[2:4]+"/"+ch[4:len(ch)]

d=int(input("Donner la date sous ce format 'jjmmaaaa' : "))
print("la date est : ",DateFormat(d))
