import pygame
import random


def load_image(name):
    image = pygame.image.load(name)
    image = image.convert_alpha()
    return image


def end_game(player):
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    screen.fill((5, 0, 75))
    screen_rect = (0, 0, 1000, 800)

    class Particle(pygame.sprite.Sprite):
        fire = [load_image("star.png")]
        for scale in (5, 10, 20):
            fire.append(pygame.transform.scale(fire[0], (scale, scale)))

        def __init__(self, pos, dx, dy):
            super().__init__(all_sprites)
            self.image = random.choice(self.fire)
            self.rect = self.image.get_rect()

            self.velocity = [dx, dy]
            self.rect.x, self.rect.y = pos

            self.gravity = 0.1

        def update(self):
            self.velocity[1] += self.gravity
            self.rect.x += self.velocity[0]
            self.rect.y += self.velocity[1]
            if not self.rect.colliderect(screen_rect):
                self.kill()

    def create_particles(position):
        particle_count = 7
        numbers = range(-5, 6)
        for _ in range(particle_count):
            Particle(position, random.choice(numbers), random.choice(numbers))

    running = True
    pygame.font.init()
    myfont = pygame.font.Font('Monly-Light.otf', 100)
    winner = myfont.render('Победитель: ' + str(player), False, (5, 0, 75))
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((5, 0, 75))

        create_particles((random.randint(0, 950), (random.randint(0, 750))))
        all_sprites.update()

        all_sprites.draw(screen)

        screen.fill((129, 193, 252), (0, 368, 1000, 100))
        screen.blit(winner, (250, 350))

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
