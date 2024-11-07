# tradutor = {}
# tradutor ["pineapple"]= "abacaxi"
# tradutor["apple"]= "maça"
# tradutor["orange"]="laranja"
# print(type(tradutor))
# print(tradutor)

# ##################

# tradutor1= {}
# tradutor1= {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(type(tradutor1))
# print(tradutor1)

# ###############ACHAR UM DEFINIDO

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1["apple"])

# tradutor1= {}
# tradutor1= {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# del(tradutor1 ["apple"])
# print(tradutor1)
# del(tradutor1["apple"])############ da erro pq ja n tem mais o elemento

# tradutor1= {}
# tradutor1= {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# del(tradutor1 ["apple"])
# print(tradutor1)
# print(tradutor1.pop("banana", "fruta n encontrada"))


#CLEAR LIMPA O DICIONARIO
# tradutor1= {}
# tradutor1= {"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# tradutor1.clear()

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print("pineapple" in tradutor1)

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print("laranja" in tradutor1.values())
# print(tradutor1.values())

#################################################################################trocar

# tradutor1={}
# tradutor1={"pineapple":"abacaxi", "apple":"maça", "orange":"laranja"}
# print(tradutor1)
# tradutor1["apple"]= "goiaba"
# print(tradutor1)

# dados={"crossfox":{"km":35000, "ano":2005}, "ds5":{"km":17000, "ano":2015}, "fusca":{"km":130000, "ano":1979}, "jetta":{"km":56000, "ano":2011}, "passat":{"km":62000, "ano":1999}}
# print(dados)
# print(dados.get("gol", "veiculo n encontrado"))

# t1={}
# t1={"Hisoto":{"idade":23}},
# {"Raquel":{"idade":31}},
# {"Day":{"idade":31}},
# {"Alexandre":{"idade":33}},
# {"Abel":{"idade":16}}
# # print(dic)

# for i in t1:
#     print(i, "-" , t1[i])

# try:
#     a= int(input("dgt uma palavra: "))
# except ValueError:
#     print("dgt apenas nmrs: ")
# except:
#     print("erro desconhecido")
# finally:
#     print("final do algoritmo")

#calculadora

while True:
    try:
    
        operador=input("dgt a operacao(1. soma, 2. sub, 3. mult, 4. div , 5. sair): ")
        
        num1= float(input("dgt o primeiro nmr: "))
        num2= float(input("dgt o sgnd nmr: "))

        if operador == "1":
            resultado= num1+num2
        elif operador=="2":
            resultado= num1-num2
        elif operador=="3":
            resultado= num1*num2
        elif operador=="4":
            resultado= num1/num2 
        elif operador=="5":
            print("operação invalida")
        print(resultado)

    except ValueError:
            print("dgt apenas nmrs: ")
    except:
        print("erro dscnhcd")


