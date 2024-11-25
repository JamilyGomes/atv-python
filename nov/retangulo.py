class Retangulo():
    def __init__(self,compr, larg):
        self.compr=compr
        self.larg=larg
   
    def X (self,compr, larg):
        self.compr= float(input("dgt o vlr do comprimento: "))
        self.larg= float(input("dgt o valor da largura: "))
        return print(self.compr, self.larg)
    def Area (self):
        return self.compr*self.larg
    def P (self):
        return ((self.compr*2)+(self.larg*2))
    
retangulo= Retangulo (0,0)
retangulo.X (0,0)
print(retangulo.Area())
print(retangulo.P())


