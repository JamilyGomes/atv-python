class encapsulamento():
    def __init__ (self, x, y):
        self.__x=x
        self.__y=y

    def add(self):
        return self.__x + self.__y
    # print(self.__x)
    
    # def sub(self):
    #     return self.x - self.y
    
calc= encapsulamento(20,30)
print(calc.add())
calc.__x

######################
