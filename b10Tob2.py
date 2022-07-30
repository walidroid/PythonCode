def B10ToB2(n):
    ch=""
    while (n!=0):
        ch=str(n%2)+ch
        n=n//2
    return ch


b10=int(input("Donner la valeur Base10 : "))
print("la valeur base 2 est : ",B10ToB2(b10))
