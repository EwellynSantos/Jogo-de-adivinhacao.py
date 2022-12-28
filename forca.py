import random

def jogar_forca():

    imprime_abertura()
    palavra_secreta = carrega_palavra_secreta()

    letras_certas = inicializa_letras_certas(palavra_secreta)
    print(letras_certas)

    errou = False
    acertou = False
    tentativas = 0

    
    while(not errou and not acertou):

        chute = solicita_chute()
        
        if(chute in palavra_secreta):
            marca_acertos(chute, letras_certas, palavra_secreta)
        else:
            tentativas += 1
            desenha_forca(tentativas)

        errou = tentativas == 7
        acertou = "_" not in letras_certas
        print(letras_certas)

    if(acertou):
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)



def imprime_abertura():
    print("****************************")
    print("Bem vindo ao jogo da forca!")
    print("****************************")

def carrega_palavra_secreta():
    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
 
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

    
def inicializa_letras_certas(palavra):
    return["_" for letra in palavra]

def solicita_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute

def marca_acertos(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): 
            letras_certas[index] = letra
        index +=  1


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_msg_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_msg_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")        

if(__name__ == "__main__"):
    jogar_forca()