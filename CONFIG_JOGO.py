import pygame as pg

class ConfigJogo:
    pg.init()
    LARGURA_TELA = 900
    ALTURA_TELA = 450
    COR_TITULO = (0, 100, 0)
    FONTE_TITULO = 72
    FONTE_SUBTITULO = 32
    Tela = 0
    PARAOJOGOPORRA = False
    smallfont = pg.font.SysFont('Corbel',35)
    bigfont = pg.font.SysFont("comicsansms", 72)
    color = (255,255,255)
    color_light = (170,170,170)
    color_dark = (100,100,100)
    tipo_jog_1 = 0
    tipo_jog_2 = 0