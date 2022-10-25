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

# https://stackoverflow.com/questions/6339057/draw-a-transparent-rectangles-and-polygons-in-pygame
# Draw Triangles


def draw_polygon_alpha(surface, color, points):
    lx, ly = zip(*points)
    min_x, min_y, max_x, max_y = min(lx), min(ly), max(lx), max(ly)
    target_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.polygon(shape_surf, color, [
        (x - min_x, y - min_y) for x, y in points])
    surface.blit(shape_surf, target_rect)


# Echelle de fenêtre
screen_scale = 1

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = screen_scale*50
HEIGHT = screen_scale*50

# This sets the margin between each cell
MARGIN = screen_scale*1
world = Levels()

grid = world.levels[world.currentLevel]
player = world.player[world.currentLevel]
cats = world.cats[world.currentLevel]

grid[player.pos[0]][player.pos[1]] = 'P'
for c in cats:
    grid[c.pos[0]][c.pos[1]] = 'C' if (
        grid[c.pos[0]][c.pos[1]] not in ('H', 'O')) else 'O'


def getCatByPos(x, y):
    for c in cats:
        if (c.pos == (x, y)):
            return c


def sliceLoop(a):
    aSliced = a
    i = 0
    while i < len(aSliced):
        # print("i = " + str(i))
        # print("aSliced = " + str(aSliced))
        # print("len(aSliced) = " + str(len(aSliced)))
        if aSliced[i] in aSliced[:i]:
            previousIndex = aSliced[:i].index(aSliced[i])
            # print("aSliced = " + str(aSliced))
            # print("i = " + str(i))
            # print("aSliced[i] = " + str(aSliced[i]))
            # print("aSliced[:i] = " + str(aSliced[:i]))
            # print("previousIndex = " + str(previousIndex))
            for j in range(previousIndex, i):
                aSliced.pop(previousIndex)
            # print("new aSliced = " + str(aSliced))
            # print("\n")

            i = 0
        i += 1
    return aSliced


# Initialize pygame
pygame.init()


# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [screen_scale*510, screen_scale*510]

for cat in cats:
    cat.set_screen(WINDOW_SIZE, HEIGHT, WIDTH, MARGIN)
screen = pygame.display.set_mode(WINDOW_SIZE)

# IMAGE SPRITE

IMAGE_CAT = pygame.image.load("img/cat3.png")
IMAGE_CAT = pygame.transform.scale(IMAGE_CAT, (WIDTH, HEIGHT))

IMAGE_MOUSE = pygame.image.load("img/mouse.png")
IMAGE_MOUSE = pygame.transform.scale(IMAGE_MOUSE, (WIDTH, HEIGHT))

IMAGE_WALL = pygame.image.load("img/wall.png")
IMAGE_WALL = pygame.transform.scale(
    IMAGE_WALL, (WIDTH + MARGIN, HEIGHT + MARGIN))

IMAGE_GRASS = pygame.image.load("img/grass.png")
IMAGE_GRASS = pygame.transform.scale(IMAGE_GRASS, (WIDTH, HEIGHT))

IMAGE_HOLE = pygame.image.load("img/hole.png")
IMAGE_HOLE = pygame.transform.scale(IMAGE_HOLE, (WIDTH, HEIGHT))

EXC_MARK = pygame.image.load("img/exclamation-mark.png")
EXC_MARK = pygame.transform.scale(EXC_MARK, (screen_scale*15, screen_scale*30))

# Set title of screen
pygame.display.set_caption("Metal Gear Solid VI : Return of the Cat")
pygame.display.set_icon(IMAGE_CAT)

# Loop until the user clicks the close button.
done = False
victory = False
gameover = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

chemin = sliceLoop(player.chemin())

# -------- Main Program Loop -----------
while not (done or victory):
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif (gameover == True):
            gameoverMenu = Menu(screen, 1)
            gameoverMenu.launch()

            # Continue
            world.Reset()
            gameover = False

            grid = world.levels[world.currentLevel]
            player.pos = world.player[world.currentLevel].initpos
            player.grid = grid
            cats = world.cats[world.currentLevel]

            for cat in cats:
                cat.set_screen(WINDOW_SIZE, HEIGHT, WIDTH, MARGIN)

            grid[player.pos[0]][player.pos[1]] = 'P'
            for c in cats:
                grid[c.pos[0]][c.pos[1]] = 'C' if (
                    grid[c.pos[0]][c.pos[1]] not in ('H', 'O')) else 'O'
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
                chemin = sliceLoop(player.chemin())

                player.moved = False

                # If level complete
                if (grid[player.pos[0]][player.pos[1]] == 'H'):
                    world.currentLevel += 1
                    for cat in cats:
                        cat.setLastSeen(False)
                        cat.setState(0)
                    if (world.currentLevel == len(world.levels)):  # Victory break
                        victory = True
                    else:
                        # Open new level
                        grid = world.levels[world.currentLevel]
                        player = world.player[world.currentLevel]
                        cats = world.cats[world.currentLevel]

                        for cat in cats:
                            cat.set_screen(WINDOW_SIZE, HEIGHT, WIDTH, MARGIN)
                        turn_count = 0

                        grid[player.pos[0]][player.pos[1]] = 'P'
                        for c in cats:
                            grid[c.pos[0]][c.pos[1]] = 'C' if (
                                grid[c.pos[0]][c.pos[1]] not in ('H', 'O')) else 'O'
                elif (grid[player.pos[0]][player.pos[1]] == 'C'):
                    gameover = True
                else:
                    turn_count += 1
                # print("turn count =", turn_count)
                for c in cats:
                    # print("move3")
                    # print("direction " + str(cat.direction))
                    c.choix_action(turn_count)
                    if (c.pos == player.pos):
                        gameover = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            if (grid[row][column] == 'C'):
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
    # Draw cat vision cone
    for cat in cats:
        draw_polygon_alpha(screen, (255, 255, 0, 127), [
                           cat.positionCentre, cat.devantGauche, cat.devantDroite])

    # chemin = player.chemin()
    # print(chemin)

    # Draw Mouse path
    for coord in chemin:
        draw_polygon_alpha(screen,
                           (0, 0, 255, 127),
                           [((MARGIN + WIDTH) * coord[1] + MARGIN, (MARGIN + HEIGHT) * coord[0] + MARGIN),
                            ((MARGIN + WIDTH) * coord[1] + MARGIN + WIDTH,
                             (MARGIN + HEIGHT) * coord[0] + MARGIN),
                               ((MARGIN + WIDTH) * coord[1] + MARGIN + WIDTH,
                                (MARGIN + HEIGHT) * coord[0] + MARGIN+HEIGHT),
                               ((MARGIN + WIDTH) * coord[1] + MARGIN,
                                (MARGIN + HEIGHT) * coord[0] + MARGIN + HEIGHT)
                            ])

    for row in range(10):
        for column in range(10):
            tile = grid[row][column]

            # Draw dangerous areas and grass
            # for c in cats:
            #     # Affichage d'une case rouge en cas de vision du chat
            # if c.vision[row][column] == 'V':

            #         pygame.draw.rect(screen,
            #                          RED,
            #                          [(MARGIN + WIDTH) * column + MARGIN,
            #                           (MARGIN + HEIGHT) * row + MARGIN,
            #                              WIDTH,
            #                              HEIGHT])
            # if grid[row][column] not in ('P','C','H','O') :
            #     grid[row][column] = 'V'

            # Draw the rest
            # Affichage du sprite wall sur la case
            if tile == 'W':
                screen.blit(IMAGE_WALL, [(MARGIN + WIDTH) * column,
                                         (MARGIN + HEIGHT) * row,
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
                if (cat.state == 0):  # Patrolling
                    IMAGE_CAT = pygame.image.load("img/cat3.png")
                    IMAGE_CAT = pygame.transform.scale(
                        IMAGE_CAT, (WIDTH, HEIGHT))
                if (cat.state == 1):  # Chasing the player
                    IMAGE_CAT = pygame.image.load("img/cat3_angry.png")
                    IMAGE_CAT = pygame.transform.scale(
                        IMAGE_CAT, (WIDTH, HEIGHT))
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

                if (cat.state == 0):  # Patrolling
                    IMAGE_CAT = pygame.image.load("img/cat3.png")
                    IMAGE_CAT = pygame.transform.scale(
                        IMAGE_CAT, (WIDTH, HEIGHT))
                if (cat.state == 1):  # Chasing the player
                    IMAGE_CAT = pygame.image.load("img/cat3_angry.png")
                    IMAGE_CAT = pygame.transform.scale(
                        IMAGE_CAT, (WIDTH, HEIGHT))

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
            if cats[0].last_seen:
                screen.blit(EXC_MARK, [(MARGIN + WIDTH) * cats[0].last_seen[1] + WIDTH/3 + MARGIN,
                                       (MARGIN + HEIGHT) *
                                       cats[0].last_seen[0] + MARGIN,
                                       WIDTH,
                                       HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
if (victory):
    victoryMenu = Menu(screen, 0)
    victoryMenu.launch()
elif (done):
    pygame.quit()
