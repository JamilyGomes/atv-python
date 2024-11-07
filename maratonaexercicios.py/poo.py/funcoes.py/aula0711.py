# def hello():
#     print("olá!!")

# hello()

# def peixe(nome):
#     print("olá, nome!!")

# peixe("betta")

# def peixe(nome):
#     print("seja bem-vindo", nome)

# a= input("Digite seu nome= ")
# peixe(a)

# def hello (nome, idade):
#     print("Olá", nome, "\nSua idade é: ", idade)
# hello("Betta", 21)

# def hello (nome, idade):
#     print("Olá", nome, "\nSua idade é: ", idade)

# p= input("dgt seu nome: ")
# x= input("dgt sua idade: ")
# hello(p,x)

# def calcular_pgmnt(qtd_hrs, valor_hrs):
#     hrs= float(qtd_hrs)
#     taxa= float(valor_hrs)
#     if hrs<= 40:
#         salario= hrs*taxa
#     else:
#         h_excd= hrs-40
#         salario= 40*taxa+(h_excd*(1.5*taxa))
#     print(salario)

# def calcular_pgmnt(qtd_hrs, valor_hrs):
#     print(qtd_hrs, valor_hrs)

# a= float(input("dgt a qntd de hrs trabalhadas: "))
# b= float(input("dgt o valor das hrs trabalhadas: "))
# calcular_pgmnt(a, b)

# hrs= float(a)
# taxa= float(b)
# if hrs<= 40:
#     salario= hrs*taxa
# else:
#     h_excd= hrs-40
#     salario= 40*taxa+(h_excd*(1.5*taxa))
# print(salario)

# def soma (x, y):
#     result= x+y
#     return result

# a= int(input("Primeiro numero: "))
# b= int(input("Segundo numero: "))
# res= soma(a,b)  #atribuaaumavariavel
# print("Soma", res)

# def inverte(nome, sobrenome):
#     nomeInverso= sobrenome+","+nome
#     return nomeInverso
# nome= input("Nome: ")
# sobrenome= input("Sobrenome: ")
# invertido= inverte(nome, sobrenome)
# print("Olá", invertido)


##############boliviano

# def par(x):
#     if (x%2)==0:
#      return True
#     else:
#      return False
    
# while True:
#   num= int(input("Insira um numero: "))
#   if par(num):
#     print("É par")
#   else:
#     print("É impar")


# def cadastro():
#     name= input("dgt seu nome: ")
#     age= int(input("Idade: "))
#     return name,age

# print("Iniciando cadastro...")
# nome, idade= cadastro()
# print("Cadastro realizado com sucesso:")
# print("Seu nome é", nome, "e vc tem", idade, "anos de idade.")


# def soma (x, y, z):
#     result= (x+y)*z
#     return result

# a= int(input("Primeiro numero: "))
# b= int(input("Segundo numero: "))
# c= int(input("Terceiro numero: "))
# res= soma(a,b,c)  #atribuaaumavariavel
# print("resultado:", res)

# def neg(x):
#     if x<0:
#      return True
#     else:
#      return False
    
# while True:
#   num= int(input("Insira um numero: "))
#   if neg(num):
#     print("N")
#   elif num==0:
#     print("Zero")
#   else:
#     print("P")


def somaImposto(qtd_hrs, valor_hrs):
    hrs= float(qtd_hrs)
    taxa= float(valor_hrs)
    if hrs<= 40:
        salario= hrs*taxa
    else:
        h_excd= hrs-40
        salario= 40*taxa+(h_excd*(1.5*taxa))
    print(salario)