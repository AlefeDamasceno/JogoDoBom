from src.Personagem import personagem

class mago(personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 80, maxvida = 80, ataque = 40)