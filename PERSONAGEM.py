import pygame as pg
from CONFIG_PERSONAGEM import ConfigPersonagem
import math as mt

class Personagem:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0 

    def mover_positivo(self):
        self.velocidade = ConfigPersonagem.VEL_PERSONAGEM

    def mover_negativo(self):
        self.velocidade = -ConfigPersonagem.VEL_PERSONAGEM
    
    def mover_positivo_diagonal(self):
        self.velocidade = ConfigPersonagem.VEL_PERSONAGEM / mt.sqrt(2)

    def mover_negativo_diagonal(self):
        self.velocidade = -(ConfigPersonagem.VEL_PERSONAGEM / mt.sqrt(2))
        
        
    
    def parar(self):
        self.velocidade = 0

    def atualizar_posx(self):
        x,y = self.posicao
        novo_x = x + self.velocidade

        if (novo_x >= ConfigPersonagem.RAIO_PERSONAGEM) and ((novo_x + ConfigPersonagem.RAIO_PERSONAGEM) <= ConfigPersonagem.SCREEN_WIDTH ):
                self.posicao = (novo_x,y)
        
   
    def atualizar_posy(self):
        x,y = self.posicao
        novo_y = y + self.velocidade

        if (novo_y >= ConfigPersonagem.RAIO_PERSONAGEM) and ((novo_y + ConfigPersonagem.RAIO_PERSONAGEM) <= ConfigPersonagem.SCREEN_HEIGHT ):
                self.posicao = (x,novo_y)
    
   


    def desenho(self, screen):
        x = self.posicao[0]
        y = self.posicao[1]
        pg.draw.circle(
            screen,
            ConfigPersonagem.COR_PERSONAGEM,
            (x, y),
            ConfigPersonagem.RAIO_PERSONAGEM
        )
    
    def barra_de_vida(self):
        pass

    def tiro(self):
        pass
