import pygame
import random


def load_image(name):
    image = pygame.image.load(name)
    image = image.convert_alpha()
    return image


def end_game(player):
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    screen.fill((240, 105, 5))

    class SnowFlake():
        def __init__(self, size, position, wind=False):
            self.size = size
            self.position = position
            self.wind = wind

        def fall(self, speed):
            self.position[1] += speed

        def draw(self):
            numb = (random.randint(20, 250))
            color = (numb, 175, 252)
            pygame.draw.circle(screen, color, self.position, self.size)

    running = True
    pygame.font.init()
    myfont = pygame.font.Font('Monly-Light.otf', 100)
    winner = myfont.render('Победитель: ' + str(player), False, (240, 105, 5))
    clock = pygame.time.Clock()
    snow_list = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((240, 105, 5))
        y_position = 0
        x_position = random.randint(0, 1000)
        speed = 1
        y_position += speed

        flake = SnowFlake(5, [x_position, y_position], False)

        snow_list.append(flake)

        for flake in snow_list:
            flake.draw()
            flake.fall(speed)

        screen.fill((129, 193, 252), (0, 368, 1000, 100))
        screen.blit(winner, (250, 350))

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
