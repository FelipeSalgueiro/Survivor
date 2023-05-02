from os import system #Biblioteca para poder limpar a tela
from Classes.CriacaoJogador import CriacaoJogador
from Classes.Jogador import Jogador

x = 1 #Variável para poder manter o while rodando
J1 = Jogador

#While para o caso do usuário digitar um valor inválido
while(x == 1):
    print("\n\n")
    print("     ╭─━━━━━━━━━━━━─╮")
    print("     |   Survivor   |")#Título do jogo com formatação bonitinha
    print("     ╰─━━━━━━━━━━━━─╯")

    opc = input("        1 - Jogar\n        2 - Sair\n     ")#Menu

    if opc == "1": #Abrir o Jogo
        system("cls")
        J1 = CriacaoJogador().Comecar_Criacao()
        system("cls")
        #O print abaixo é temporário, apenas para que o if tenha algum retorno, dessa forma conseguindo saber se a criação de jogador está funcionando
        print(J1.get_Nome(), "é um", J1.get_Clas(), "e tem: \nForça:", J1.get_Stat().get_Forca(), "\nAgilidade:", J1.get_Stat().get_Agili(), "\nInteligência:", J1.get_Stat().get_Intel(), "\nSorte:", J1.get_Stat().get_Sorte())
        input()
    
    elif opc == "2": #Fechar o Jogo
        x = 2
    
    else: #Caso o usuário digite um valor inválido
        input("Valor inválido! Por favor digite 1 ou 2")

    system("cls") #Limpar a tela