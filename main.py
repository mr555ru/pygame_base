import sys

import pygame
from pygame import *

wwidth = 800
wheight = 600

display = (wwidth, wheight)

bgcolor = "#000A0F"

GAME_SPEED = 50


class Game():
    def __init__(self, wwidth, wheight, bgcolor, game_speed, game_title="pygame window"):
        self.wwidth = wwidth
        self.wheight = wheight
        self.display = (wwidth, wheight)
        self.bgcolor = bgcolor
        self.game_speed = game_speed
        self.caption = game_title
        
    def init(self):
        pygame.init()
        self.UPDATE_GAME = pygame.USEREVENT + 1
        pygame.time.set_timer(self.UPDATE_GAME, self.game_speed)
        self.screen = pygame.display.set_mode(self.display)
        pygame.display.set_caption(self.caption)
        self.bg = Surface(display)
        self.bg.fill(Color(self.bgcolor))
        
    def exit(self):
        pygame.quit()
        
    def step(self):
        pass
    
    def get_key(self, event):
        pass
    
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()

def main():
    game = Game(wwidth, wheight, bgcolor, GAME_SPEED, "dummy")
    game.init()

    while 1:
        for e in pygame.event.get():
            if e.type == QUIT:
                game.exit()
                sys.exit()
            elif e.type == game.UPDATE_GAME:
                game.step()
            elif e.type == KEYDOWN or e.type == KEYUP:
                game.get_key(e)
        game.draw()

if __name__ == "__main__":
    main()
