import random

def jogar():
    print("*******************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*******************************")

    numeroSecreto = random.randrange(1, 101)
    # print('hey -> {} sshhhh ;)'.format(numeroSecreto))

    tentativas = 0
    pts = 1000
    print("Selecione o nível de dificuldade (1(fácil), 2(médio) ou 3(difícil)")
    nivel = int(input('Nível: '))

    if (nivel == 1):
        tentativas = 20
    elif (nivel == 2):
        tentativas = 10
    elif (nivel == 3):
        tentativas = 5
    else:
        print("nível inválido")

    rodada = 1

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de  {}".format(rodada, tentativas))
        strChute = input("digite o seu número entre 1 e 100: ")
        chute = int(strChute)

        if chute < 1 | chute > 100:
            print("você deveria respeitar os limites do número")
            pts -= 10
            continue

        acertou = chute == numeroSecreto
        maior = chute > numeroSecreto
        menor = chute < numeroSecreto

        if (acertou):
            print("Você acertou! Pontuação final: {}".format(pts))
            break
        else:
            pts -= abs(numeroSecreto - chute)
            if maior:
                print("Errou. vc chutou ACIMA")
            elif menor:
                print("Errou. vc chutou ABAIXO")

        if rodada == tentativas:
            print("Fim das tentativas. O número secreto era {}. Sua pontuação final é {}".format(numeroSecreto, pts))

    print("\nFim do Jogo!")


if __name__ == "__main__":
    jogar()
