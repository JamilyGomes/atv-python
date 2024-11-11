
def somatorio_lista_recursivo(lista):
    if not lista:
        return 0
    a, *b = lista
    return a + somatorio_lista_recursivo(b)
    
lista = [1, 2, 3, 4, 5]
print(somatorio_lista_recursivo(lista))  
