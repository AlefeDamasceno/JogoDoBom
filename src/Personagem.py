import random

class personagem:
    def __init__(self, nome, vida, maxvida, ataque, maxcura=5):
        self.nome = nome
        self.vida = vida
        self.maxvida = maxvida
        self.ataque = ataque
        self.maxcura = maxcura

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
        if self.maxcura < 0:
            print(f"{self.nome} já usou todas as 5 curas!")
            return

        print(self.maxcura)
        self.maxcura -= 1
        cura = random.randint(1, 20)
        vida_faltante = self.maxvida - self.vida
        cura_real = min(cura, vida_faltante)
        self.vida += cura_real
        print(f"{self.nome} se curou em {cura} pontos de vida!")
        print(f"{self.nome} agora tem {self.vida} pontos de vida!")