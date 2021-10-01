import pygame

grid =[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        ['W','W','W','W','W',0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],  
]
class Player():
    def __init__(self, pos = (0, 0)):
        # First we create the image by filling a surface with blue color
        # img = pygame.Surface( (10, 15) ).convert()
        # img.fill(BLUE)

        # rec = pygame.transform.scale(IMAGE_CAT, (WIDTH, HEIGHT))
        self.pos = pos
    
    def move (self, x, y):
        
        posX = self.pos[0] + x
        posY = self.pos[1] + y
        # if (posX > 0 or posX < ) :
        
        # print(grid)
        # if(posX>0 and):
        #     self.pos = (posX, posY)
        # print(self.pos)

