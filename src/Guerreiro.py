from src.Personagem import personagem;

class guerreiro(personagem):
    def __init__(self, nome):
        super().__init__(nome, vida = 150, maxvida = 150, ataque = 20)
        