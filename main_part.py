import pygame
import random
import pygame.display
from ending import end_game

n_stone = [6, 10, 15, 21]
names = ['Первый', 'Второй']


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
    first = names[0]
    second = names[1]

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

    ky = 0
    player = 1
    current = 0
    taken = 0
    winner = 0
            
    stones_sprites_group = pygame.sprite.Group()
    for i in range(n_stone[numb]):
        st = pygame.sprite.Sprite()
        st.image = load_im("pictures/diamond.png")
        st.rect = st.image.get_rect()
        stones_sprites_group.add(st)

    pygame.font.init()
    myfont = pygame.font.Font('Casper.ttf', 50)
    myfont_prev = pygame.font.Font('Casper.ttf', 20)
    player_one = myfont.render('Ходит ' + str(first), False, (255, 255, 255))
    player_two = myfont.render('Ходит ' + str(second), False, (255, 255, 255))
    curr_text = myfont.render('x' + str(current), False, (255, 255, 255))
    max_stone = pygame.font.Font('Casper.ttf', 20).render('Максимальное количество камней,'
                                                          ' которое можно взять за ход: '
                                                          + str(numb_move), False, (255, 255, 255))
    error = myfont_prev.render('Необходимо взять хотя бы один камень', False, (255, 255, 255))

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
    left_diamond = n_stone[numb]
    current_d = 1

    j = 0
    for i in stones_sprites_group:
        if j == current_d:
            ky += a_diamond
            kx = start_x - (a_diamond / 2) * current_d
            current_d += 1
        i.rect.x = kx
        i.rect.y = ky
        kx += a_diamond
        ki += 1
        left_diamond -= 1
        j += 1

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
                    stones_sprites_group.draw(screen)
                    mouse_sprites.draw(screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in stones_sprites_group:
                    if i.rect.collidepoint(event.pos):
                        current += 1
                        taken += 1
                        i.kill()
                        screen.blit(bg.image, bg.rect)
                        if taken == n_stone[numb]:
                            winner = player - 1
                            running = False
                            break
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
                        mouse_sprites.draw(screen)

                if left_tick.rect.collidepoint(event.pos):
                    if current == 0:
                        screen.blit(error, (320, 90))
                    else:
                        player = 2
                        current = 0
                        curr_text = myfont.render('x' + str(current), False, (255, 255, 255))
                        screen.blit(bg.image, bg.rect)
                        stones_sprites_group.draw(screen)
                    mouse_sprites.draw(screen)

                elif right_tick.rect.collidepoint(event.pos):
                    if current == 0:
                        screen.blit(error, (320, 90))
                    else:
                        player = 1
                        current = 0
                        curr_text = myfont.render('x' + str(current), False, (255, 255, 255))
                        screen.blit(bg.image, bg.rect)
                    mouse_sprites.draw(screen)

        if player == 1:
            screen.blit(player_one, (340, 10))
            screen.blit(left.image, left.rect)
            screen.blit(curr_text, (80, 660))
            screen.blit(left_tick.image, left_tick.rect)
        else:
            screen.blit(player_two, (340, 10))
            screen.blit(right.image, right.rect)
            screen.blit(curr_text, (880, 660))
            screen.blit(right_tick.image, right_tick.rect)

        screen.blit(max_stone, (180, 60))
        stones_sprites_group.draw(screen)
        mouse_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
    print(winner)
    end_game(names[winner])
