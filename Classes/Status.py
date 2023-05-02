class Status:

    #Status
    __Forca = 0
    __Agili = 0
    __Intel = 0
    __Sorte = 0

    #Método construtor para armazenar os valores do status
    def __init__(self, a, b, c, d):
        self.set_Forca(a)
        self.set_Agili(b)
        self.set_Intel(c)
        self.set_Sorte(d)

    #Métodos para obtenção dos status
    def get_Forca(self):
        return self.__Forca
    
    def get_Agili(self):
        return self.__Agili
    
    def get_Intel(self):
        return self.__Intel
    
    def get_Sorte(self):
        return self.__Sorte
    
    #Métodos para armazenamento de status
    def set_Forca(self, x):
        self.__Forca = int(x)

    def set_Agili(self, x):
        self.__Agili = int(x)
        
    def set_Intel(self, x):
        self.__Intel = int(x)

    def set_Sorte(self, x):
        self.__Sorte = int(x)