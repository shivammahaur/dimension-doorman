import pygame as pg
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Player:
    def __init__(self, pos_x=SCREEN_WIDTH/2, pos_y=SCREEN_HEIGHT/2, speed=5):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.speed = speed
        self.width = 32
        self.height = 32
        self.rect = pg.Rect(pos_x, pos_y, self.height, self.width)

    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        if keys[pg.K_d]:
            self.rect.x += self.speed
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        if keys[pg.K_s]:
            self.rect.y += self.speed

    def draw(self, screen):
        pg.draw.rect(screen, (0, 0, 255), self.rect)