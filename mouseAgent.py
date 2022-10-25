from matplotlib.pyplot import grid
import pygame
import random

from pygame.constants import VIDEOEXPOSE

from entity import Entity


class Mouse(Entity):

    def __init__(self, grid, grid_poid, pos):
        super(Mouse, self).__init__(grid, pos)
        self.direction = 0
        self.grid_poid = grid_poid
        self.tmpgrid_poid = self.grid_poid_cat()
        # print('chemin')
        # print(self.print_chemin(pos[0],pos[1]))

        for line in range(0, len(self.grid)):
            for column in range(0, len(self.grid[0])):
                if self.grid[line][column] == 'H':
                    self.hole = (line, column)

    def move(self, a, q):
        # Get the best direction to go to the player
        self.rotate(self.greedy2())
        # Move
        # if (turn_count % 2 == 1):
        self.move2()
        self.moved = True

    # bird's eye distance heuristic
    def h(self, x, y):

        return abs(x - self.hole[0]) + abs(y - self.hole[1])

    def grid_poid_cat(self):
        grid_copy = list(map(list, self.grid_poid))
        weight = -5
        for line in range(0, len(self.grid)):
            for column in range(0, len(self.grid[0])):
                if self.grid[line][column] == 'C':
                    grid_copy[line][column] = -10

                    if (self.canMove(line+1, column)):
                        grid_copy[line+1][column] += weight

                    if (self.canMove(line, column+1)):
                        grid_copy[line][column+1] += weight

                    if (self.canMove(line-1, column)):
                        grid_copy[line-1][column] += weight

                    if (self.canMove(line, column-1)):
                        grid_copy[line][column-1] += weight

        return grid_copy

    def print_chemin(self, posx, posy):
        chemin = []
        x, y = posx, posy
        maxpos = [x, y]
        iteration = len(self.grid)*len(self.grid)
        # print(iteration)

        while self.grid[x][y] != 'H' and iteration > 0:
            max = -10
            iteration -= 1
            # print(self.tmpgrid_poid)
            candidatForMax = []
            arrayMax = []

            maxpos = [x, y]

            if self.canMove(x+1, y):
                if max <= self.tmpgrid_poid[x+1][y]:
                    max = self.tmpgrid_poid[x+1][y]
                    maxpos = [x + 1, y]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x+1][y], [x + 1, y]))

            if self.canMove(x-1, y):
                if max <= self.tmpgrid_poid[x-1][y]:
                    max = self.tmpgrid_poid[x-1][y]
                    maxpos = [x - 1, y]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x-1][y], [x - 1, y]))

            if self.canMove(x, y+1):
                if max <= self.tmpgrid_poid[x][y+1]:
                    max = self.tmpgrid_poid[x][y+1]
                    maxpos = [x, y+1]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x][y+1], [x, y + 1]))

            if self.canMove(x, y-1):
                if max <= self.tmpgrid_poid[x][y-1]:
                    max = self.tmpgrid_poid[x][y-1]
                    maxpos = [x, y - 1]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x][y-1], [x, y - 1]))

            # x, y = maxpos
            for c in candidatForMax:
                if c[0] == max:
                    arrayMax.append(c[1])
            # print('============1')
            # print(candidatForMax)
            # print(arrayMax)
            # print('============2')

            x, y = random.choice(arrayMax)
            chemin.append([x, y])
        # print('=====CHEMIN=====')
        # print("iteration ", iteration)
        # print("Attention beaucoup d'embuche !!") if iteration <= 0 else print(
        #     "Le chemin est libre ")

        return chemin

    def chemin(self):
        chemin = []
        x, y = self.pos[0], self.pos[1]
        maxpos = [x, y]
        iteration = len(self.grid)*len(self.grid)
        # print(iteration)

        while self.grid[x][y] != 'H' and iteration > 0:
            max = -10
            iteration -= 1
            # print(self.tmpgrid_poid)
            candidatForMax = []
            arrayMax = []

            maxpos = [x, y]

            if self.canMove(x+1, y):
                if max <= self.tmpgrid_poid[x+1][y]:
                    max = self.tmpgrid_poid[x+1][y]
                    maxpos = [x + 1, y]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x+1][y], [x + 1, y]))

            if self.canMove(x-1, y):
                if max <= self.tmpgrid_poid[x-1][y]:
                    max = self.tmpgrid_poid[x-1][y]
                    maxpos = [x - 1, y]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x-1][y], [x - 1, y]))

            if self.canMove(x, y+1):
                if max <= self.tmpgrid_poid[x][y+1]:
                    max = self.tmpgrid_poid[x][y+1]
                    maxpos = [x, y+1]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x][y+1], [x, y + 1]))

            if self.canMove(x, y-1):
                if max <= self.tmpgrid_poid[x][y-1]:
                    max = self.tmpgrid_poid[x][y-1]
                    maxpos = [x, y - 1]
                    candidatForMax.append(
                        (self.tmpgrid_poid[x][y-1], [x, y - 1]))

            # x, y = maxpos
            for c in candidatForMax:
                if c[0] == max:
                    arrayMax.append(c[1])
            # print('============1')
            # print(candidatForMax)
            # print(arrayMax)
            # print('============2')

            x, y = random.choice(arrayMax)
            chemin.append([x, y])
        return chemin

    def greedy2(self):
        x = self.pos[0]
        y = self.pos[1]
        max = [-10, -10]
        maxpos = [x, y]
        self.tmpgrid_poid = self.grid_poid_cat()
        if self.canMove(x+1, y):
            # print("270")
            if max[1] < self.tmpgrid_poid[x+1][y]:
                max[0] = 270
                max[1] = self.tmpgrid_poid[x+1][y]
                maxpos = [x + 1, y]

        if self.canMove(x-1, y):
            # print("90")
            if max[1] < self.tmpgrid_poid[x-1][y]:
                max[0] = 90
                max[1] = self.tmpgrid_poid[x-1][y]
                maxpos = [x - 1, y]

        if self.canMove(x, y+1):
            # print("0")
            if max[1] < self.tmpgrid_poid[x][y+1]:
                max[0] = 0
                max[1] = self.tmpgrid_poid[x][y+1]
                maxpos = [x, y + 1]

        if self.canMove(x, y-1):
            # print("180")
            if max[1] < self.tmpgrid_poid[x][y-1]:
                max[0] = 180
                max[1] = self.tmpgrid_poid[x][y-1]
                maxpos = [x, y - 1]

        #astar(self.grid, self.pos, self.hole)
        # print("star")
        # print(self.print_chemin(self.pos[0],self.pos[1]))
        self.print_chemin(self.pos[0], self.pos[1])
        if max[1] > 0:
            direction = max[0]
        else:
            direction = 0 if self.canMove(x, y+1) else 180

        return direction

    # greedy algorithm
    def greedy(self):
        x = self.pos[0]
        y = self.pos[1]

        #astar(self.grid, self.pos, self.hole)
        # print("star")

        min = self.h(x, y)
        direction = 10
        if (self.canMove(x+1, y) and min > self.h(x+1, y)):
            direction = 270
        elif (self.canMove(x-1, y) and min > self.h(x-1, y)):
            direction = 90
        elif (self.canMove(x, y+1) and min > self.h(x, y+1)):
            direction = 0
        elif (self.canMove(x, y-1) and min > self.h(x, y-1)):
            direction = 180
        # dans le cas ou le chat peut pas bouger a cause d'un mur/obstacle
        # on donne une direction par defaut(à droite)
        else:
            print("\nCOINCé\n")
            direction = 0 if self.canMove(x, y+1) else 180
        return direction

    def move2(self):
        #print("last seen by cat" + str(Cat.last_seen) + " etat:" + str(Cat.state))

        if (self.direction == 0):  # Right
            x, y = 0, 1
        if (self.direction == 90):  # Up
            x, y = -1,  0
        if (self.direction == 180):  # Left
            x, y = 0, -1
        if (self.direction == 270):  # Down
            x, y = 1, 0
        if self.canMove(self.pos[0]+x, self.pos[1]+y) and (self.grid[self.pos[0]+x][self.pos[1]+y] != 'V') and (self.grid[self.pos[0]+x][self.pos[1]+y] != 'C'):
            super(Mouse, self).move(x, y)
        if (self.moved):
            if self.grid[self.pos[0]][self.pos[1]] != 'H':
                self.grid[self.pos[0]][self.pos[1]] = 'P'
            self.moved = False
            # print(self.hole[0])

    def rotate(self, angle):
        self.direction = angle
        if (self.direction >= 360):
            self.direction = self.direction % 360
