
import pygame
import random

from pygame.constants import VIDEOEXPOSE

from entity import Entity


class Cat(Entity):

    state = 0  # Patrolling
    last_seen = False

    def __init__(self, grid, player, pos):
        super(Cat, self).__init__(grid, pos)
        self.player = player
        self.direction = 0
        self.portee_vision = 2
        self.vision = [[0] * len(self.grid[0])
                       for i in range((len(self.grid)))]  # Init 2D Array to 0
        # Cat.state = 0 # Patrolling
        self.positionCentre = (0, 0)
        self.devantGauche = (0, 0)
        self.devantDroite = (0, 0)

    def set_screen(self, window_size, height, width, margin):
        self.window_size = window_size
        self.height = height
        self.width = width
        self.margin = margin

    def souffle(self):
        effect = pygame.mixer.Sound('sound/chatpascontent.wav')
        effect.play()



    def cout_move(self,dir,pos):
        cost = 0
        if dir == 0 :
            if (pos[0]+1)<len(self.grid[0]) :
                if self.grid[pos[0]+1][pos[1]] != 'W' :    
                    if self.grid[pos[0] + 1][pos[1]] == '0' :
                        cost+=1
                    if (pos[0]+2)<len(self.grid[0]) :
                        if self.grid[pos[0] + 2][pos[1]] == '0' :
                            cost+=1
                        if (pos[1]-1)>len(self.grid) :
                            if self.grid[pos[0] + 2][pos[1]-1] == '0' :
                                cost+=1
                        if (pos[1]+1)<len(self.grid) :
                            if self.grid[pos[0] + 2][pos[1]+1] != 'V' :
                                cost+=1
        
        if dir == 90 :
            if (pos[1]+1)<len(self.grid) :
                if self.grid[pos[0]][pos[1]+1] != 'W' :
                    if self.grid[pos[0]][pos[1]+1] != 'V' :
                        cost+=1
                    if (pos[1]+2)<len(self.grid) :
                        if self.grid[pos[0]][pos[1]+2] != 'V' :
                            cost+=1
                        if (pos[0]-1)>len(self.grid[0]) :
                            if self.grid[pos[0]-1][pos[1]+2] != 'V' :
                                cost+=1
                        if (pos[0]+1)<len(self.grid[0]) :
                            if self.grid[pos[0]+1][pos[1]+2] != 'V' :
                                cost+=1

        if dir == 180 :
            if (pos[0]-1)>len(self.grid[0]) :
                if self.grid[pos[0]-1][pos[1]] != 'W' :
                    if self.grid[self.pos[0] - 1][pos[1]] != 'V' :
                        cost+=1
                    if (pos[0]-2)>len(self.grid[0]) :
                        if self.grid[pos[0] - 2][pos[1]] != 'V' :
                            cost+=1
                        if (pos[1]-1)>len(self.grid) :
                            if self.grid[pos[0] - 2][pos[1]-1] != 'V' :
                                cost+=1
                        if (pos[1]+1)<len(self.grid) :
                            if self.grid[pos[0] - 2][pos[1]+1] != 'V' :
                                cost+=1

        if dir == 270 :
            if (pos[1]-1)>len(self.grid) :
                if self.grid[pos[0]][pos[1]-1] != 'W' :
                    if self.grid[pos[0]][pos[1]-1] != 'V' :
                        cost+=1
                    if (pos[1]-2)>len(self.grid) :
                        if self.grid[pos[0]][pos[1]-2] != 'V' :
                            cost+=1
                        if (pos[0]-1)>len(self.grid[0]) :
                            if self.grid[pos[0]-1][pos[1]-2] != 'V' :
                                cost+=1
                        if (pos[0]+1)<len(self.grid[0]) :
                            if self.grid[pos[0]+1][pos[1]-2] != 'V' :
                                cost+=1

        return cost
  


    def patrol(self, turn_count):
        # Rotate to new direction
        if (turn_count % 2 == 0):
            # dir = random.randint(0, 3)*90
            # if(self.pos[1] == len(self.grid)-1): # If cat on right side, go left
            #     dir = 180
            # elif(self.pos[1] == 0): # If cat on left side, go right
            #     dir = 0
            # if(self.pos[0] == len(self.grid[0])-1): # If cat on bottom side, go up
            #     dir = 90
            # if(self.pos[0] == 0): # If cat on top side, go down
            #     dir = 270if (self.direction == 0): # Right
            
            directions = (0, 90, 180, 270)
            max = 0
            dir = self.direction
            cost_dir = []

            for d in directions :
                if d != self.direction :
                    cost_dir.append((d,self.cout_move(d,self.pos)))
                else :
                    if d == 0 :
                        if(self.pos[0]+1)<len(self.grid[0]) :
                            if max < self.cout_move(d,(self.pos[0]+1,self.pos[1])) :
                                max = self.cout_move(d,(self.pos[0]+1,self.pos[1]))
                                dir = d
                    
                    if d == 90 :
                        if(self.pos[1]-1)>len(self.grid) :
                            if max < self.cout_move(d,(self.pos[0],self.pos[1]-1)) :
                                max = self.cout_move(d,(self.pos[0],self.pos[1]-1))
                                dir = d

                    if d == 180 :
                        if(self.pos[0]-1)>len(self.grid[0]) :
                            if max < self.cout_move(d,(self.pos[0]-1,self.pos[1])) :
                                max = self.cout_move(d,(self.pos[0]-1,self.pos[1]))
                                dir = d

                    if d == 270 :
                        if(self.pos[1]+1)<len(self.grid) :
                            if max < self.cout_move(d,(self.pos[0],self.pos[1]+1)) :
                                max = self.cout_move(d,(self.pos[0],self.pos[1]+1))
                                dir = d
            
            for d,c in cost_dir :
                if max<c :
                    max = c

            potential_dir = []
            for d,c in cost_dir :
                if max == c :
                    potential_dir.append(d)
            if len(potential_dir)>0 :
                dir = potential_dir[random.randint(0,len(potential_dir)-1)]
            else :
                dir = random.randint(0,3)*90


            self.rotate(dir)
        # Move
        if (turn_count % 2 == 1):
            self.move()

    # bird's eye distance heuristic
    def h(self, x, y):
        return abs(x - Cat.last_seen[0]) + abs(y - Cat.last_seen[1])

    # greedy algorithm
    def greedy(self):
        x = self.pos[0]
        y = self.pos[1]
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

    def chase(self, turn_count):
        # Get the best direction to go to the player
        self.rotate(self.greedy())
        # Move
        # if (turn_count % 2 == 1):
        self.move()

    def choix_action(self, turn_count):
        if (Cat.state == 0):  # Patrolling
            self.patrol(turn_count)
        elif (Cat.state == 1):  # Chasing player
            self.chase(turn_count)

    def move(self):
        # print("last seen by cat" + str(Cat.last_seen) + " etat:" + str(Cat.state))
        if (self.direction == 0):  # Right
            x, y = 0, 1
        if (self.direction == 90):  # Up
            x, y = -1,  0
        if (self.direction == 180):  # Left
            x, y = 0, -1
        if (self.direction == 270):  # Down
            x, y = 1, 0
        trou = self.pos if (self.grid[self.pos[0]]
                            [self.pos[1]] in ('O', 'H')) else False
        if self.canMove(self.pos[0]+x, self.pos[1]+y) and (self.grid[self.pos[0]+x][self.pos[1]+y] not in ('C', 'O')):
            super(Cat, self).move(x, y)
        if (self.moved):
            if self.pos == Cat.last_seen:
                Cat.last_seen = False
                Cat.state = 0
            if trou is not False:
                self.grid[trou[0]][trou[1]] = 'H'
            if self.grid[self.pos[0]][self.pos[1]] == 'H':
                self.grid[self.pos[0]][self.pos[1]] = 'O'
            else:
                self.grid[self.pos[0]][self.pos[1]] = 'C'
            self.update_cone_vision()
            self.moved = False

    def rotate(self, angle):
        self.direction = angle
        if (self.direction >= 360):
            self.direction = self.direction % 360
        self.update_cone_vision()

    def clear_vision_cases(self):
        # Nettoie cases entourant le chat
        for j in range(-self.portee_vision, self.portee_vision+1):
            for i in range(-self.portee_vision, self.portee_vision+1):
                if (self.pos[0]+j >= 0 and self.pos[0]+j < len(self.grid[0]) and self.pos[1]+i >= 0 and self.pos[1]+i < len(self.grid[0])):
                    if (self.vision[self.pos[0]+j][self.pos[1]+i] == 'V'):
                        self.vision[self.pos[0]+j][self.pos[1]+i] = 0

    def build_cone_vision(self, dist):
        x, y = self.pos[0], self.pos[1]

        self.positionCentre = (y * (self.width + self.margin) + 0.5 * (self.width + self.margin),
                               x * (self.height + self.margin) + 0.5 * (self.height + self.margin))

        if (self.direction == 0):  # Right
            if (y < len(self.grid[0]) - 1):
                if (self.grid[x][y+1] == 'W'):
                    self.devantGauche = (self.positionCentre[0] + 0.5*self.width + 1*self.margin,
                                         self.positionCentre[1] - 0.5*self.height - 1*self.margin)
                    self.devantDroite = (self.positionCentre[0] + 0.5*self.width + 1*self.margin,
                                         self.positionCentre[1] + 0.5*self.height + 1*self.margin)
                else:
                    self.devantGauche = (self.positionCentre[0] + 2.5*self.width + 2*self.margin,
                                         self.positionCentre[1] - 1.5*self.height - 1*self.margin)
                    self.devantDroite = (self.positionCentre[0] + 2.5*self.width + 2*self.margin,
                                         self.positionCentre[1] + 1.5*self.height + 1*self.margin)
            else:
                self.devantGauche = (self.positionCentre[0] + 2.5*self.width + 2*self.margin,
                                     self.positionCentre[1] - 1.5*self.height - 1*self.margin)
                self.devantDroite = (self.positionCentre[0] + 2.5*self.width + 2*self.margin,
                                     self.positionCentre[1] + 1.5*self.height + 1*self.margin)
        if (self.direction == 90):  # Up
            if (x > 0):
                if (self.grid[x-1][y] == 'W'):
                    self.devantGauche = (self.positionCentre[0] + 0.5*self.width + 1*self.margin,
                                         self.positionCentre[1] - 0.5*self.height - 1*self.margin)
                    self.devantDroite = (self.positionCentre[0] - 0.5*self.width - 1*self.margin,
                                         self.positionCentre[1] - 0.5*self.height - 1*self.margin)
                else:
                    self.devantGauche = (self.positionCentre[0] + 1.5*self.width + 1*self.margin,
                                         self.positionCentre[1] - 2.5*self.height - 2*self.margin)
                    self.devantDroite = (self.positionCentre[0] - 1.5*self.width - 1*self.margin,
                                         self.positionCentre[1] - 2.5*self.height - 2*self.margin)
            else:
                self.devantGauche = (self.positionCentre[0] + 1.5*self.width + 1*self.margin,
                                     self.positionCentre[1] - 2.5*self.height - 2*self.margin)
                self.devantDroite = (self.positionCentre[0] - 1.5*self.width - 1*self.margin,
                                     self.positionCentre[1] - 2.5*self.height - 2*self.margin)
        if (self.direction == 180):  # Left
            if (y > 0):
                if (self.grid[x][y-1] == 'W'):
                    self.devantGauche = (self.positionCentre[0] - 0.5*self.width - 1*self.margin,
                                         self.positionCentre[1] - 0.5*self.height - 1*self.margin)
                    self.devantDroite = (self.positionCentre[0] - 0.5*self.width - 1*self.margin,
                                         self.positionCentre[1] + 0.5*self.height + 1*self.margin)
                else:
                    self.devantGauche = (self.positionCentre[0] - 2.5*self.width - 2*self.margin,
                                         self.positionCentre[1] - 1.5*self.height - 1*self.margin)
                    self.devantDroite = (self.positionCentre[0] - 2.5*self.width - 2*self.margin,
                                         self.positionCentre[1] + 1.5*self.height + 1*self.margin)
            else:
                self.devantGauche = (self.positionCentre[0] - 2.5*self.width - 2*self.margin,
                                     self.positionCentre[1] - 1.5*self.height - 1*self.margin)
                self.devantDroite = (self.positionCentre[0] - 2.5*self.width - 2*self.margin,
                                     self.positionCentre[1] + 1.5*self.height + 1*self.margin)
        if (self.direction == 270):  # Down
            if (x < len(self.grid[0]) - 1):
                if (self.grid[x+1][y] == 'W'):
                    self.devantGauche = (self.positionCentre[0] + 0.5*self.width + 1*self.margin,
                                         self.positionCentre[1] + 0.5*self.height + 1*self.margin)
                    self.devantDroite = (self.positionCentre[0] - 0.5*self.width - 1*self.margin,
                                         self.positionCentre[1] + 0.5*self.height + 1*self.margin)
                else:
                    self.devantGauche = (self.positionCentre[0] + 1.5*self.width + 1*self.margin,
                                         self.positionCentre[1] + 2.5*self.height + 2*self.margin)
                    self.devantDroite = (self.positionCentre[0] - 1.5*self.width - 1*self.margin,
                                         self.positionCentre[1] + 2.5*self.height + 2*self.margin)
            else:
                self.devantGauche = (self.positionCentre[0] + 1.5*self.width + 1*self.margin,
                                     self.positionCentre[1] + 2.5*self.height + 2*self.margin)
                self.devantDroite = (self.positionCentre[0] - 1.5*self.width - 1*self.margin,
                                     self.positionCentre[1] + 2.5*self.height + 2*self.margin)

        Vx = Vy = 0
        Cat.state = 1 if Cat.last_seen else 0
        hidden = False  # Si on croise un mur, sortir de la boucle
        for d in dist:
            # Determine width according to vision distance
            if (self.direction == 0 or self.direction == 270):
                if (hidden):
                    break
                # minWidth = -d
                # maxWidth = d +1
                minWidth = -d + 1
                maxWidth = d
            elif (self.direction == 90 or self.direction == 180):
                if (hidden):
                    break
                # minWidth = d
                # maxWidth = -d +1
                minWidth = d + 1
                maxWidth = -d

            for w in range(minWidth, maxWidth):
                # Manage sides vision cones
                if ((self.direction == 0 or self.direction == 180)
                        and self.pos[0]+w >= 0 and self.pos[0]+w < len(self.grid[0]) and self.pos[1]+d >= 0 and self.pos[1] + d < len(self.grid[0])):
                    Vx = self.pos[0] + w
                    Vy = self.pos[1] + d
                    if (self.grid[Vx][Vy] == 'W'):
                        hidden = True
                        continue
                    self.vision[Vx][Vy] = 'V'
                    if (self.grid[Vx][Vy] == 'P'):  # If player is spotted while patrolling
                        if Cat.last_seen == False:
                            effect = pygame.mixer.Sound('sound/spotted.wav')
                            effect.play()
                        Cat.last_seen = (Vx, Vy)
                        Cat.state = 1  # Chase him

                elif ((self.direction == 90 or self.direction == 270)
                      and self.pos[0]+d >= 0 and self.pos[0]+d < len(self.grid[0]) and self.pos[1]+w >= 0 and self.pos[1] + w < len(self.grid[0])):
                    Vx = self.pos[0] + d
                    Vy = self.pos[1] + w
                    if (self.grid[Vx][Vy] == 'W'):
                        hidden = True
                        continue
                    self.vision[Vx][Vy] = 'V'
                    # If player is spotted while patrolling
                    if (Cat.state == 0 and self.grid[Vx][Vy] == 'P'):
                        Cat.state = 1  # Chase him
                        Cat.last_seen = (Vx, Vy)

    def update_cone_vision(self):
        self.clear_vision_cases()

        if (self.direction == 0):
            self.build_cone_vision(range(1, self.portee_vision+1))

        elif (self.direction == 90):
            self.build_cone_vision(range(-1, -(self.portee_vision+1), -1))

        elif (self.direction == 180):
            self.build_cone_vision(range(-1, -(self.portee_vision+1), -1))

        elif (self.direction == 270):
            self.build_cone_vision(range(1, self.portee_vision+1))
