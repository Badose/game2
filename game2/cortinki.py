import pygame as pg
from pathlib import Path
import sys

class Sprite_Sheet:
    def __init__(self, file_path, scale=1):
        sheet = pg.image.load(file_path).convert_alpha()
        w, h = sheet.get_size()
        last_size = (int(w*scale), int(h*scale))
        self.sheet = pg.transform.scale(sheet, last_size)
        self.w, self.h = self.sheet.get_size()
    def get_image(self, x, y, width, height):
        return self.sheet.subsurface(x, y, width, height)


