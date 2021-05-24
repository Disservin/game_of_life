from game_of_life import *
import sys
import pygame
import cProfile
from random import *
from pygame.locals import *

BOARD_SIZE = WIDTH, HEIGHT = 600,600   # WIDTH = size * qsize , HEIGHT = size *qsize  1280,720          600,600
DEAD_COLOR = 0,0,0
ALIVE_COLOR = 255,255,255
FPS = 24
fpsclock = pygame.time.Clock()

class LifeGame:
    def __init__(self) -> None:
        self.g = Game()
        self.qsize = 5
        self.sizex,self.sizey = WIDTH//self.qsize,HEIGHT//self.qsize  
        self.g.initalize(self.sizey,self.sizex)
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        pygame.init()
    def figure(self):
        self.g.overwrite_certain_pos(6,5,1)
        self.g.overwrite_certain_pos(6,6,1)
        self.g.overwrite_certain_pos(6,7,1)
        self.g.overwrite_certain_pos(7,6,1)
    def randomboard(self):              
        for i in range(self.sizey//4,self.sizey-self.sizey//4):
            for j in range(self.sizex//4,self.sizex-self.sizex//4):
                if randint(0,1) == 1:
                    self.g.overwrite_certain_pos(i,j,1)
    def spaceship(self):
        self.g.overwrite_certain_pos(1,3,1)
        self.g.overwrite_certain_pos(2,3,1)
        self.g.overwrite_certain_pos(3,3,1)
        self.g.overwrite_certain_pos(3,2,1)
        self.g.overwrite_certain_pos(2,1,1)        
    def start(self,iterations = float('inf')):
        current = self.g.board
        self.draw()
        n = 0
        self.g.nextstate()
        self.draw()
        while n < iterations:
            self.g.nextstate()
            self.draw()
            n+=1
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.key.key_code("p"):
                        return

    def run(self):
        self.screen.fill(DEAD_COLOR)
        # self.spaceship()
        self.randomboard()
        self.draw()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.key.key_code("p"):
                        self.start()
                    elif event.key == pygame.key.key_code("n"):
                        self.g.nextstate()
                        self.draw()
                pygame.display.update()
                # pygame.event.pump()
        pygame.quit()
        sys.exit()
    def draw(self):
        for element in self.g.alive_list:
            i,j = element
            pygame.draw.rect(self.screen,ALIVE_COLOR,(j*self.qsize,i*self.qsize,1*self.qsize,1*self.qsize))
        for element in self.g.dead_list:
            i,j = element
            pygame.draw.rect(self.screen,DEAD_COLOR,(j*self.qsize,i*self.qsize,1*self.qsize,1*self.qsize))
        pygame.display.update()
        fpsclock.tick(FPS)

if __name__ == "__main__":
    g = Game()
    gui = LifeGame()
    gui.run()
    # cProfile.run('gui.run()')

