from entity import Entity

class Player(Entity):
    def __init__(self, grid, pos = (8, 5)):
        super(Player, self).__init__(grid, pos)
        self.moved = False
    def move (self, x, y):
        if(self.grid[self.pos[0]][self.pos[1]] == 'T'):
            self.grid[self.pos[0]][self.pos[1]] = 'V'
        else:
            self.grid[self.pos[0]][self.pos[1]] = 0

        posX = self.pos[0] + x
        posY = self.pos[1] + y

        if (posX>=0 and posX<len(self.grid[0]) and posY>=0 and posY<len(self.grid[0])):
            if (self.grid[posX][posY] != 'W') :
                self.pos = (posX, posY)
                self.moved = True
        if(self.grid[self.pos[0]][self.pos[1]] == 'V'):
            self.grid[self.pos[0]][self.pos[1]] = 'T'
        elif(self.grid[self.pos[0]][self.pos[1]] != 'H'):
            self.grid[self.pos[0]][self.pos[1]] = 'P'