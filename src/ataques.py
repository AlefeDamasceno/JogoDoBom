def ataque1(jogador, inimigo):
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


def ataque2(inimigo, jogador):
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