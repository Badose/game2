import pygame as pg
import pygame.freetype
from settings import TILE_SIZE

pg.init() #инициализация pygame
screen = pg.display.set_mode((544, 256))#создание окна
font = pygame.freetype.Font(None, 18)#шрифт
image = pg.image.load('map/rpg_tileset.png')#загрузка изображения
image = pg.transform.scale(image, (544, 256))#изменение размера изображения

ind = 0
for y in range(0, 256, TILE_SIZE):
    for x in range(0, 544, TILE_SIZE):
        font.render_to(image, (x+10, y+10), str(ind))
        ind += 1

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                run = False
    screen.blit(image, (0, 0))
    pg.display.flip()

        