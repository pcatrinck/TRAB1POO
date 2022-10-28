from turtle import Screen
import pygame as pg
from CONFIG_PERSONAGEM import ConfigPersonagem

class Personagem:
    def __init__(self, posicao):
        self.posicao = posicao
        self.velocidade = 0 

    def mover_positivo(self):
        self.velocidade = ConfigPersonagem.VEL_PERSONAGEM

    def mover_negativo(self):
        self.velocidade = -ConfigPersonagem.VEL_PERSONAGEM
    
    def parar(self):
        self.velocidade = 0

    def atualizar_posx(self):
        x,y = self.posicao
        novo_x = x + self.velocidade

        if (novo_x >= 0) and ((novo_x + ConfigPersonagem.LARGURA_PERSONAGEM) <= ConfigPersonagem.SCREEN_WIDTH ): 
            self.posicao = (novo_x,y)
        
   
    def atualizar_posy(self):
        x,y = self.posicao
        novo_y = y + self.velocidade

        if (novo_y >= 0) and ((novo_y + ConfigPersonagem.ALTURA_PERSONAGEM) <= ConfigPersonagem.SCREEN_HEIGHT ):
            self.posicao = (x,novo_y)
    
    def atualizar_posxy(self):
        x,y = self.posicao
        novo_x = x - (self.velocidade)
        novo_y = y + (self.velocidade)

        if (novo_y >= 0) and (novo_x >=0) and ((novo_y + ConfigPersonagem.ALTURA_PERSONAGEM) <= ConfigPersonagem.SCREEN_HEIGHT ) and \
            ((novo_x + ConfigPersonagem.LARGURA_PERSONAGEM) <= ConfigPersonagem.SCREEN_WIDTH ):
            self.posicao = (novo_x,novo_y)


    def desenho(self, screen):
        x = self.posicao[0]
        y = self.posicao[1]
        l = ConfigPersonagem.LARGURA_PERSONAGEM
        a = ConfigPersonagem.ALTURA_PERSONAGEM
        pg.draw.rect(
            screen,
            ConfigPersonagem.COR_PERSONAGEM,
            pg.rect.Rect(x, y, l, a),
        )
    
    def barra_de_vida(self):
        pass

    def tiro(self):
        pass
