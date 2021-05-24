import sys
from scipy import signal
from numpy import ones,int8,array
import cProfile

class Game(object):
    def __init__(self):
        self.board = []
        self.board_size = 0
        self.board_sizey= 0
        self.alive_list = []
        self.dead_list = []
        self.kernel = array([[1, 1, 1],[1, 0, 1],[1, 1, 1]], dtype=int8)        #ones((3,3),dtype=int8) self.kernel[1,1] = 0

    def initalize(self,n,m): # n * m # Row, Column   
        self.board = []
        for i in range(n):
            self.board.append([])
            for j in range(m):
                self.board[i].append(0)
        self.board_size = n
        self.board_sizey = m

    def add_alive_dead(self):               # DEAD = 0 , ALIVE = 1
        for i in range(self.board_size):
            for j in range(self.board_sizey):
                if self.board[i][j] == 1:
                    self.alive_list.append([i,j])
                
    def __str__(self):
        for i in range(len(self.board)):
            print(self.board[i])
        return ""

    def nextstate(self):
        change = []
        neighbors = signal.convolve(self.board,self.kernel,mode='same')
        for i in range(self.board_size):
            for j in range(self.board_sizey):
                if self.board[i][j] == 1:
                    if neighbors[i][j] < 2 or neighbors[i][j] > 3:
                        change.append([i,j,0])
                        self.alive_list.remove([i,j])
                        self.dead_list.append([i,j])
                    else:
                        continue
                else:
                    if neighbors[i][j] == 3:
                        change.append([i,j,1])
                        self.alive_list.append([i,j])
                        if [i,j] in self.dead_list:
                            self.dead_list.remove([i,j])
                    else:
                        continue
        for element in change:
            i,j,action = element
            self.board[i][j] = action
        return self.board
    def overwrite_certain_pos(self,i,j,input):
        self.board[i][j] = input
        self.alive_list.append([i,j])

    def continuous(self,iterations = float('inf')):
        current = self.board
        # print(g)
        n = 0
        g.nextstate()
        # print(g)
        while n < iterations:
            g.nextstate()
            # print(g)
            n+=1

if __name__ == "__main__":
    g = Game()
    def run():
        g.initalize(400,400)
        g.overwrite_certain_pos(6,5,1)
        g.overwrite_certain_pos(6,6,1)
        g.overwrite_certain_pos(6,7,1)
        g.overwrite_certain_pos(7,7,1)
        g.overwrite_certain_pos(7,6,1)
        g.continuous(40)
    # run()
    cProfile.run('run()',sort="tottime")