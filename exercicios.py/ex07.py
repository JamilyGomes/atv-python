#7. Crie uma função conta_vogais(texto) que retorne o número de vogais em uma string. "ERRADA"
def conta_vogais(texto):
    return sum(1 for letra in texto if letra.lower() in "aeiouáéíóú")
texto= input("dgt uma frase: ")
print(conta_vogais(texto))