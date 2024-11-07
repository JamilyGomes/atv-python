total=0
while True:

    while True:
        y= float(input("dgt o valor da mercadoria : "))

        total= total+y
      
        if y==0.0:
            break
    print(total)

    while True:

        x=float(input("digite o valor do pagamento "))
        if total >x:
            print("Valor insuficiente")
        elif total<=x:
            z=x-total
            print("Seu troco foi de ",z)
            total=0
            break

    x=int(input("1-continuar\n0-Sair:\n"))
    if x ==0:
        break


cont=0
cont1=0
cont2=0
cont3=0
cont4=0
cont6=0