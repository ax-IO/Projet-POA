from player import Player
from catAgent import Cat

class Levels():
    def __init__(self):
        self.currentLevel = 0
        level1 =[
            [0,0,0,0,0,0,0,0,0,0],
            ['H',0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            ['W','W','W','W','W',0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ]
        level1Player = Player(level1, (8, 5))
        level1Cats = [Cat(level1, (2,7)),]

        level2 =[
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            ['W','W','W','W','W',0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,'H',0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
        ]
        level2Player = Player(level2, (0, 0))
        level2Cats = [Cat(level2, (7,7)),Cat(level2, (7,5)),Cat(level2, (8,6))]

        self.levels = [level1, level2]
        self.player = [level1Player,level2Player]
        self.cats = [level1Cats,level2Cats]
