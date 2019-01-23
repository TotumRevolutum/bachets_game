import pygame


def end_game(player):
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    screen.fill((240, 105, 5))
    running = True
    pygame.font.init()
    myfont = pygame.font.SysFont('Optima', 50)
    winner = myfont.render('Победитель ' + str(player), False, (255, 255, 255))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(winner, (300, 400))
        pygame.display.flip()
    pygame.quit()
