import random

class personagem:
    def __init__(self, nome, vida, maxvida, ataque):
        self.nome = nome
        self.vida = vida
        self.maxvida = maxvida
        self.ataque = ataque

    def atacar(self, inimigo):
        dano = random.randint(1, self.ataque)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} e causou {dano} de dano!")
        if (dano > self.ataque * (2/3)):
            print("ATAQUE CRÍTICO!!")
        if (inimigo.vida <= 0):
            print(f"{inimigo.nome} derrotado!")
        elif (inimigo.vida > 0):
            print(f"{inimigo.nome} ainda tem {inimigo.vida} de vida")

    def curar(self, jogador):
        if self.vida >= self.maxvida:
            print(f"{self.nome} já está com o máximo de pontos de vida!")
            return
        cura = random.randint(1, 20)
        vida_faltante = self.maxvida - self.vida
        cura_real = min(cura, vida_faltante)
        self.vida += cura_real
        print(f"{self.nome} se curou em {cura} pontos de vida!")
        print(f"{self.nome} agora tem {self.vida} pontos de vida!")


class guerreiro(personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 150, maxvida = 150, ataque = 20)
        
class mago(personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 80, maxvida = 80, ataque = 40)

class arqueiro(personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 120, maxvida = 120, ataque = 30)

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