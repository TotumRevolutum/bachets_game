import pygame
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

    screen = pygame.display.set_mode((1000, 800))
    screen.fill((255, 255, 255))
    running = True
    bg = Background('pictures/cave.png', [0, 0])

    mouse_sprites = pygame.sprite.Group()
    mouse = pygame.sprite.Sprite()
    mouse.image = load_im("pictures/knife.png")
    mouse.rect = mouse.image.get_rect()
    mouse_sprites.add(mouse)

    right = pygame.sprite.Sprite()
    right.image = load_im("pictures/right.png")
    right.rect = right.image.get_rect()

    left = pygame.sprite.Sprite()
    left.image = load_im("pictures/left.png")
    left.rect = left.image.get_rect()

    right_tick = pygame.sprite.Sprite()
    right_tick.image = load_im("pictures/tick.png")
    right_tick.rect = right_tick.image.get_rect()

    left_tick = pygame.sprite.Sprite()
    left_tick.image = load_im("pictures/tick.png")
    left_tick.rect = left_tick.image.get_rect()

    right.rect.x = 800
    right.rect.y = 650
    left.rect.x = 0
    left.rect.y = 650

    right_tick.rect.x = 750
    right_tick.rect.y = 655
    left_tick.rect.x = 200
    left_tick.rect.y = 655

    numb = random.randint(0, 3)
    numb_move = random.randint(2, 5)

    stones_sprites_group = []
    stones_sp = []

    ky = 0
    player = 1
    current = 0

    class Stone(pygame.sprite.Sprite):
        images = load_im("pictures/diamond.png")

        def __init__(self, group):
            super().__init__(group)
            self.image = Stone.images
            self.rect = self.image.get_rect()

    for i in range(n_stone[numb]):
        stones_sprites_group.append(pygame.sprite.Group())
        stones_sp.append(Stone(stones_sprites_group[i]))

    pygame.font.init()
    myfont = pygame.font.SysFont('Extra Cheese Melted', 50)
    curr_text = myfont.render('x' + str(current), False, (255, 255, 255))

    if numb == 0:
        ky = 350
    if numb == 1:
        ky = 300
    if numb == 2:
        ky = 200
    if numb == 3:
        ky = 120

    ki = 0
    start_x = 450
    kx = 450
    a_diamond = 90
    left_diamond = len(stones_sp)
    current_d = 1
    while (1):
        for i in range(current_d):
            stones_sp[ki].rect.x = kx
            stones_sp[ki].rect.y = ky
            kx += a_diamond
            ki += 1
            left_diamond -= 1
        ky += a_diamond
        kx = start_x - (a_diamond / 2) * current_d
        current_d += 1
        if (current_d > left_diamond):
            break

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
                        current += 1

                        if player == 1:
                            if current == numb_move:
                                player = 2
                                current = 0
                            curr_text = myfont.render('x' + str(current), False, (255, 255, 255))

                        elif player == 2:
                            if current == numb_move:
                                player = 1
                                current = 0
                            curr_text = myfont.render('x' + str(current), False, (255, 255, 255))
                        stones_sp[i].kill()
                        screen.blit(bg.image, bg.rect)

                        for i in range(n_stone[numb]):
                            stones_sprites_group[i].draw(screen)
                        mouse_sprites.draw(screen)

                if left_tick.rect.collidepoint(event.pos):
                    player = 2
                    current = 0
                    curr_text = myfont.render('x' + str(current), False, (255, 255, 255))
                    screen.blit(bg.image, bg.rect)

                    for i in range(n_stone[numb]):
                        stones_sprites_group[i].draw(screen)
                    mouse_sprites.draw(screen)

                elif right_tick.rect.collidepoint(event.pos):
                    player = 1
                    current = 0
                    curr_text = myfont.render('x' + str(current), False, (255, 255, 255))
                    screen.blit(bg.image, bg.rect)

                    for i in range(n_stone[numb]):
                        stones_sprites_group[i].draw(screen)
                    mouse_sprites.draw(screen)

        if player == 1:
            screen.blit(left.image, left.rect)
            screen.blit(curr_text, (80, 667))
            screen.blit(left_tick.image, left_tick.rect)
        else:
            screen.blit(right.image, right.rect)
            screen.blit(curr_text, (880, 667))
            screen.blit(right_tick.image, right_tick.rect)
        mouse_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
