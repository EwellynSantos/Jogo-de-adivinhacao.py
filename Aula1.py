import random
##jogo de adivinhação


print("Bem vindos ao jogo de adivinhação!")
 
nSecreto = random.randrange(1,51)
totalTentativas = 1

print(nSecreto)

for rodada in range(totalTentativas, 4, 1):
        print(f"Tentativa: {totalTentativas} de 3")

        nUsuario = int(input("Digite um número entre 1 e 50: "))
        print("Você digitou ", nUsuario)

        if(nUsuario < 1 and  nUsuario > 50):
                print("Você precisa digitar um número entre 1 e 50!")


        if (nSecreto == nUsuario):
                print("Você acertou!")
                break
        elif(nUsuario > nSecreto):
                print("Você errou! Voce chutou um número maior que o secreto.")
        else:
                print("Você errou! Voce chutou um número menor que o secreto.")


        totalTentativas = totalTentativas + 1

print("Fim de jogo.")