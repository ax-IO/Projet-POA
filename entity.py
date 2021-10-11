class Entity():
    def __init__(self, grid, pos = (2, 7)):
        self.grid = grid
        self.initpos = self.pos = pos
        self.moved = False
    def move(self, x, y):
        posX = self.pos[0] + x
        posY = self.pos[1] + y

        if (posX>=0 and posX<len(self.grid[0]) and posY>=0 and posY<len(self.grid[0])):
            if (self.grid[posX][posY] != 'W') :
                self.grid[self.pos[0]][self.pos[1]] = 0
                self.pos = (posX, posY)
                self.moved = True