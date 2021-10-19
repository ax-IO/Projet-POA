class Entity():
    def __init__(self, grid, pos=(2, 7)):
        self.grid = grid
        self.initpos = self.pos = pos
        self.moved = False

    def canMove(self, x, y):
        return x >= 0 and x < len(self.grid[0]) and y >= 0 and y < len(self.grid[0]) and self.grid[x][y] != 'W'

    def move(self, x, y):
        posX = self.pos[0] + x
        posY = self.pos[1] + y

        if (self.canMove(posX,posY)):
            self.grid[self.pos[0]][self.pos[1]] = 0
            self.pos = (posX, posY)
            self.moved = True
