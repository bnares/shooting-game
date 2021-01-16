import pygame, sys


pygame.init()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)


class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picturePath):
        super().__init__()
        self.image = pygame.image.load(picturePath)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = pygame.mouse.get_pos()



#Game screen

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

#background

background = pygame.image.load("bg.png")


crosshair = Crosshair("crosshair_blue_small.png")

group = pygame.sprite.Group()
group.add(crosshair)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    crosshair.update()
    screen.blit(background, (0,0))
    group.draw(screen)
    pygame.display.update()
    clock.tick(60)