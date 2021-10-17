"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame

from menu import Menu
from levels import Levels

turn_count = 0
currentLevel = 0

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Echelle de fenêtre
screen_scale = 2

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = screen_scale*50
HEIGHT = screen_scale*50

# This sets the margin between each cell
MARGIN = screen_scale*1

# IMAGE SPRITE
IMAGE_CAT = pygame.image.load("img/cat2.png")
IMAGE_CAT = pygame.transform.scale(IMAGE_CAT, (WIDTH, HEIGHT))

IMAGE_MOUSE = pygame.image.load("img/mouse.png")
IMAGE_MOUSE = pygame.transform.scale(IMAGE_MOUSE, (WIDTH, HEIGHT))

IMAGE_WALL = pygame.image.load("img/wall.png")
IMAGE_WALL = pygame.transform.scale(IMAGE_WALL, (WIDTH, HEIGHT))

IMAGE_GRASS = pygame.image.load("img/grass.png")
IMAGE_GRASS = pygame.transform.scale(IMAGE_GRASS, (WIDTH, HEIGHT))

IMAGE_HOLE = pygame.image.load("img/hole.png")
IMAGE_HOLE = pygame.transform.scale(IMAGE_HOLE, (WIDTH, HEIGHT))

world = Levels()

grid = world.levels[world.currentLevel]
player = world.player[world.currentLevel]
cats = world.cats[world.currentLevel]

grid[player.pos[0]][player.pos[1]] = 'P'
for c in cats:
    grid[c.pos[0]][c.pos[1]] = 'C' if (grid[c.pos[0]][c.pos[1]] not in ('H','O')) else 'O'


def getCatByPos(x, y):
    for c in cats:
        if(c.pos == (x, y)):
            return c


# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [screen_scale*510, screen_scale*510]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Metal Gear Solid VI : Return of the Cat")

# Loop until the user clicks the close button.
done = False
victory = False
gameover = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not (done or victory):
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif(gameover == True):
            gameoverMenu = Menu(screen, 1)
            gameoverMenu.launch()

            # Continue
            world.Reset()
            gameover = False

            grid = world.levels[world.currentLevel]
            player.pos = world.player[world.currentLevel].initpos
            player.grid = grid
            cats = world.cats[world.currentLevel]

            grid[player.pos[0]][player.pos[1]] = 'P'
            for c in cats:
                grid[c.pos[0]][c.pos[1]] = 'C' if (grid[c.pos[0]][c.pos[1]] not in ('H','O')) else 'O'
                c.grid = grid
            screen = pygame.display.set_mode(WINDOW_SIZE)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(-1, 0)
            if event.key == pygame.K_DOWN:
                player.move(1, 0)
            if event.key == pygame.K_LEFT:
                player.move(0, -1)
            if event.key == pygame.K_RIGHT:
                player.move(0, 1)
            if event.key == pygame.K_SPACE:
                player.move(0, 0)
            if player.moved == True:
                player.moved = False
                if (grid[player.pos[0]][player.pos[1]] == 'H'):
                    world.currentLevel += 1
                    if(world.currentLevel == len(world.levels)):  # Victory break
                        victory = True
                    else:
                        # Open new level
                        grid = world.levels[world.currentLevel]
                        player = world.player[world.currentLevel]
                        cats = world.cats[world.currentLevel]
                        turn_count = 0

                        grid[player.pos[0]][player.pos[1]] = 'P'
                        for c in cats:
                            grid[c.pos[0]][c.pos[1]] = 'C' if (grid[c.pos[0]][c.pos[1]] not in ('H','O')) else 'O'
                elif(grid[player.pos[0]][player.pos[1]] == 'C'):
                    gameover = True
                else:
                    turn_count += 1
                print("turn count =", turn_count)
                for c in cats:
                    c.choix_action(turn_count)
                    if(c.pos == player.pos):
                        gameover = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if(grid[row][column] == 'C'):
                cats[0].souffle()

    # Set the screen background
    screen.fill(BLACK)

    # Draw the grid

    # Draw grass
    for row in range(10):
        for column in range(10):
            # Affichage du sprite grass sur la case
            screen.blit(IMAGE_GRASS, [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                      WIDTH,
                                      HEIGHT])
    for row in range(10):
        for column in range(10):
            tile = grid[row][column]

            # Draw dangerous areas and grass
            for c in cats:
                # Affichage d'une case rouge en cas de vision du chat
                if c.vision[row][column] == 'V':
                    pygame.draw.rect(screen,
                                     RED,
                                     [(MARGIN + WIDTH) * column + MARGIN,
                                      (MARGIN + HEIGHT) * row + MARGIN,
                                         WIDTH,
                                         HEIGHT])

            # Draw the rest
            # Affichage du sprite wall sur la case
            if tile == 'W':
                screen.blit(IMAGE_WALL, [(MARGIN + WIDTH) * column + MARGIN,
                                         (MARGIN + HEIGHT) * row + MARGIN,
                                         WIDTH,
                                         HEIGHT])
            elif tile == 'H':
                screen.blit(IMAGE_HOLE, [(MARGIN + WIDTH) * column + MARGIN,
                                         (MARGIN + HEIGHT) * row + MARGIN,
                                         WIDTH,
                                         HEIGHT])

            # Affichage du sprite cat sur la case
            if tile == 'C':
                cat = getCatByPos(row, column)
                IMAGE_CAT_rotate = pygame.transform.rotate(
                    IMAGE_CAT, cat.direction)
                screen.blit(IMAGE_CAT_rotate, [(MARGIN + WIDTH) * column + MARGIN,
                                               (MARGIN + HEIGHT) * row + MARGIN,
                                               WIDTH,
                                               HEIGHT])
                                               
            # Affichage du sprite cat sur le trou
            if tile == 'O':
                screen.blit(IMAGE_HOLE, [(MARGIN + WIDTH) * column + MARGIN,
                                         (MARGIN + HEIGHT) * row + MARGIN,
                                         WIDTH,
                                         HEIGHT])
                cat = getCatByPos(row, column)
                IMAGE_CAT_rotate = pygame.transform.rotate(
                    IMAGE_CAT, cat.direction)
                screen.blit(IMAGE_CAT_rotate, [(MARGIN + WIDTH) * column + MARGIN,
                                               (MARGIN + HEIGHT) * row + MARGIN,
                                               WIDTH,
                                               HEIGHT])

            # Affichage du sprite Player sur la case
            if tile == 'P':
                screen.blit(IMAGE_MOUSE, [(MARGIN + WIDTH) * column + MARGIN,
                                          (MARGIN + HEIGHT) * row + MARGIN,
                                          WIDTH,
                                          HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
if(victory):
    victoryMenu = Menu(screen, 0)
    victoryMenu.launch()
elif(done):
    pygame.quit()
