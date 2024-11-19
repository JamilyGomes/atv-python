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

# from urllib.request import urlopen

# #url a ser requisitada
# url= 'https://www.example.com'

# #fazer a requisição http para a pag
# response= urlopen(url)

# #ler o conteudo da pag
# content= response.read().decode('utf-8')

# #exibir os primeiros 3000 caracteres do conteudo da pag
# print(content[:3000])

                    #///°fazer requisição http: urlopen
                    #///°ler conteudo da pag: read() em seguida decodificamos esse conteudo de bytes para uma string usando decode('utf-8')
                    #///°exibir os 3000 primeiros caracteres: print(content[3000])


#04.

# Manipulação de Parâmetros da URL

# Utilizando a URL `https://www.example.com/search?query=python&sort=desc`, escreva um código que recupere os parâmetros da consulta usando `urllib.parse.parse_qs()` e imprima o parâmetro `query` e o parâmetro `sort`.

# from urllib.parse import urlparse, parse_qs
# #///°importando as funções urlparse_qs, essas funções ajudam a analisar a url e recuperar os parametros da consulta.


# # url fornecida
# url= 'https://www.example.com/search?query=python&sort=desc'

# # parse da url
# parsed_url= urlparse(url)

# # recupera os parametros da consulta
# query_params= parse_qs(parsed_url.query)

# # imprime os parametros 'query' e 'sort'
# print('query:', query_params.get('query', [''])[0])
# print('sort:', query_params.get('sort', [''])[0])

                    #///°analisar url, isso divide a url em componentes como esquema(https), dominio(www.example.com), caminho(/search) e a parte da consulta(query=python&sort=desc)= parsed_url= urlparse(url)
                    #///°pega a parte da consulta da url (query=python&sort=desc) e a converte em um dicionario python, o dicionario resultante tera os parametros da consulta como chaves e seus valores como listas=query_params= parse_qs(parsed_url.query)
                    #///°usamos o metodo get do dicionario para obter os valores dos parametros query e sort. o metodo get retorna uma lista, entao pegamos o primeiro elemento da lista([0]). se o parametro nao existir, retornamos uma string vazia([''])= 
                    # print('query:', query_params.get('query', [''])[0])
                    # print('sort:', query_params.get('sort', [''])[0])


#05.

#  Construção de URL com Parâmetros de Consulta

# Escreva um código que utilize `urllib.parse.urlencode()` para criar uma URL com os seguintes parâmetros de consulta:
# - `user=john`
# - `id=123`
# - `status=active`

# A URL deve ser formada a partir do domínio `https://www.example.com`. Exiba a URL gerada no console.


# from urllib.parse import urlencode

# #parametros de consulta
# params= {
#     'user': 'john',
#     'id': '123',
#     'status': 'active'
# }

# #codifica os parametros de consulta
# query_string= urlencode(params)

# #dominio base
# base_url= 'https://www.example.com'

# #constroi a url completa
# full_url= f"{base_url}?{query_string}"

# #exibe a url gerada no console
# print(full_url)

                    #///°importar a funçao urlencode do modulo urllib.parse. usada para codificar os parametros de consulta em uma str de consulta= urlencode
                    #///°definir parametros de consulta em um dicionario. cada chave representa o nome de um parametro e cada valor representa o valor do parametro= params= 
                     # {
                     # 'user': 'john',
                     # 'id': '123',
                     # 'status': 'active'
                     # }
                    #///°usamos função urlencode para converter o dicionario de parametros em consulta em uma string de consulta. a string resultante sera algo como user=john&id=123&status=active= urlencode(params)
                    #///°definimos o dominio base da url. este é o inicio da url antes dos parametros de consulta= base_url= 'https//www.example.com' 
                    #///°concatenamos o dominio base com a string de consulta para formar a url completa. usamos uma f-string para facilitar a concatenaçao= full_url= f"{base_url}?{query_string}"
                    #///°exibimos a url completa no console= print(full_url)


#06.

# Redirecionamento de URL

# Usando a função `urllib.request.urlopen()`, tente fazer uma requisição para a URL `https://httpbin.org/redirect/1` e capture a URL para a qual a requisição é redirecionada. Exiba a URL de destino no console.


import urllib.request

# URL inicial
url = 'https://httpbin.org/absolute-redirect/1'

# Fazendo a requisição captura a resposta
response= urllib.request.urlopen(url)

# Captura a URL final após o redirecionamento
final_url = response.geturl()
print(f'URL de destino :, {final_url}')
                    #/// urlopen(): A função urlopen() faz a requisição HTTP. Se a URL inicial redireciona para outra, o urlopen() automaticamente segue o redirecionamento e retorna a resposta final.
                    #/// geturl(): O método geturl() retorna a URL final após o redirecionamento