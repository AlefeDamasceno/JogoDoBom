from src.Mago import mago
from src.Guerreiro import guerreiro
from src.Arqueiro import arqueiro

def classSet():
    opc = 0
    print("[ 1 ] - Guerreiro\n[ 2 ] - Mago\n[ 3 ] - Arqueiro\n")
    while True:
        opc = int(input(f"Classe jogador:"))
        if opc in (1, 2, 3):
            break
    nome = input(f"Nome do jogador:")
    if opc == 1:
        escolhaJogador = guerreiro(f"{nome}")
    elif opc == 2:
        escolhaJogador = mago(f"{nome}")
    elif opc == 3:
        escolhaJogador = arqueiro(f"{nome}")

    return escolhaJogador
