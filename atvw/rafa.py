# from pydantic import BaseModel
# class usuario(BaseModel):
#     nome: str
#     idade: int
#     email: str
# usuario= usuario(nome="betta", idade=21, email="bettapx@example.com")
# print(usuario.nome)
# print(usuario.idade)
# print(usuario.email)

from pydantic import BaseModel
class usuario(BaseModel):
    nome: str
    idade: int
    sexo: str
usuario= usuario(nome="betta", idade=21, sexo="feminino")
print(usuario.nome)
print(usuario.idade)
print(usuario.sexo)