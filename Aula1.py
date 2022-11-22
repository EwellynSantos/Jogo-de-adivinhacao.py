import random
##jogo de adivinhação

def jogar_adivinhacao():
        print("Bem vindos ao jogo de adivinhação!")
        
        nSecreto = random.randrange(1,51)
        totalTentativas = 0
        pontos = 100

        print("Escolha o nível de dificuldade:")
        print("(1) Fácil (2) Médio (3) Difícil")

        nivel = int(input("Defina o nível:  "))
        print (nSecreto)
        if (nivel == 1):
                totalTentativas = 10
        elif (nivel == 2):
                totalTentativas = 5
        elif (nivel == 3):
                totalTentativas = 3


        for rodada in range(1,totalTentativas + 1):
                print("Tentativa {} de {}".format(rodada, totalTentativas))

                nUsuario = int(input("Digite um número entre 1 e 50: "))
                print("Você digitou ", nUsuario)

                if(nUsuario < 1 or  nUsuario > 50):
                        print("Você precisa digitar um número entre 1 e 50!")
                        continue

                if (nSecreto == nUsuario):
                        print("Você acertou e fez {} pontos!" .format(pontos))
                        break
                else:
                        if(nUsuario > nSecreto):
                                print("Você errou! Voce chutou um número maior que o secreto.")
                        elif(nUsuario < nSecreto):
                                print("Você errou! Voce chutou um número menor que o secreto.")
                        pontosPerdidos = abs(nSecreto - nUsuario)
                        pontos = pontos - pontosPerdidos
                


                totalTentativas = totalTentativas + 1

        print("Fim de jogo.")

if(__name__== "__main__"):
        jogar_adivinhacao()