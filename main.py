"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

# Import classes in directory
# from .user import User
# from .dir import Dir
# from AgentCat import AgentCat
# from Player import Player

# turn_count = 0
# old_turn_count = turn_count

class Player():
    def __init__(self, pos = (8, 5)):
        # First we create the image by filling a surface with blue color
        # img = pygame.Surface( (10, 15) ).convert()
        # img.fill(BLUE)

        # rec = pygame.transform.scale(IMAGE_CAT, (WIDTH, HEIGHT))
        self.pos = pos
    
    def move (self, x, y):
        posX = self.pos[0] + x
        posY = self.pos[1] + y

        if (posX>=0 and posX<len(grid[0]) and posY>=0 and posY<len(grid[0])):
            if (grid[posX][posY] != 'W') :
                self.pos = (posX, posY)
                # global turn_count 
                # turn_count+= 1
                # print(turn_count)
                cat.choix_action()
                

class Cat():
    def __init__(self, pos = (1, 7)):
        self.pos = pos
        self.direction = 0
    
    def choix_action(self):
        print("test")
        # global old_turn_count
        # old_turn_count = turn_count

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 40
HEIGHT = 40
 
# This sets the margin between each cell
MARGIN = 10

# IMAGE SPRITE
# <div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
# IMAGE_CAT = pygame.image.load("cat-black-face.png")
#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
IMAGE_CAT = pygame.image.load("cat.png")

IMAGE_CAT = pygame.transform.scale(IMAGE_CAT, (WIDTH, HEIGHT))
IMAGE_CAT_RECT = IMAGE_CAT.get_rect()
 

#<div>Icons made by <a href="https://www.freepik.com" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
IMAGE_MOUSE = pygame.image.load("mouse.png")
IMAGE_MOUSE = pygame.transform.scale(IMAGE_MOUSE, (WIDTH, HEIGHT))
IMAGE_MOUSE_RECT = IMAGE_MOUSE.get_rect()

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
# grid = []
# for row in range(10):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)  # Append a cell
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


player = Player((8, 5))
cat = Cat((1, 7))
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)

grid[cat.pos[0]][cat.pos[1]] = 'C'
grid[player.pos[0]][player.pos[1]] = 'P'


# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [510, 510]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Metal Gear Solid VI : Return of the Cat")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN :
            grid[player.pos[0]][player.pos[1]] = 0
            if event.key == pygame.K_UP:
                player.move(-1, 0)
            if event.key == pygame.K_DOWN:
                player.move(1, 0)
            if event.key == pygame.K_LEFT:
                player.move(0, -1)
            if event.key == pygame.K_RIGHT:
                player.move(0, 1)
            grid[player.pos[0]][player.pos[1]] = 'P'
        


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 'C'
            print("Click ", pos, "Grid coordinates: ", row, column)
        
        # print(turn_count)

        # if (turn_count>old_turn_count):
        #     cat.choix_action()
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 'W':
                color = GRAY
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            
            # Affichage du sprite cat sur la case
            if grid[row][column] == 'C':
                # color = GREEN
                IMAGE_CAT_rotate = pygame.transform.rotate(IMAGE_CAT, cat.direction)
                screen.blit(IMAGE_CAT_rotate, [(MARGIN + WIDTH) * column + MARGIN,
                                        (MARGIN + HEIGHT) * row + MARGIN,
                                        WIDTH,
                                        HEIGHT])
            # Affichage du sprite Player sur la case

            if grid[row][column] == 'P':
                screen.blit(IMAGE_MOUSE, [(MARGIN + WIDTH) * column + MARGIN,
                                        (MARGIN + HEIGHT) * row + MARGIN,
                                        WIDTH,
                                        HEIGHT])
                # screen.blit(IMAGE_CAT, [row,column, 20, 20])

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()