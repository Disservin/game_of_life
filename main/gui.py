from game_of_life import *
import sys
import pygame
import cProfile
from random import *
from pygame.locals import *

BOARD_SIZE = WIDTH, HEIGHT = 1280,720  # WIDTH = size * qsize , HEIGHT = size *qsize  1280,720          600,600
DEAD_COLOR = 0,0,0
ALIVE_COLOR = 255,255,255
FPS = 24
fpsclock = pygame.time.Clock()

class LifeGame:
    def __init__(self) -> None:
        self.g = Game()
        self.qsize = 20
        self.sizex,self.sizey = WIDTH//self.qsize,HEIGHT//self.qsize  
        self.g.initalize(self.sizey,self.sizex)
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        self.screen = pygame.display.set_mode(BOARD_SIZE)
        pygame.init()
    def restart(self):
        return self.g.initalize(self.sizey,self.sizex)
    def randomboard(self):              
        for i in range(self.sizey//4,self.sizey-self.sizey//4):
            for j in range(self.sizex//4,self.sizex-self.sizex//4):
                if randint(0,1) == 1:
                    self.g.overwrite_certain_pos(i,j,1)      
    def start(self,empty_hash,iterations = float('inf')):
        current = self.g.board
        current_hash = hash(str(self.g.board))
        self.draw2()
        n = 0
        self.g.nextstate()
        new_hash = hash(str(self.g.board))
        self.draw2()
        while n < iterations:
            current_hash = new_hash
            self.g.nextstate()
            new_hash = hash(str(self.g.board))
            self.draw2()
            n+=1
            if empty_hash == new_hash:
                return
            elif current_hash == new_hash:
                return
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    elif event.key == pygame.key.key_code("p"):
                        return 
    def emptyhash(self):
        self.restart()
        str_list = str(self.g.board)
        hash_list = hash(str_list)
        return hash_list
    def run(self):
        self.screen.fill(DEAD_COLOR)
        # self.randomboard()
        my_hash = self.emptyhash()
        self.draw_grid()
        self.draw2()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.key.key_code("p"):
                        self.start(my_hash)
                    elif event.key == pygame.key.key_code("n"):
                        self.g.nextstate()
                        self.draw2()
                    elif event.key == pygame.key.key_code("r"):
                        self.restart()
                        self.g.alive_list = []
                        self.g.dead_list = []
                        self.draw_black()
                        print("reset")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    location = pygame.mouse.get_pos()
                    col = location[0]//self.qsize
                    row = location[1]//self.qsize
                    deleted = False
                    added = False
                    if self.g.board[row][col] == 1:
                        self.g.alive_list.remove([row,col])
                        self.g.dead_list.append([row,col])
                        self.g.overwrite_certain_pos(row,col,0)
                        deleted = True
                    else:
                        self.g.overwrite_certain_pos(row,col,1)
                        if [row,col] in self.g.dead_list:
                            self.g.dead_list.remove([row,col])
                        added = True
                    self.draw2()
                pygame.display.update()
                # pygame.event.pump()
        pygame.quit()
        sys.exit()
    def draw(self):             # BLACK BACKGROUND
        for element in self.g.alive_list:
            i,j = element
            pygame.draw.rect(self.screen,ALIVE_COLOR,(j*self.qsize,i*self.qsize,1*self.qsize,1*self.qsize))
        for element in self.g.dead_list:
            i,j = element
            pygame.draw.rect(self.screen,DEAD_COLOR,(j*self.qsize,i*self.qsize,1*self.qsize,1*self.qsize))
        pygame.display.update()
        fpsclock.tick(FPS)
    def draw_grid(self):
        x,y= 0,0
        w = 1
        for row in range(0,WIDTH,self.qsize):
            for col in range(0,HEIGHT,self.qsize):
                pygame.draw.rect(self.screen,(128,128,128),(row,col,self.qsize,self.qsize),1)
        pygame.display.update()
        fpsclock.tick(FPS)
    def draw2(self):
        for element in self.g.alive_list:
            i,j = element
            pygame.draw.rect(self.screen,ALIVE_COLOR,(j*self.qsize+1,i*self.qsize+1,self.qsize-2,self.qsize-2))
        for element in self.g.dead_list:
            i,j = element
            pygame.draw.rect(self.screen,DEAD_COLOR,(j*self.qsize+1,i*self.qsize+1,self.qsize-2,self.qsize-2))
        pygame.display.update()
        fpsclock.tick(FPS)
    def draw_black(self):
        self.screen.fill(DEAD_COLOR)
        self.draw_grid()
if __name__ == "__main__":
    g = Game()
    gui = LifeGame()
    gui.run()
    # cProfile.run('gui.run()')

