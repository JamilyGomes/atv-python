
class Conta_Corrente:
    def __init__(self, n_conta, nome_correntista, saldo=0):
       
        self.n_conta = n_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo
 
    def alterar_nome(self, novo_nome):
       
        self.nome_correntista = novo_nome
        print(f"Nome alterado: {self.nome_correntista}")
 
    def deposito(self, valor):
       
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")
 
    def saque(self, valor):
   
        if valor > 0:
            if valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado com sucesso. Saldo atual: R${self.saldo:.2f}")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor de saque inválido. O valor deve ser maior que zero.")
 
x= float(input("valor deposito: "))
y= float(input("valor saque: "))
conta = Conta_Corrente(678910, "Jamily Gomes")
conta.deposito(x)
conta.saque(y)
conta.alterar_nome("Jamily Gomes")
