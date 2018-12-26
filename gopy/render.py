import pygame
from pygame.locals import *


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((900, 1450))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    BackGround = Background('/Users/samuelmichael/gopy/darkgoban2.png', [0, 0])
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 200))
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        pygame.display.flip()


if __name__ == '__main__':
    main()
