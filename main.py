import pygame
from math import *

# Разрешение игрового окна
RESOLUTION = WIDTH, HEIGHT = 1200, 800

class Resources:
  pass

r = Resources()

def init():
    pygame.init()
    r.surface = pygame.display.set_mode(RESOLUTION)
    r.clock = pygame.time.Clock()
 
    # Инициализация шрифта
    r.font = pygame.font.SysFont('Verdana', 30)

    # Загрузка изображения из файла (и помечаем, что прозрачный цвет - цвет левого верхнего пикселя)
    r.img = pygame.image.load('img/mario.png').convert()
    r.img.set_colorkey(r.img.get_at((0, 0)), pygame.RLEACCEL)

    # Загрузка изображения из файла, уже содержащего прозрачность
    #r.img = pygame.image.load('img/mario.png').convert_alpha()

    # Загрузка изображения из файла и растягивание его до нужных размеров
    r.bg = pygame.image.load('img/bg.jpg').convert()
    r.bg = pygame.transform.scale(r.bg, (WIDTH, HEIGHT))

def run():
    global r
    s = r.surface

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        # Рисовать фон
        s.blit(r.bg, (0, 0))
        # Рисовать изображение
        px, py = 10, 30
        s.blit(r.img, (px, py))
        # Рисовать круг
        x, y, radius = 310, 120, 40
        pygame.draw.circle(s, pygame.Color('gainsboro'), (x, y), radius, 7)
        # Рисовать линию
        x1, y1 = 10, 10
        x2, y2 = 600, 200
        pygame.draw.line(s, pygame.Color('orange'), (x1, y1), (x2, y2), 3)

        # Показать кадр
        pygame.display.flip()
        r.clock.tick(20)

if __name__=='__main__':
    init()
    run()