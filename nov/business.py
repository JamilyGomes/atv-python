from herança import Acount

class BusinessAcount(Acount):
    def __init__(self, number: int, holder: str, balance: 0, loanLinit):
        super().__init__(number, holder, balance)
        self.loanLinit= loanLinit

    


    def deposit(self, amount, balance): 
        if self.amount> balance:
            print("depositado com sucesso!")
        else:
            print("valor invalido")


    def withdraw(self, amount, balance):
        if self.amount > balance:
            print("limite excedido")
        else: 
            super().withdraw(amount)
            self.balance += amount

    # def main():
    #     holder= input("dgt seu nome: ")
    #     balancex= float(input("dgt o saldo inicial: "))
    #     herançax= BusinessAcount(holder, balancex)

        # while True:
        #     print("\n1. consultar Saldo")
        #     print("\n2. Depositar")
        #     print("\n3. Sacar")
        #     print("\n4. Sair")
        #     escolha= input("escolha uma opção: ")

        #     if escolha == "1":
        #         herançax.balance()
    
    # print("titular", holder)
    # amount= int(input("dgt o valor do deposito: "))
    # print(amount)
    



















    # def withdraw(self):
    #     print(self.cor)
    #     self.cor=input("dgt uma cor: ")
    #     print(self.cor)
    # def loan(self, amount: float):
         
    # def withdraw(self, amount: float):
    #     #implementar o saque
    #         if amount > 0 and amount <= self.balance:
    #             self.balance -= amount
    #             return f"saque de R${amount: } realizado com sucesso"
    #         else: 
    #             return "saldo insuficiente"

    #     pass