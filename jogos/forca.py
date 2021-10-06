import random


def apresentar():
    print("*******************************")
    print("Bem vindo ao jogo de forca")
    print("*******************************")


def carregarPalavra():
    with open("palavras.txt", "r") as arquivo:
        palavras = [p.strip() for p in arquivo]
    idx = random.randrange(0, len(palavras))
    return palavras[idx].upper()

def carregaPLaceholders(palavraSecreta):
    return ["_" for p in palavraSecreta]

def pedeChute():
    chute = input("Digite a letra: ")
    return chute.upper().strip()

def jogar():
    apresentar()
    palavraSecreta = carregarPalavra()
    letrasCertas = carregaPLaceholders(palavraSecreta)

    enforcado = False
    palavraCompleta = False
    erros = 0

    print(letrasCertas)

    while not enforcado and not palavraCompleta:
        chute = pedeChute()
        if(chute in palavraSecreta):
            index = 0
            for letra in palavraSecreta:
                if letra == chute:
                    print("encontrei {} na  posição {}".format(letra, index))
                    letrasCertas[index] = letra
                index += 1
        else:
            erros += 1
            print("{} não consta na palavra secreta".format(chute))
            desenha_forca(erros)

        print("faltando {} letra(s)".format(str(letrasCertas.count('_'))))

        enforcado = erros == 7
        palavraCompleta = "_" not in letrasCertas

        print(letrasCertas)

    if(palavraCompleta):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavraSecreta)

    print("\n Fim do Jogo!")


def imprime_mensagem_vencedor():
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


def imprime_mensagem_perdedor(palavra_secreta):
    print("Poxa, você foi enforcado!")
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


if __name__ == "__main__":
    jogar()
