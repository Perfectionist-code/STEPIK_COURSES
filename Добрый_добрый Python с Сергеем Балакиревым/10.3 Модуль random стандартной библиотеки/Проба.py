import random
import pygame
import sys

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
W, H = 1440, 700 # размеры экрана

y = W/2 # ось y
x = H - H/10 # ось x

n = 2e5 # ЧИСЛО ТОЧЕК

screen = pygame.display.set_mode((W, H))

# сгенерим все точки
points = {}
for _ in range(int(n)):
    p = int(random.gauss(0, 160))
    if not points.get(p):
        points[p] = 1
    else:
        points[p] = points.get(p) + 1

# нарисуем все точки
for p in points:
    pygame.draw.circle(screen, 'white', (y+p, x-points[p]), 1)

# нарисуем оси
pygame.draw.line(screen, 'blue', (y, 0), (y, H))
pygame.draw.line(screen, 'green', (0, x), (W, x))
pygame.display.update()



while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()