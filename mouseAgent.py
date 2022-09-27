
import pygame
import random

from pygame.constants import VIDEOEXPOSE

from entity import Entity



class Mouse(Entity):


    def __init__(self, grid, pos):
        super(Mouse, self).__init__(grid, pos)
        self.direction = 0
        for line in range(0,len(self.grid)):
            for column in range(0,len(self.grid[0])):
                if self.grid[line][column] == 'H':
                    self.hole = (line, column) 
        
    # def souffle(self):
    #     effect = pygame.mixer.Sound('sound/chatpascontent.wav')
    #     effect.play()

    def move(self, a, q):
        # Get the best direction to go to the player
        self.rotate(self.greedy())
        # Move
        #if (turn_count % 2 == 1):
        self.move2()
        self.moved=True 

    # bird's eye distance heuristic
    def h(self, x, y): 
        return abs(x - self.hole[0]) + abs(y - self.hole[1])


    # greedy algorithm
    def greedy(self):
        x = self.pos[0]
        y = self.pos[1]
        min = self.h(x,y)
        direction = 10
        if(self.canMove(x+1, y) and  min > self.h(x+1, y)): direction = 270
        elif(self.canMove(x-1, y) and  min > self.h(x-1, y)): direction = 90
        elif(self.canMove(x,y+1) and  min > self.h(x, y+1)): direction = 0
        elif(self.canMove(x,y-1) and  min > self.h(x, y-1)): direction = 180
        #dans le cas ou le chat peut pas bouger a cause d'un mur/obstacle 
        #on donne une direction par defaut(à droite)
        else:
            print("\nCOINCé\n")
            direction = 0 if self.canMove(x,y+1) else 180
        return direction

    

    def move2(self):
        #print("last seen by cat" + str(Cat.last_seen) + " etat:" + str(Cat.state))
        
        if (self.direction == 0): # Right
            x, y = 0, 1
        if (self.direction == 90): # Up
            x, y = -1,  0
        if (self.direction == 180): # Left
            x, y = 0, -1
        if (self.direction == 270): # Down
            x, y = 1, 0
        if self.canMove(self.pos[0]+x,self.pos[1]+y) and (self.grid[self.pos[0]+x][self.pos[1]+y] != 'V'):
            super(Mouse, self).move(x, y)
        if(self.moved):
            self.grid[self.pos[0]][self.pos[1]] = 'P'
            self.moved = False
            


    def rotate(self, angle):
        self.direction = angle
        if (self.direction >= 360):
            self.direction = self.direction % 360


  
    