class Bola:
    def __init__ (self, circ, mater, cor):
        self.circ=circ
        self.mater=mater
        self.cor=cor
        print(self.circ)
        print(self.mater)

    def mudar_cor(self):
        print(self.cor)
        self.cor=input("dgt uma cor: ")
        print(self.cor)


bola= Bola(70, "couro","preta")
bola.mudar_cor()
print(bola.circ)
print(bola.mater)