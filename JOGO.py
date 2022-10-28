import sys
import pygame as pg

from CONFIG_PERSONAGEM import ConfigPersonagem
from PERSONAGEM import Personagem

class Jogo:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(
            (ConfigPersonagem.SCREEN_WIDTH, ConfigPersonagem.SCREEN_HEIGHT))

        px = ConfigPersonagem.POSX_PERSONAGEM
        py = ConfigPersonagem.POSY_PERSONAGEM
        
        self.player = Personagem(posicao=(px,py))
        self.clock = pg.time.Clock()
    def run(self):
        while True:
            self.eventos()
            self.desenha()
    
    def eventos(self):
        pg.event.get()
        
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE]:
            sys.exit(0)

        if keys[pg.K_w]:
            self.player.mover_negativo()
            self.player.atualizar_posy()
        elif keys[pg.K_d]:
            self.player.mover_positivo()
            self.player.atualizar_posx()
        elif keys[pg.K_s]:
            self.player.mover_positivo()
            self.player.atualizar_posy()
        elif keys[pg.K_a]:
            self.player.mover_negativo()
            self.player.atualizar_posx() 
        else:
            self.player.parar()

        if keys[pg.K_w] and keys[pg.K_d]:   #x+ y-
            self.player.mover_positivo_diagonal()
            self.player.atualizar_posx()
            self.player.mover_negativo_diagonal()
            self.player.atualizar_posy()
        elif keys[pg.K_w] and keys[pg.K_a]: #x- y-
            self.player.mover_negativo_diagonal()
            self.player.atualizar_posx()
            self.player.atualizar_posy()
        elif keys[pg.K_s] and keys[pg.K_d]: #x+ y+
            self.player.mover_positivo_diagonal()
            self.player.atualizar_posx()
            self.player.atualizar_posy()
        elif keys[pg.K_s] and keys[pg.K_a]: #x- y+
            self.player.mover_negativo_diagonal()
            self.player.atualizar_posx()
            self.player.mover_positivo_diagonal()
            self.player.atualizar_posy()
        else:
            self.player.parar()
    def desenha(self):
        self.screen.fill('white')
        self.player.desenho(self.screen)
        self.player.desenho(self.screen)
        pg.display.flip()
        self.clock.tick(ConfigPersonagem.FPS)
        

def main():
    game = Jogo()
    game.run()

if __name__ == '__main__':
    main()
            