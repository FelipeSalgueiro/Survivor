from Classes.Status import Status #Importando a classe status

#Classe Jogador
class Jogador:

    #Variáveis importantes do Jogador
    __Nome = ""
    __Clas = ""
    __Stat = Status


    #Método construtor
    def __init__(self, a, b, forc, agil, inte, sort):
        self.set_Nome(a) #Armazenando o Nome do Jogador
        self.set_Clas(b) #Armazenando a Classe do Jogador
        self.set_Stat(int(forc), int(agil), int(inte), int(sort)) #Armazenando os status do Jogador

    #Métodos de retorno das propriedades do Jogador
    def get_Nome(self):
        return self.__Nome
    
    def get_Clas(self):
        return self.__Clas
    
    def get_Stat(self):
        return self.__Stat
    
    #Métodos de modificação das propriedades do Jogador
    def set_Nome(self, x):
        self.__Nome = x

    def set_Clas(self, x):
        self.__Clas = x

    def set_Stat(self, c, d, e, f):
        self.__Stat = Status(c, d, e, f)