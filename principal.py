from random import randint
import os
import uteis
import json
from time import sleep


#Inicializando as variaveis
monte1 = [] #Monte de cartas para o jogador
monte2 = [] #Monte de cartas para o computador
x = 0 #Variavel para escolher o indice da carta SUPER TRUNFO
jogBat = 0 #Quando o jogador vencer a batalha
compBat = 0 #Quando o computador vencer a batalha
opcao = "S" #Inicia o jogo com S na opcao

#Loop do jogo
while True:
    venc = ""
    monte1 = [] #Monte de cartas para o jogador
    monte2 = [] #Monte de cartas para o computador
    x = 0
    if opcao == "S":
        #escolhe numeros aleatorios para o jogador
        for c in range(0,13):#Executa este comando 14 vezes      
            while len(monte1) <= 12:
                i = randint(0,27) #Escolhe um numero de 0 até 27(28 cartas)
                if i not in monte1 and i != 6 and i != 22: #Verifica se o numero escolhido nao está no monte1
                    monte1.append(i) #Coloca os numeros escolhidos no monte1
        x = randint(0,13)
        monte1.insert(x,6) #Insere a carta Super trunfo no monte1 na posicao de indice aleatoria
                
        #escolhe numeros aleatorios para o computador
        for n in range(0,13):   
            
            while len(monte2) <=12: 
                j = randint(0,27) 
                if j not in monte2 and j not in monte1 and j !=22:
                    monte2.append(j)
        x = randint(0,13)
        monte2.insert(x,22)#Insere a carta Super trunfo no monte2 na posicao de indice aleatoria


        with open("cartas.json") as meu_json: #Abre o arquivo de cartas json
            cartas = json.load(meu_json)


        #Loop do jogo - Enquanto o monte1 ou o monte2 sejam maiores do que 0
        while True:
            if len(monte1) > 0 or len(monte2) > 0:
                os.system('cls' if os.name == 'nt' else 'clear') or None #Apaga a tela
                uteis.inicio() #Modulo para o cabeçalho do jogo

                uteis.placar(monte1, monte2, jogBat, compBat) #Modulo para o placar

                print("")
                
                uteis.mCartaPre(cartas[monte1[0]]) #Modulo que exibe somente a carta do jogador
                uteis.menu() #Modulo que exibe o menu de escolha de categoria
                catEscolha = int(input("\t\t==> "))

                #Se o jogador digitar a categoria errada, ficara no loop até digitar corretamente
                while True:
                    if catEscolha <= 0 or catEscolha > 5:
                        print("Categoria errada, escolha uma categoria correta!")
                        for c in range(3, 0, -1):
                            print(".")
                            sleep(1)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        uteis.inicio()
                        uteis.placar(monte1, monte2, jogBat, compBat)
                        print("")
                        uteis.mCartaPre(cartas[monte1[0]])
                        uteis.menu()

                        catEscolha = int(input("\t\t==> "))
                    else:
                        break


                #Após escolher a carta, refaz o inicio, placar, menu e mostra a carta do computador
                os.system('cls' if os.name == 'nt' else 'clear') or None
                uteis.inicio()

                #Se o jogador estiver com a carta SUPER TRUNFO, só perde se o comp tiver as cartas com final 1(A1, B1...)
                if (cartas[monte2[0]]['Modelo'] == "ST-2" or cartas[monte2[0]]['Modelo'] == "ST-1") and (cartas[monte1[0]]['ID'] == "A1" or cartas[monte1[0]]['ID'] == "B1" or cartas[monte1[0]]['ID'] == "C1" or cartas[monte1[0]]['ID'] == "D1" or cartas[monte1[0]]['ID'] == "E1" or cartas[monte1[0]]['ID'] == "F1" or cartas[monte1[0]]['ID'] == "G1"):
                    venc = "VOCE GANHOU!!"
                
                #Se o comp estiver com a carta SUPER TRUNFO, só perde se o jogador tiver as cartas com final 1(A1, B1...)
                elif (cartas[monte1[0]]['Modelo'] == "ST-1" or cartas[monte1[0]]['Modelo'] == "ST-2") and (cartas[monte2[0]]['ID'] == "A1" or cartas[monte2[0]]['ID'] == "B1" or cartas[monte2[0]]['ID'] == "C1" or cartas[monte2[0]]['ID'] == "D1" or cartas[monte2[0]]['ID'] == "E1" or cartas[monte2[0]]['ID'] == "F1" or cartas[monte2[0]]['ID'] == "G1"):
                    venc = "COMPUTADOR GANHOU!!"
                
                #Se o comp ou jogador nao tiver a carta SUPER TRUNFO, a decisao será de acordo com cada categoria
                else:
                
                    if catEscolha == 1:
                        if (cartas[monte1[0]]['Potencia'] > cartas[monte2[0]]['Potencia']):
                            venc = "VOCE GANHOU!!"                
                        elif cartas[monte1[0]]['Potencia'] < cartas[monte2[0]]['Potencia']:
                            venc = "COMPUTADOR GANHOU!!"
                        else:
                            venc = "EMPATE!!"
                            
                    elif catEscolha == 2:
                        if cartas[monte1[0]]['Velocidade'] > cartas[monte2[0]]['Velocidade']:
                            venc = "VOCE GANHOU!!"
                        elif cartas[monte1[0]]['Velocidade'] < cartas[monte2[0]]['Velocidade']:
                            venc = "COMPUTADOR GANHOU!!"
                        else:
                            venc = "EMPATE!!"

                    elif catEscolha == 3:
                        if cartas[monte1[0]]['Alcance'] > cartas[monte2[0]]['Alcance']:
                            venc = "VOCE GANHOU!!"
                        elif cartas[monte1[0]]['Alcance'] < cartas[monte2[0]]['Alcance']:
                            venc = "COMPUTADOR GANHOU!!"
                        else:
                            venc = "EMPATE!"
                            
                    elif catEscolha == 4:
                        if cartas[monte1[0]]['Peso'] > cartas[monte2[0]]['Peso']:
                            venc = "VOCE GANHOU!!"
                        elif cartas[monte1[0]]['Peso'] < cartas[monte2[0]]['Peso']:
                            venc = "COMPUTADOR GANHOU!!"
                        else:
                            venc = "EMPATE!"
                        
                    elif catEscolha == 5:
                        if cartas[monte1[0]]['Comprimento'] > cartas[monte2[0]]['Comprimento']:
                            venc = "VOCE GANHOU!!"
                        elif cartas[monte1[0]]['Comprimento'] < cartas[monte2[0]]['Comprimento']:
                            venc = "COMPUTADOR GANHOU!!"
                        else:
                            venc = "EMPATE!"
                


                uteis.placar(monte1, monte2, jogBat, compBat)
                print(" ")
                #print(monte1) #Somente para manutencao
                #print(monte2) #Somente para manutencao

                uteis.mCartaPos(cartas[monte1[0]], cartas[monte2[0]]) #Mostra as cartas do jogador e computador
                uteis.menuPos(catEscolha) #Mostra o menu após a escolha da categoria

            if venc == "VOCE GANHOU!!": #Se o jogador ganhar
                uteis.jogVence(cartas[monte1[0]], venc)
                if monte2 != "":
                    monte1.append(monte2[0]) #Coloca a carta do computador no final da lista do jogador
                    monte2.pop(0) #Excluir a primeira carta da lista do computador

                if monte1 != "":
                    monte1.append(monte1[0]) #Coloca a primeira carta do jogador no final da lista
                    monte1.pop(0) #Excluir a primeira carta da lista do jogador

            elif (venc == "COMPUTADOR GANHOU!!" ): #Se o computador ganhar
                uteis.compVence(cartas[monte2[0]], venc)
                if monte1 != "":
                    monte2.append(monte1[0]) #Coloca a carta do jogador no final da lista do computador
                    monte1.pop(0) #Excluir a primeira carta da lista do jogador
                if monte2 != "":
                    monte2.append(monte2[0]) #Coloca a primeira carta do computador no final da lista
                    monte2.pop(0) #Excluir a primeira carta da lista do computador

            else: #Se empatar
                uteis.empate(venc)
                if monte1 !="":
                    monte1.append(monte1[0]) #Coloca a primeira carta do jogador no final da lista
                    monte1.pop(0) #Excluir a primeira carta da lista do jogador
                
                if monte2 !="":
                    monte2.append(monte2[0]) #Coloca a primeira carta do computador no final da lista
                    monte2.pop(0) #Excluir a primeira carta da lista do computador
            
            #Termino do jogo
            if len(monte1) == 0 or len(monte2) == 0:
                if len(monte1) > len(monte2): #Se o monte1 for maior que o monte 2, jogador ganhou
                    jogBat += 1
                    print(f"\t\t{'VOCE GANHOU A BATALHA!!'}")
                else:
                    print(f"\t\t{'O COMPUTADOR GANHOU A BATALHA!!'}") #Se o monte2 for maior que o monte1, computador ganha
                    compBat += 1

                break
            else:
                input("Pressione a tecla ENTER...") #Após aparecer o resultado de quem ganhou o set, o programa espera para voltar ao Loop
            
        opcao = str(input("Continuar? [S/N] ")).strip().upper()
    else:
        break
print("\n\t\tFIM DO JOGO\n\n")
    

