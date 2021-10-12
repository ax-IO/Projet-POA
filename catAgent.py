
import pygame
import random

from entity import Entity


class Cat(Entity):
    def __init__(self, grid, pos=(2, 7)):
        super(Cat, self).__init__(grid, pos)
        self.direction = 0
        self.portee_vision = 2
        self.vision = [[0] * len(self.grid[0])
                       for i in range((len(self.grid)))]  # Init 2D Array to 0

    def souffle(self):
        effect = pygame.mixer.Sound('sound/chatpascontent.wav')
        effect.play()

    def choix_action(self, turn_count):
        if (turn_count % 2 == 1):
            self.move()
        if (turn_count % 2 == 0):
            self.rotate(random.randint(0, 3)*90)

    def move(self):
        if (self.direction == 0):
            x, y = 0, 1
        if (self.direction == 90):
            x, y = -1,  0
        if (self.direction == 180):
            x, y = 0, 1
        if (self.direction == 270):
            x, y = 1, 0
        if (self.pos[0]+x >= 0 and self.pos[0]+x < len(self.grid[0]) and self.pos[1]+y >= 0 and self.pos[1]+y < len(self.grid[0])):
            if (self.grid[self.pos[0] + x][self.pos[1] + y] != 'W'):
                # print(grid[self.pos[0]][self.pos[1]])
                self.grid[self.pos[0]][self.pos[1]] = 0
                self.grid[self.pos[0]+x][self.pos[1]+y] = 'C'
                self.pos = (self.pos[0] + x, self.pos[1] + y)

    def rotate(self, angle):
        self.direction += angle
        if (self.direction >= 360):
            self.direction = self.direction % 360
        self.update_cone_vision()

    def update_cone_vision(self):
        # Nettoie cases entourant le chat
        for j in range(-self.portee_vision, self.portee_vision+1):
            for i in range(-self.portee_vision, self.portee_vision+1):
                if (self.pos[0]+j >= 0 and self.pos[0]+j < len(self.grid[0]) and self.pos[1]+i >= 0 and self.pos[1]+i < len(self.grid[0])):
                    if (self.vision[self.pos[0]+j][self.pos[1]+i] == 'V'):
                        self.vision[self.pos[0]+j][self.pos[1]+i] = 0

        # Crée les cases de visions
        # if (self.direction  == 90):
        #     grid[self.pos[0]][self.pos[1] +1] = 'V'

        if (self.direction == 0):
            for dist in range(1, self.portee_vision+1):
                for largeur in range(-dist + 1, dist):
                    if (self.pos[0]+largeur >= 0 and self.pos[0]+largeur < len(self.grid[0]) and self.pos[1]+dist >= 0 and self.pos[1] + dist < len(self.grid[0])):
                        self.vision[self.pos[0] +
                                    largeur][self.pos[1] + dist] = 'V'

        if (self.direction == 90):
            for dist in range(-self.portee_vision, 0):
                for largeur in range(dist + 1, -dist):
                    # print("dist=", dist, "largeur=", largeur)
                    if (self.pos[0]+dist >= 0 and self.pos[0]+dist < len(self.grid[0]) and self.pos[1]+largeur >= 0 and self.pos[1] + largeur < len(self.grid[0])):
                        self.vision[self.pos[0] +
                                    dist][self.pos[1] + largeur] = 'V'

        if (self.direction == 180):
            for dist in range(-self.portee_vision, 0):
                for largeur in range(dist + 1, -dist):
                    # print("dist=", dist, "largeur=", largeur)
                    if (self.pos[0]+largeur >= 0 and self.pos[0]+largeur < len(self.grid[0]) and self.pos[1]+dist >= 0 and self.pos[1] + dist < len(self.grid[0])):
                        self.vision[self.pos[0] +
                                    largeur][self.pos[1] + dist] = 'V'

        if (self.direction == 270):
            for dist in range(1, self.portee_vision+1):
                for largeur in range(-dist + 1, dist):
                    if (self.pos[0]+dist >= 0 and self.pos[0]+dist < len(self.grid[0]) and self.pos[1]+largeur >= 0 and self.pos[1] + largeur < len(self.grid[0])):
                        self.vision[self.pos[0] +
                                    dist][self.pos[1] + largeur] = 'V'
    # [-dist+1 ; dist]
