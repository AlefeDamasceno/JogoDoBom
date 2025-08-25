from src.Personagem import personagem

class arqueiro(personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 120, maxvida = 120, ataque = 30)
