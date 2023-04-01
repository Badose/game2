import pygame as pg
from settings import *
from player import Player
from world import Map

class Game:
    '''Общий класс для хранения игровых функций.'''
    def __init__(self):
        '''Создание игрового окна.'''
        pg.init()
        self.clock = pg.time.Clock()
        pg.display.set_caption(TITLE)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.running = True

    def new(self):
        '''Добавление в главный код новых объектов, груп.'''
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.map = Map(self, 'game2/map/map.csv', 'game2/map/rpg_tileset.png', 16)
        player = Player(self, 'game2/png/player_sheet.png', (100, 100))
        
    
    def _events(self):
        '''Создание игровых событий.'''
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.running = False

    def _draw(self):
        '''Отрисовка.'''
        self.screen.fill((100, 100, 100))
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def _update(self):
        '''Обновление спрайтов.'''
        self.all_sprites.update()
        
    def run(self):
        '''Создание игрового цикла.'''
        while self.running:
            self.clock.tick(FPS)
            self._events()
            self._update()
            self._draw()
            
if __name__ == "__main__":
    game = Game()
    game.new()
    game.run()
