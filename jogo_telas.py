from cena_lore import Lore
from cena_inicial_com_class import Inicial
from cena_selecao_personagem import SelecaoPVP
from CONFIG_JOGO import ConfigJogo
import pygame as pg


class BatalhaEletronica:
    def __init__(self):
        pg.init()

        self.tela = pg.display.set_mode((
            ConfigJogo.LARGURA_TELA,
            ConfigJogo.ALTURA_TELA
        ))

    def rodar(self):
        ConfigJogo.Tela = 3
        while True:
            if ConfigJogo.Tela == 1:
                cena = Inicial(self.tela)        
                cena.rodar()
            if ConfigJogo.Tela == 2:
                cena = Lore(self.tela)
                cena.rodar()
            if ConfigJogo.Tela == 3:
                cena = SelecaoPVP(self.tela)
                cena.rodar()

       