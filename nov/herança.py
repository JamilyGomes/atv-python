#implementar uma classe Acount e BusinessAcount e fzr alguns testes
class Acount():
    def __init__ (self, number: int, holder: str, balance: float):
        self.number= number
        self.holder= holder
        self.balance= balance

        
    def dep(self, amount: float):
        #implementar dep
        if amount > 0:
            self.balance += amount
            print (f"Deposito de R${amount:} realizado com sucesso")
        else:
            print("Valor invalido")



    def withdraw(self, amount: float):
        #implementar o saque
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                print (f"saque de R${amount: } realizado com sucesso!")
            elif amount>self.balance:
                print("saldo insuficiente.")
            else: 
                print ("valor inválido")
      
        
    # def dep(self, amount: float):
    #     #implementar dep
    #     if valor > 0:
    #         self.__saldo += valor
    #         return f"Deposito de R${valor: .2f} realizado com sucesso"
    #     else:
    #         return "Valor invalido"
        

#         pass
        


# class BusinessAcount(Acount):
#     def __init__(self, number: int, holder: str, balance: float, loanLinit):
#         super().__init__(number, holder, balance)
#         self.loanLinit= loanLinit

#     def loam(self, amount: float):


#         pass