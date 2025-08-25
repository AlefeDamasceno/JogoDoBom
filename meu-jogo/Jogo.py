import random

##Lazy Import
from src import *

print("BEM VINDO AO SIMULADOR DE BATALHA")


jogador = classSet()
inimigo = classSet()

while True:
    while True:
        if jogador.vida > 0 and inimigo.vida > 0:
            if jogador.vida > 0:
                ataque1(jogador, inimigo)
            if inimigo.vida > 0:
                ataque2(inimigo, jogador)
        else:
            break
    break
