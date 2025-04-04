import pygame as pg
from config import SCREEN_WIDTH, SCREEN_CAPTION, SCREEN_HEIGHT
from scripts.player import Player
from scripts.door import Door

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(SCREEN_CAPTION)
player = Player()
door = Door()
clock = pg.time.Clock()
running = True

while running:
    # check for exit event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    player.movement()
    door.collision_player(player.rect)
    player.interact_door(door.rect)

    # screen background
    screen.fill("red")

    door.draw(screen)
    player.draw(screen)

    # Target FPS
    clock.tick(60)

    # update display
    pg.display.flip()

pg.quit()