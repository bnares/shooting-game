import pygame, sys


pygame.init()
clock = pygame.time.Clock()


#Game screen

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            

    pygame.display.update()
    clock.tick(60)