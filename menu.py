import pygame
from pygame import display

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)
RED = (76, 0, 19)

class Menu():
    def __init__(self, screen, type):
        pygame.font.init()
        self.type = type
        self.screen = screen
        w = h = 0
        if(self.type==0): #Victory Menu
            w = 800
            h = 600
            self.s = [w, h]
            self.screen = pygame.display.set_mode(self.s)
            self.screen.fill(BLACK)
            self.message_display("Vous avez atteint le dernier niveau!", 30, w/2 -280, 50, GRAY)
            self.message_display("Votre souris est saine et sauve.", 25, w/2 -220, 90, GRAY)
            self.message_display("Pressez une touche pour quitter le jeu...", 35, w/2 -350, 200, GRAY)
            self.message_display("Merci d'avoir joué !", 30, w/2 -150, 250, RED)
            self.message_display("Travail réalisé par : ", 20, 20, h - 250, WHITE)
            self.message_display("Pierre Hennecart", 28, 50, h - 200, WHITE)
            self.message_display("Gauthier Germain", 28, w - 350, h - 200, WHITE)
            self.message_display("Thomas ", 28, 50, h - 100, WHITE)
            self.message_display("Albena ", 28, w - 350, h - 100, WHITE)
        elif (self.type==1): #Game Over Menu
            w = 600
            h = 300
            self.s = [w, h]
            self.screen = pygame.display.set_mode(self.s)
            self.screen.fill(BLACK)
            self.message_display("GAME OVER", 50, w/2 -160, 50, RED)
            self.message_display("Vous vous êtes fait mangée!", 30, w/2 -220, 100, RED)
            self.message_display("Voulez-vous réessayer ?", 38, w/2 -220, h -80, WHITE)
            self.continueButton = pygame.Rect(w/2 - 101, h -35, 82, 30)
            self.quitButton = pygame.Rect(w/2 + 20, h -35, 80, 30)
            pygame.draw.rect(screen, [255, 0, 0], self.continueButton)
            self.message_display("Continuer", 16, w/2 - 101, h -28, BLACK)
            pygame.draw.rect(screen, [255, 0, 0], self.quitButton)
            self.message_display("Quitter", 16, w/2 + 30, h -28, BLACK)
        pygame.display.flip()
        
        

    def message_display(self, text, taille, x, y, couleur):
        font = pygame.font.Font(pygame.font.get_default_font(), taille)
        textsurface = font.render(text, True, couleur)
        self.screen.blit(textsurface,(x,y))
        
    def launch(self):
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if (self.type==0) and event.type == pygame.KEYDOWN:
                    gameExit = True
                elif(self.type==1) and event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # gets mouse position
                    if self.quitButton.collidepoint(mouse_pos):
                        gameExit = True
                    elif self.continueButton.collidepoint(mouse_pos):
                        gameExit = True
        pygame.quit()
        