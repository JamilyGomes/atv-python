class contaBanc():
    def __init__ (self, nome, saldo, cpf, senha):
        self.nome= nome
        self.__saldo= saldo
        self.__cpf= cpf
        self.__senha= senha

    def extrato(self, senha):
        if senha== self.__senha:
            return f"saldo: R${self.__saldo: .2f}"
        else:
            return "senha invalida"
    
    def dep(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Deposito de R${valor: .2f} realizado com sucesso"
        else:
            return "Valor invalido"
        
    def saque(self, senha, valor):
        if senha == self.__senha:
            if 0<valor<=self.__saldo:
                self.__saldo -= valor
                return f"saque de R${valor: .2f} realizado com sucesso"
            else: 
                return "saldo insuficiente"
        else:
            return "senha invalida"

        
        # __x=float(input("dgt sua senha: "))
        # self.senha= 91586924


   
        # if __x == self.senha:
        #     print("senha correta.")
        # else:
        #     print("senha incorreta.")

    # def extr(self):          
    #     return self.__x
        