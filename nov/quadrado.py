class Quadrado():
    def __init__(self,lado):
        self.lado=lado
    def mostrar_area (self):
        print(self.lado**2)
    
    def mudar_valor_lado(self, novo_lado):
        self.lado=novo_lado
        print(self.lado*self.lado)


quadradox=Quadrado(6)

quadradox.mostrar_area()
quadradox.mudar_valor_lado(10)