def jogar_forca():

    print("Bem vindo ao jogo da forca!")


    palavra_secreta = "banana"
    errou = False
    acertou = False

    while(not errou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): 
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("...")

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar_forca()