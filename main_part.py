import pygame
import os


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def mouse_im(name):
    image = pygame.image.load(name)
    image = image.convert_alpha()
    return image


def start_game():
    pygame.init()
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))
    running = True
    bg = Background('cave.png', [0, 0])

    mouse_sprites = pygame.sprite.Group()
    mouse = pygame.sprite.Sprite()
    mouse.image = mouse_im("knife.png")
    mouse.rect = mouse.image.get_rect()
    mouse_sprites.add(mouse)

    pygame.mouse.set_visible(False)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_focused():
                    mouse.rect.x = event.pos[0]
                    mouse.rect.y = event.pos[1]
                    screen.blit(bg.image, bg.rect)
                    mouse_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
