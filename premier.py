def estpremier(n):
    test=True
    i=2
    while (test) and (i<=n //2):
        if n % i==0:
            test=False
        i=i+1
    return test

x=int(input("Donner un nombre:"))
if (estpremier(x)):
    print("Premier")
else:
    print("Non Premier")
    