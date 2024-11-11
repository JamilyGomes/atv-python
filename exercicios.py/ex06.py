# Escreva uma função soma_lista(lista) que receba uma lista de números e retorne a 
# soma de todos os elementos''' 

x = float(input("Digite um nº: "))
y = float(input("Digite outro nº: "))
z = float(input("Digite mais um nº: "))

lista = soma_lista= [x, y, z]

def soma_lista(lista):
    soma=0
    for numero in lista:
        soma = + numero
        return soma
print(lista)
print(sum(lista))
