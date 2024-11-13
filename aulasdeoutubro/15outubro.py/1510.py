# nota1= float(input("dgt sua primeira nota= "))
# nota2= float(input("dgt sua segunda nota= "))

# media= (nota1+nota2)/2

# if media== 10:
#     print("aprovado com distinção")

# elif media >= 7:
#     print("aprovado")

# else:
#     print("reprovado")



# salAtual= float(input("dgt seu salario= "))

# if salAtual <= 280.00:
#     porc= 20
# elif salAtual > 280.00 and salAtual < 700.00:
#     porc= 15
# elif salAtual >= 700 and salAtual < 1500.00:
#     porc= 10
# elif salAtual >= 1500.00:
#     porc= 5

# aumento= salAtual*porc/100
# total= aumento+salAtual

# print("salario atual: ", salAtual)
# print("aumento: ", aumento)
# print("total: ", total)
# print("porcentagem: ", porc)


# nota1= float(input("dgt sua primeira nota= "))
# nota2= float(input("dgt sua segunda nota= "))
# nota3= float(input("dgt sua terceira nota= "))
# nota4= float(input("dgt sua quarta nota= "))

# media=(nota1+nota2+nota3+nota4)/4

# if  media >= 9.1 and media <= 10.0:
#     print("sua media é: A", "\nAprovado") 

# elif media >= 7.6 and media < 9.0:
#     print("sua media é: B", "\nAprovado")

# elif media >= 6.0 and media < 7.5:
#     print("sua media é: C", "\nAprovado")

# elif media >= 4.1 and media < 5.9:
#     print("sua media é: D", "\nReprovado")

# elif media >= 4.0 and media < 0.0:
#     print("sua media é: E", "\nReprovado")
 

a= input("telefonou p a vitima?")
b= input("esteve no local do crime?")
c= input("mora perto da vitima?")
d= input("devia p a vitima?")
e= input("ja trabalhou com a vitima?")

count=0
if a== "sim":
    count= +1
if b== "sim":
    count= +1
if c== "sim":
    count= +1
if d== "sim":
    count= +1
if e== "sim":
    count= +1

if count==5: 
    print("assassino")
elif count==4 or count==3:
    print("cumplice")
elif count==2:
    print("suspeito")
elif count==1 or count==0:
    print("inocente")
























