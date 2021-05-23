from game_of_life import *
import sys
import pygame
import cProfile
from random import *
import time
from pygame.locals import *

BOARD_SIZE = WIDTH, HEIGHT = 1280,720    # WIDTH = size * qsize , HEIGHT = size *qsize
DEAD_COLOR = 0,0,0
ALIVE_COLOR = 255,255,255

class LifeGame:
    def __init__(self) -> None:
        self.g = Game()
        self.qsize = 20
        self.sizex,self.sizey = WIDTH//self.qsize,HEIGHT//self.qsize  
        self.g.initalize(self.sizey,self.sizex)
        
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        pygame.init()
    def figure(self):
        self.g.overwrite_certain_pos(6,5,"A")
        self.g.overwrite_certain_pos(6,6,"A")
        self.g.overwrite_certain_pos(6,7,"A")
        self.g.overwrite_certain_pos(7,6,"A")
    def randomboard(self):              #X/4 Y/4
        l = ["A","D"]
        for i in range(self.sizey//4,self.sizey-self.sizey//4):
            for j in range(self.sizex//4,self.sizex-self.sizex//4):
                if randint(0,5) == 0:
                    self.g.overwrite_certain_pos(i,j,"A")
    def spaceship(self):
        self.g.overwrite_certain_pos(1,3,"A")
        self.g.overwrite_certain_pos(2,3,"A")
        self.g.overwrite_certain_pos(3,3,"A")
        self.g.overwrite_certain_pos(3,2,"A")
        self.g.overwrite_certain_pos(2,1,"A")        
    def start(self,iterations = float('inf')):
        fps = 1/30
        current = self.g.board
        self.draw()
        time.sleep(fps)
        n = 0
        next = self.g.nextstate()
        self.g.board = next 
        self.draw()
        time.sleep(fps)
        while n < iterations:
            if current == next:
                break
            else:
                current = next
                next = self.g.nextstate()
                self.g.board = next
                self.draw()
                time.sleep(fps)
                n+=1
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
    def run(self):
        self.screen.fill(DEAD_COLOR)
        # self.spaceship()
        self.randomboard()
        self.start()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                pygame.display.update()
                pygame.event.pump()
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

if __name__ == "__main__":
    g = Game()
    gui = LifeGame()
    gui.run()
    # cProfile.run('gui.run()')

