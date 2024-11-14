### Exercício 1: Análise de Componentes de URL


#01.

#Extração de Dados da URL
# Utilizando a URL `https://www.google.com/search?q=python+programming`, use o `urllib.parse.urlparse()` para extrair o domínio e o caminho da URL. Em seguida, exiba:
# - O domínio
# - O caminho (sem a parte da consulta)


# from urllib.parse import urlparse

# url= 'https://www.google.com/search?q=python+programming'
# parsed_url= urlparse(url)

# domain= parsed_url.netloc
# path= parsed_url.path

# print(f"Domain: {domain}")
# print(f"Path: {path}")

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#///°primeiro passo: importamos a função urlparse do módulo urllib.parse.
#///°segundo passo definimos a url q iremos analisar. No caso acima foi https://www.google.com/search?q=python+programming.
#///°terceiro passo usamos a função urlparse p/ analisar a url, isso divide a url em componentes, como esquema (protocolo), dominio, caminho, parametro, consulta e fragmento.
#///°quarto passo (extrair dominio) e caminho a partir do objeto retornado por urlparse, extraimos o dominio usando parsed_url.netloc e o caminho usando parsed_url.path.
#///°EXPLICAÇÃO DOS COMPONENTES:
#///°dominio(netloc): esta parte da url indica o servidor onde o recurso está hospedado. No exemplo, é www.google.com
#///°caminho (path): esta parte da url indica o caminho especifico no servidor onde o recurso pode ser encontrado. no exemplo, é /search
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

                    #///°EXTRAÇÃO DE NOVOS COMPONENTES:
                    #///°dominio: parsed_url.netloc
                    #///°caminho: parsed_url.path


#02.

#Análise de Componentes de URL
# Dada a URL `https://www.example.com/path/to/page?query=python&lang=pt`, utilize a função `urllib.parse.urlparse()` para analisar a URL e imprima os seguintes componentes:
# - Esquema
# - Domínio
# - Caminho
# - Consulta

# from urllib.parse import urlparse

#url a ser analisada
# url= 'https://www.example.com/path/to/page?query=python&lang=pt'

# #analisar url
# parsed_url= urlparse(url)

# #extrair os componentes
# esquema= parsed_url.scheme
# dominio= parsed_url.netloc
# caminho= parsed_url.path
# consulta= parsed_url.query

# #exibir os componentes
# print(f"Esquema: {esquema}")
# print(f"Domínio: {dominio}")
# print(f"Caminho: {caminho}")
# print(f"Consulta: {consulta}")

                    #///°EXTRAÇÃO DE NOVOS COMPONENTES:
                    #///°esquema: parsed_url.scheme
                    #///°consulta: parsed_url.query
#03.

# Recuperação de Conteúdo de uma Página Web
# Utilize a URL `https://www.example.com` e, com o auxílio de `urllib.request.urlopen()`, faça uma requisição HTTP para a página. Exiba os primeiros 3000 caracteres do conteúdo da página no console.

from urllib.request import urlopen

#url a ser requisitada
url= 'https://www.example.com'

#fazer a requisição http para a pag
response= urlopen(url)

#ler o conteudo da pag
content= response.read().decode('utf-8')

#exibir os primeiros 3000 caracteres do conteudo da pag
print(content[:3000])

                    #///°fazer requisição http: urlopen
                    #///°ler conteudo da pag: read() em seguida decodificamos esse conteudo de bytes para uma string usando decode('utf-8')
                    #///°exibir os 3000 primeiros caracteres: print(content[3000])


#04.


