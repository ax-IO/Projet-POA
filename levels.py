from player import Player
from catAgent import Cat


class Levels():
    def __init__(self):
        self.currentLevel = 0
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
        level1Player = Player(level1, (8, 5))
        level1Cats = [Cat(level1, level1Player, (2, 3)), ]

        level2 = [
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
        level2Player = Player(level2, (0, 0))
        level2Cats = [Cat(level2, level1Player, (7, 7)), Cat(level2, level1Player, (7, 5)), 
        Cat(level2, level1Player, (8, 6)), Cat(level2, level1Player, (5, 1)), Cat(level2, level1Player, (6, 6)), 
        Cat(level2, level1Player, (8, 3)), Cat(level2, level1Player, (5, 6)), Cat(level2, level1Player, (7, 6)),]

        self.levels = [level1, level2]
        self.player = [level1Player, level2Player]
        self.cats = [level1Cats, level2Cats]

    def Reset(self):
        self.currentLevel = 0
