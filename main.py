import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption

clock = pygame.time.Clock()
FPS = 60

bg = pygame.image.load('')



run = True
while run:

    Clock.tick(FPS)


    for event in pygame.event.get():
        if event.type == pygame.QUIT :
           run  = False 

pygame.quit()           




