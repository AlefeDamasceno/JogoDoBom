import random

from src.Personagem import personagem;
from src.Arqueiro import arqueiro;
from src.Guerreiro import guerreiro;
from src.Mago import mago;

def ataque1(jogador):
    while True:
        op = input(f"{jogador.nome}: Atacar ou curar?").strip().lower()
        if op == "atacar":
            jogador.atacar(inimigo)
            break
        elif op == "curar":
            jogador.curar(jogador)
            break
        else:
            print("Escolha invalida.")

def ataque2(inimigo):
    while True:
        op = input(f"{inimigo.nome}: Atacar ou curar?").strip().lower()
        if op == "atacar":
            inimigo.atacar(jogador)
            break
        elif op == "curar":
            inimigo.curar(inimigo)
            break
        else:
            print("Escolha invalida.")

print("BEM VINDO AO SIMULADOR DE BATALHA")

cura_jogador = 5
cura_inimigo = 5
jogador = guerreiro("felipe")
inimigo = guerreiro("Paulo")

while jogador.vida > 0 and inimigo.vida > 0:
    ataque1(jogador)
    ataque2(inimigo)

    if inimigo.vida <= 0:
        break
    if jogador.vida <= 0:
        break