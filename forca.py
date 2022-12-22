import random

def jogar_forca():

    print("Bem vindo ao jogo da forca!")

    arquivo = open("palavra.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
 
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_certas = ["_" for letra in palavra_secreta]

    errou = False
    acertou = False
    tentativas = 0

    print(letras_certas)

    while(not errou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()
        
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): 
                    letras_certas[index] = letra
                index +=  1
        else:
            tentativas += 1

        errou = tentativas == 6
        acertou = "_" not in letras_certas
        print(letras_certas)

    if(acertou):
        print("Você ganhou!")
    else:
        ("Você perdeu...")
    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar_forca()

