import pygame
import os
import random
import pygame.display

n_stone = [6, 10, 15, 21]


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


def load_im(name):
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
    mouse.image = load_im("knife.png")
    mouse.rect = mouse.image.get_rect()
    mouse_sprites.add(mouse)

    numb = random.randint(0, 3)
    numb_move = random.randint(2, 5)

    stones_sprites_group = []
    stones_sp = []

    class Stone(pygame.sprite.Sprite):
        images = load_im("diamond.png")

        def __init__(self, group):
            super().__init__(group)
            self.image = Stone.images
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(200, 800)
            self.rect.y = 100

    for i in range(n_stone[numb]):
        stones_sprites_group.append(pygame.sprite.Group())
        stones_sp.append(Stone(stones_sprites_group[i]))

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
                    for i in range(n_stone[numb]):
                        stones_sprites_group[i].draw(screen)
                    mouse_sprites.draw(screen)
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(n_stone[numb]):
                    if stones_sp[i].rect.collidepoint(event.pos):
                        stones_sp[i].kill()
        pygame.display.flip()
    pygame.quit()


