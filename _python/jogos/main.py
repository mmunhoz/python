import adivinhacao
import forca

print("*******************************")
print("Bem vindo ao JOGOS em Python")
print("*******************************")


print("(1))Forca (2)Adivinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    forca.jogar()
else:
    adivinhacao.jogar()
