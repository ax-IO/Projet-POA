from entity import Entity


class Player(Entity):
    def __init__(self, grid, pos=(8, 5)):
        super(Player, self).__init__(grid, pos)

    def move(self, x, y):
        super(Player, self).move(x, y)

        if(self.moved and self.grid[self.pos[0]][self.pos[1]] != 'H'
           and self.grid[self.pos[0]][self.pos[1]] != 'C'):
            self.grid[self.pos[0]][self.pos[1]] = 'P'
