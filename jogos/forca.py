def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de forca")
    print("*******************************")

    palavraSecreta = "banana".upper()
    letrasCertas = ["_" for p in palavraSecreta]
    enforcado = False
    palavraCompleta = False
    tentativas = 0

    print(letrasCertas)

    while not enforcado and not palavraCompleta:

        chute = input("Digite a letra: ")
        chute = chute.upper().strip()
        print("jogando...")

        if(chute in palavraSecreta):
            index = 0
            letraEncontrada = False
            for letra in palavraSecreta:
                if letra == chute:
                    print("encontrei {} na  posição {}".format(letra, index))
                    letrasCertas[index] = letra
                index += 1
        else:
            tentativas += 1
            print("{} não consta na palavra secreta".format(chute))

        print("faltando {} letra(s)".format(str(letrasCertas.count('_'))))

        enforcado = tentativas == 6
        palavraCompleta = "_" not in letrasCertas
        print(letrasCertas)

    if(palavraCompleta):
        print("Parabéns, você ganhou!")
    else:
        print("Que pena, você perdeu...")

    print("\n Fim do Jogo!")


if __name__ == "__main__":
    jogar()
