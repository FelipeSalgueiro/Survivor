from os import system #Biblioteca para poder limpar o terminal
from Classes.Jogador import Jogador #Chamando a classe Jogador

#Classe do menu de criação do Jogador
class CriacaoJogador:

    #Menu de criação do Jogador / Método que imprime o menu na tela e organiza as entradas do usuário
    def Comecar_Criacao(self):

        #Armazenamento do Nome e da Classe do jogador (classe a ser modificada)
        print("\nCrie seu personagem: ")
        nome = input("Nome: \n- ")
        classe = input("\nClasse: \n- ")

        #Arrays para organizar melhor o menu de distribuição de status
        status_nome = ["Força", "Agilidade", "Inteligência", "Sorte"]
        status_valor = []
    
        #Variável de opção do usuário, para que ele possa resetar seus pontos de status caso não esteja satisfeito
        opc = 'n'

        #Menu de distribuição de status
        while True:
            pontos_status = 20 #Pontos de status a serem distribuidos entre os 4 status
            status_valor.clear() #Limpar os valores dos status, caso o usuário decida redistribuir os pontos

            z = 0 #Variável contadora para saber em qual status estou mexendo agora
            for x in status_nome: #Com esse loop consigo imprimir o menu de distribuição de status mais de uma vez, para ficar organizado no código e bonito para o usuário
                system("cls")
                print ("\nStatus (", pontos_status, "pontos restantes ): ") #Informar quantos pontos de status ainda restam ao jogador

                y = 0 #Variável contadora para percorrer status anteriormente preenchidos
                while y < z: #Imprimir na tela status previamente preenchidos pelo jogador

                    print(status_nome[y], ": \n- ", status_valor[y], "\n", sep = "")
                    y += 1 #Incremento da variável contadora

                print(status_nome[z], ": ", sep = "") #Impressão do status a ser modificado atualmente
                status_valor.append(self.__VerificarInt(input("- "))) #Armazenamento do valor do status escolhido pelo usuário
                pontos_status -= status_valor[z] #Atualização de quantos pontos o usuário tem disponível

                z += 1 #Incremento da varíavel contadora

            system("cls") #Limpeza da tela

            #Última impressão dos status para o usuário
            print("\nStatus (", pontos_status, "pontos restantes ): ") 
            y = 0
            while y < 4:

                print(status_nome[y], ": \n- ", status_valor[y], "\n", sep = "")
                y += 1
            #Fim Última impressão dos status para o usuário

            opc = input("Manter esses status? (S/N)\n- ") #Verificar se o usuário deseja manter/redistribuir o status

            if(pontos_status < 0): #Caso o usuário tenha utilizado mais pontos de status que os 20 disponíveis
                input("Tentando trapacear? Por favor utilize no máximo 20 pontos de status!")
            elif(opc == 'S' or opc == 's' or opc == "Sim" or opc == "sim"): #Usuário decide manter os status e prosseguir
                input("Espero que não se arrependa...")
                J1 = Jogador(nome, classe, status_valor[0], status_valor[1], status_valor[2], status_valor[3]) #Armazenamento do personagem criado
                break #Sai do menu de distribuição de status
        #Fim menu de distribuição de status

        return J1 #Retorna o Jogador criado
    #Fim Menu de criação do Jogador
    
    #Verificação de valor inteiro / tratamento de erro
    def __VerificarInt(self, x):
        while True:
            try:
                return int(x)
            except ValueError:
                x = input("Valor Inválido! Por favor insira um valor válido: \n- ")