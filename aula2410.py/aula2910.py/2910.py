#imprima na tela nmrs impares de 0 a 50
# for x in range(1, 50, 2):
#     print (x)

#faça um algoritmo q imprima uma lista de times, adicionando um numeral. ex: entrada: 
#time= ["palmeiras", "curitiba", "sao paulo"]
#saida: palmeiras, curitiba, sao paulo

# time= ["1-Palmeiras", "2-Curitiba", "3-São Paulo"]
# for n in time:
#     print(n)


#faça um programa q receba dois nmrs e gere os nmr inteiros q estao no intervalo compreendido por eles.
# cont=0
# soma=0
# x= int(input("dgt um nmr= "))
# y= int(input("dgt outro nmr= "))
# for i in range (x+1, y):
#     print (i)
#     soma=soma+i
# print(soma)


# for i in range (1,21):
#      print (i, end= " ")


#faça um programa que leia 5 nmrs e informe a soma e a media dos nmrs

# cont=0
# soma=0

# for x in range(5):
#     b= int(input("dgt um nmr= "))
#     cont=cont+1
#     soma=soma+b
# print(soma)

# media=soma/cont
# print(media)

#fibonacci 
b= int(input("dgt um nmr= "))
x, y= 0, 1
print(x, y, end= " ")
for i in range(2,b+1):
    z=x+y
    print(z, end= " ")
    x=y
    y=z




    