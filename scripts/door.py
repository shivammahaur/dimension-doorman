import pygame as pg

class Door:
    def __init__(self, pos_x=10, pos_y=10, width=32, height=64):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.rect = pg.Rect(pos_x, pos_y, self.width, self.height)

    def draw(self, screen):
        pg.draw.rect(screen, (0, 255, 0), self.rect)

    def collision_player(self, player_rect):
        door_entered = False
        if self.rect.colliderect(player_rect):
            door_entered = True
            if door_entered == True:
                print("Door entered")