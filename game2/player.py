import pygame as pg
from cortinki import Sprite_Sheet
from pygame.math import Vector2

class Player(pg.sprite.Sprite):

    speed = 2
    
    def __init__(self, sp_sheet_path, pos):
        super().__init__()

        sprite_sheet = Sprite_Sheet(sp_sheet_path, 2)
        self._load_images(sprite_sheet)
        self.image = self.walk_r[0]
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self):
        self.velocity = Vector2(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.velocity.y = -1
        if keys[pg.K_s]:
            self.velocity.y = 1
        if keys[pg.K_a]:
            self.velocity.x = -1
        if keys[pg.K_d]:
            self.velocity.x = 1

        if self.velocity.length() > 1:
            self.velocity.x = 0

        self.velocity *= Player.speed
        self.rect.center += self.velocity
        
    def _load_images(self, sheet):
        self.walk_r = []
        self.walk_l = []
        self.walk_u = []
        self.walk_d = []

        w, h = sheet.w//4, sheet.h//4
        for i in range(0, w*4, w):
            self.walk_r.append(sheet.get._image(i, 0, w, h))
            self.walk_l.append(sheet.get._image(i, h, w, h))
            self.walk_u.append(sheet.get._image(i, h*2, w, h))
            self.walk_d.append(sheet.get._image(i, h*3, w, h))
