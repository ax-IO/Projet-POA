class Entity():
    def __init__(self, grid, pos = (2, 7)):
        self.grid = grid
        self.pos = pos
    def move(self, off_x, off_y):
        self.pos[0] += off_x
        self.pos[1] += off_y