import pygame as pg
from settings import *
from player import Player
from world import Map

class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.running = True

    def new(self):
        player = Player('game2/png/player_sheet.png', (100, 100))
        #self.map = Map('game2/map/the_third.csv', 'game2/map/tilemap.png')
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(player)
        
    
    def _events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False

    def _draw(self):
        self.screen.fill((100, 100, 100))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def _update(self):
        self.all_sprites.update()
        
    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()
            
if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
