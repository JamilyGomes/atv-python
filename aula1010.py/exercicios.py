senha= int(input("digite sua senha: "))
extrato= 0.00
x=0
if senha== 91586924:
    
    print("\n1. Extrato",
           "\n2. Deposito",
           "\n3. Saque",
           "\n4. Sair")

    

    opçao= int(input("digite a sua opção: "))
    if opçao== 1:
        print(extrato)

    elif opçao== 2:
        deposito= int(input("digite o valor do deposito: "))
        extrato=extrato+deposito
        print(extrato)

    elif opçao== 3:
        saque= int(input("digite o valor do saque: "))
        saque=extrato-saque
        print(saque)

    elif opçao== 4:
        sair= int(input("saindo"))

else:
    print("Senha invalida") 








