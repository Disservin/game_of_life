from copy import deepcopy
import sys
import os

#game of life
class Game(object):
    def __init__(self):
        self.board = []
        self.board_size = 0
        self.board_sizey= 0
        self.alive_list = []
        self.dead_list = []

    def initalize(self,n,m): # n * m # Row, Column   
        self.board = []
        for i in range(n):
            self.board.append([])
            for j in range(m):
                self.board[i].append("#")
        self.board_size = n
        self.board_sizey = m

    def add_alive_dead(self):
        for i in range(self.board_size):
            for j in range(self.board_sizey):
                if self.board[i][j] == "A":
                    self.alive_list.append([i,j])
                
    def __str__(self):
        for i in range(len(self.board)):
            print(self.board[i])
        return ""
    def checkneighbours(self,i,j):  #DEAD = D ALIVE = A
        cut = []
        size = self.board_size
        sizey = self.board_sizey
        status = self.board[i][j]
        a = 0
        d = 0
        if i-1 >=0:
            for n in range(3):
                if j-1+n >=0 and j-1+n < sizey:
                    cut.append(self.board[i-1][j-1+n])
                else:
                    continue
        if j-1 >=0:
            cut.append(self.board[i][j-1])
        if j+1 < sizey:
            cut.append(self.board[i][j+1])
        if i+1 < size:
            for n in range(3):
                if j-1+n >=0 and j-1+n < sizey:
                    cut.append(self.board[i+1][j-1+n])
                else:
                    continue
        for l in cut:
            if l == "A":
                a += 1
            else:
                d += 1
        if status == "A":
            if a < 2:
                return "dies"
            elif a == 3 or a == 2:
                return "alive"
            elif a > 3:
                return "dies"
        else:
            if a == 3:
                return "reincarnates"

    def nextstate(self):
        copy = deepcopy(self.board)
        change = []
        for i in range(self.board_size):
            for j in range(self.board_sizey):
                if self.checkneighbours(i,j) == "dies":
                    change.append([i,j,"#"])
                    self.alive_list.remove([i,j])
                    self.dead_list.append([i,j])
                elif self.checkneighbours(i,j) == "reincarnates":
                    change.append([i,j,"A"])
                    self.alive_list.append([i,j])
                    if [i,j] in self.dead_list:
                        self.dead_list.remove([i,j])
                else:
                    continue
        for element in change:
            i,j,action = element
            copy[i][j] = action
        return copy
    def overwrite_certain_pos(self,i,j,input):
        self.board[i][j] = input
        self.alive_list.append([i,j])

    def continuous(self,iterations = float('inf')):
        current = self.board
        print(g)
        n = 0
        next = g.nextstate()
        self.board = next
        print(g)
        while n < iterations:
            if current == next:
                break
            else:
                current = next
                next = g.nextstate()
                self.board = next
                print(g)
                n+=1


if __name__ == "__main__":
    g = Game()
    g.initalize(12,12)
    g.overwrite_certain_pos(6,5,"A")
    g.overwrite_certain_pos(6,6,"A")
    g.overwrite_certain_pos(6,7,"A")
    g.overwrite_certain_pos(7,6,"A")
    g.continuous(10)
