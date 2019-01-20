import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))
    running = True
    bg = Background('cave.png', [0, 0])
    while running:
        screen.blit(bg.image, bg.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.flip()
    pygame.quit()
