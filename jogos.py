import forca
import Aula1

def escolha_jogo():
    print("Escolha seu jogo!")
    print("(1) Forca   (2) Adivinhação")

    jogo = int(input("Qual jogo?  "))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar_forca()
    elif(jogo == 2):
        print("Jogando adivinhação")
        Aula1.jogar_adivinhacao()

if(__name__ == "__main__"):
    escolha_jogo() 