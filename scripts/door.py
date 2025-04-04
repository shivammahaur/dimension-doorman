import pygame as pg

class Door:
    def __init__(self, pos_x=10, pos_y=10, width=32, height=64):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = pg.Rect(pos_x, pos_y, self.width, self.height)
        self.is_interactable = True
        self.is_open = False

    def draw(self, screen):
        pg.draw.rect(screen, (0, 255, 0), self.rect)

    def collision_player(self, player_rect):
        return self.rect.colliderect(player_rect)