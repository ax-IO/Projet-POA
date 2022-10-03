
import pygame
import random

from pygame.constants import VIDEOEXPOSE

from entity import Entity

def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""

    # Create start and end node

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start)

    # Loop until you find the end
    while len(open_list) > 0:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item[0]+item[1] < current_node[0]+current_node[1]:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node[0] + new_position[0], current_node[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != 0:
                continue

            # Create new node

            # Append
            children.append(node_position)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node :
                    continue

            # Add the child to the open list
            open_list.append(child)


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
        print(self.pos)
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

        astar(self.grid, self.pos, self.hole)
        print("star")

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
        if self.canMove(self.pos[0]+x,self.pos[1]+y) and (self.grid[self.pos[0]+x][self.pos[1]+y] != 'V') and (self.grid[self.pos[0]+x][self.pos[1]+y] != 'C'):
            super(Mouse, self).move(x, y)
        if(self.moved):
            if self.grid[self.pos[0]][self.pos[1]] != 'H' :
                self.grid[self.pos[0]][self.pos[1]] = 'P'
            self.moved = False
            print(self.hole[0])
            


    def rotate(self, angle):
        self.direction = angle
        if (self.direction >= 360):
            self.direction = self.direction % 360


  
    