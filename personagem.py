class Personagem:
    def __init__ (self):
        self.lista_tipos = [0, 1, 2, 3, 4] #placeholder, mago, tank, lutador, atirador
        self.tipo = self.lista_tipos[0]
        self.color = "White"

    def escolhe_tipo (self, seletor: int):
        self.tipo = self.lista_tipos[seletor]

        if self.tipo == 1:
            self.color = "Yellow"
        if self.tipo == 2:
            self.color = "Cyan"
        if self.tipo == 3:
            self.color = "Red"
        if self.tipo == 4:
            self.color = "Blue"
        


