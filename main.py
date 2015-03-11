#pylint: disable=trailing-whitespace,no-member,too-many-instance-attributes
#for fucks sake :D

"""Simple pygame base with controller"""
import sys

import pygame
from pygame import * #because everybody does it pylint: disable=wildcard-import,unused-wildcard-import

WWIDTH = 800
WHEIGHT = 600

BGCOLOR = "#000A0F"

GAME_SPEED = 50


class Game(object):
    """Controller of overall game logic and drawing"""
    
    def __init__(self, wwidth, wheight, bgcolor, game_speed, game_title="pygame window"):
        self.wwidth = wwidth
        self.wheight = wheight
        self.display = (wwidth, wheight)
        self.bgcolor = bgcolor
        self.game_speed = game_speed
        self.caption = game_title
        
    def init(self):
        """Initializes game window and logic."""
        #pylint: disable=attribute-defined-outside-init
        pygame.init()
        self.update_game = pygame.USEREVENT + 1
        pygame.time.set_timer(self.update_game, self.game_speed)
        self.screen = pygame.display.set_mode(self.display)
        pygame.display.set_caption(self.caption)
        self.bg = Surface(self.display) #pylint: disable=invalid-name,too-many-function-args
        self.bg.fill(Color(self.bgcolor))
        
    def exit(self): #pylint: disable=no-self-use
        """Ends pygame loop"""
        pygame.quit()
        
    def step(self):
        """Game logic goes here"""
        pass
    
    def get_key(self, event): #pylint: disable=redefined-outer-name
        """Processing key presses"""
        pass
    
    def draw(self):
        """Drawing goes here."""
        self.screen.blit(self.bg, (0, 0))
        pygame.display.update()

def main():
    """This is main loop"""
    game = Game(WWIDTH, WHEIGHT, BGCOLOR, GAME_SPEED, "dummy")
    game.init()

    while 1:
        for e in pygame.event.get(): #pylint: disable=invalid-name
            if e.type == QUIT: #pylint: disable=undefined-variable
                game.exit()
                sys.exit()
            elif e.type == game.update_game:
                game.step()
            elif e.type == KEYDOWN or e.type == KEYUP: #pylint: disable=undefined-variable
                game.get_key(e)
        game.draw()

if __name__ == "__main__":
    main()
