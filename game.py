import pygame, sys


pygame.init()
clock = pygame.time.Clock()


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, width,height, pos_x,pos_y, color):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)



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