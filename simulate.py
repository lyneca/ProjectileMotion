__author__ = 'wing2048'
from classes import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
done = False
ball = Object(100, 100, 1, True, 10, 10)
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    objects.update()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        for o in objects:
            o.playing = True
    else:
        for o in objects:
            o.playing = False


    screen.fill(WHITE)
    objects.draw(screen)
    pygame.display.flip()
    clock.tick(FRAMERATE)