class Tabla:
    def __init__(self, numero):
        self.__numero = numero
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero):
        self.__numero = numero
    def Generar_tabla(self):
        for i in range(0, 11):
            print(str(self.__numero)+" * "+str(i)+" = "+str(self.__numero*i))