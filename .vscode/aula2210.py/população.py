#a= 80.000 habitantes
#3% taxa anual de crescimento
#b= 200.000 habitantes
#1,5%  taxa anual de crescimento
#CALCULAR E ESCREVER O N DE ANOS NECESSÁRIOS PARA Q A POPULAÇÃO DO PAIS "A" ULTRAPASSE OU = A POPULAÇÃO B, MANTIDAS A TAXA DE CRESCIMENTO.


# a=80000
# b=200000

# cont=0

# while a<=b:
#     a=a+(a*3/100)
#     b=b+(b*1.5/100)
#     cont=cont+1
# print(cont)

#ALTERAR O ANTERIOR P INFORMAR AS POPULAÇÕES E AS TAXAS INICIAIS. VALIDAR ENTRADA E REPETIR OPERAÇÃO
# while True:
#     x=int(input("1-informa dados\n0-Sair:\n"))
#     if x ==1:
#         a=float(input("dgt a 1 população: "))
#         b=float(input("dgt a 2 população: "))
#         c=float(input("dgt a %: "))
#         d=float(input("dgt a %: "))
        
#         cont=0

#         while a<=b:
#             a=a+(a*c/100)
#             b=b+(b*d/100)
#             cont=cont+1
#         print(cont)
#     elif x ==0:
#         break


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


# cont=0
# cont1=0
# cont2=0
# cont3=0
# cont4=0
# cont6=0

# while True:
#         x=int(input("1-Lula\n 2-Dilma\n 3-Bozo\n 4-Betta 6=nulo"))
#         if x==1:
#             cont1=cont1+1
#         if x==2:
#             cont2=cont2+1
#         if x==3:
#             cont3=cont3+1
#         if x==4:
#             cont4=cont4+1
#         if x==6:
#             cont6=cont6+1
#         if x>0: