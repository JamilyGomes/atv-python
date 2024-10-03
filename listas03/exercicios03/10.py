#mostra quantas vezes o numero 1 aparece
lista= [1, 2, 1, 5, 6, 4, 3, 1]
print(lista)
print(lista.count(1))

#receba vetor de 5 frutas mostre-os e depois substitua o segundo elemento do vetor
frutas= ["banana", "maça", "cereja", "uva", "goiaba"]
print(frutas)
frutas[1]= "laranja"
print(frutas)

#temperatura media de cada mes do ano, amarzene-as em uma lista. após calcule a media anual das temperaturas, mostre a maior e a menor.

jan= [30,28]
fev= [28,30]
mar= [25,22] 
abril= [22,18] 
maio= [18,20] 
jun= [15,20] 
jul= [14,14] 
ago= [16,20] 
set= [20,20] 
out= [23,20] 
nov= [27,20] 
dez= [29,20]


listas= [jan, fev, mar, abril, maio, jun, ago, set, out, nov, dez]
listas.extend([3, 4])
print(listas)


media_anual=sum(temperaturas)/len(temperaturas)
maior_temperatura= max(temperaturas)
menor_temperatura= min(temperaturas)

print(f"media anual das temperaturas: {media_anual:.2f}°C")

print(f"maior temperatura: {maior_temperatura}°C")

print(f"menor temperatura: {menor_temperatura}°C")

