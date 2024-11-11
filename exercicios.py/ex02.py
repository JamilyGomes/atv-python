#função maior(a, b)

a=float(input("dgt um nmr: "))
b=float(input("dgt outro nmr: "))

def maior(a,b):
    if a>b:
        return a
    else:
        return b
if a>b:
    print(a, ", é maior")
elif a==b:
    print("os numeros são iguais.")
else:
    print(b, ", é maior")