from cortinki import png
import pygame as pg
from settings import *
from player import Player

pg.init()
clock = pg.time.Clock()
pg.display.set_caption(TITLE)
screen = pg.display.set_mode((WIDTH, HEIGHT))

player = Player(png/'player_sheet.png', (100, 100))
all_sprites = pg.sprite.Group()
all_sprites.add(player)


running = True
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            running = False
    player.move()
    screen.fill((100, 100, 100))
    all_sprites.draw(screen)
    clock.tick(FPS)
    pg.display.flip()
