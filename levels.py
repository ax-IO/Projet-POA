from player import Player
from catAgent import Cat
from mouseAgent import Mouse


class Levels():
    def __init__(self):
        self.currentLevel = 0
        pos_hole_level1 = (1, 0)
        level1 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['H', 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['W', 'W', 'W', 'W', 'W', 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        poid_level1 = -1
        poid_level1 = [
            [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
            [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
            [19, 18, 17, 16, 15, 14, 13, 12, 11, 10],
            [-10, -10, -10, -10, -10, 13, 12, 11, 10, 9],
            [7, 8, 9, 10, 11, 12, 11, 10, 9, 8],
            [6, 7, 8, 9, 10, 11, 10, 9, 8, 7],
            [5, 6, 7, 8, 9, 10, 9, 8, 7, 6],
            [4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
            [3, 4, 5, 6, 7, 8, 7, 6, 5, 4],
            [2, 3, 4, 5, 6, 7, 6, 5, 4, 3],
        ]
        level1Player = Mouse(level1, poid_level1, (8, 5))
        level1Cats = [Cat(level1, level1Player, (2, 3)), ]

        level2 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 0],
            ['H', 0, 0, 'W', 0, 0, 0, 0, 0, 0],
            ['W', 'W', 0, 'W', 'W', 0, 0, 0, 0, 0],
            [0, 'W', 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        poid_level2 = [
            [4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            [5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
            [6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [-10, -10, -10, -10, -10, -10, -10, -10, -10, 16],
            [30, 29, 28, -10, 20, 21, 20, 19, 18, 17],
            [-10, -10, 27, -10, -10, 22, 21, 20, 19, 18],
            [22, -10, 26, 25, 24, 23, 22, 21, 20, 19],
            [5, 6, 7, 8, 9, 10, 9, 8, 7, 6],
            [4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
            [3, 4, 5, 6, 7, 8, 7, 6, 5, 4],
        ]
        # level2Player = Player(level2, (1, 0))
        level2Player = Mouse(level2, poid_level2, (1, 0))
        level2Cats = [Cat(level2, level2Player, (8, 5)), Cat(
            level2, level2Player, (7, 6)), Cat(level2, level2Player, (8, 7)), ]

        level3 = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['W', 'W', 'W', 'W', 'W', 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 'H', 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        level3Player = Player(level3, (0, 0))
        level3Cats = [Cat(level3, level3Player, (7, 7)), Cat(level3, level3Player, (7, 5)),
                      Cat(level3, level3Player, (8, 6)), Cat(
                          level3, level3Player, (5, 1)), Cat(level3, level3Player, (6, 6)),
                      Cat(level3, level3Player, (8, 3)), Cat(level3, level3Player, (5, 6)), Cat(level3, level3Player, (7, 6)), ]

        self.levels = [level1, level2, level3]
        self.player = [level1Player, level2Player, level3Player]
        self.cats = [level1Cats, level2Cats, level3Cats]

    def Reset(self):
        self.currentLevel = 0

    def generateWeight(self, grid, gridWeight, width, heigth, x, y, w):

        if (x < width and y < width and x > 0 and y > 0):
            gridWeight[x, y] = max(gridWeight[x, y], w)

            self.generateWeight(grid, gridWeight, width, heigth, x+1, y, w-1)
            self.generateWeight(grid, gridWeight, width, heigth, x, y+1, w-1)
            self.generateWeight(grid, gridWeight, width, heigth, x-1, y, w-1)
            self.generateWeight(grid, gridWeight, width, heigth, x, y-1, w-1)

        return gridWeight

    # width = len(grid)
    # height = len(grid[0])


if __name__ == '__main__':
    level = Levels()
    level.generateWeight()
    # print("hello\n")

    # self.generateWeight(self.level1, self.poid_level1, width, height, self.pos_hole_level1[0], self.pos_hole_level1[1], 40)
