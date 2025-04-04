import pygame as pg
from config import SCREEN_WIDTH, SCREEN_CAPTION, SCREEN_HEIGHT

pg.init()

screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption(SCREEN_CAPTION)
running = True

while running:
    # check for exit event
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # screen background
    screen.fill("red")

    # update display
    pg.display.flip()

pg.quit()