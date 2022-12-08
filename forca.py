def jogar_forca():

    print("Bem vindo ao jogo da forca!")


    palavra_secreta = "banana"
    letras_certas = ["_","_","_","_","_","_"]
    
    errou = False
    acertou = False

    print = (letras_certas)

    while(not errou and not acertou):
        chute = input("Qual letra? ")
        chute = chute.strip()
        

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): 
                letras_certas[index] = letra
            index = index + 1

        print(letras_certas)

    print("Fim de Jogo")

if(__name__ == "__main__"):
    jogar_forca()