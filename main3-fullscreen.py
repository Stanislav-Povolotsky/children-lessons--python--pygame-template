import pygame
import pygame as pg
from math import *

# Разрешение игрового окна
RESOLUTION = WIDTH, HEIGHT = 1200, 800
FPS = 60

class Resources:
  pass

r = Resources()

def init():
    pygame.init()
    r.mode_flags = pg.HWSURFACE | pg.DOUBLEBUF | pg.RESIZABLE
    r.surface = pygame.display.set_mode(RESOLUTION, r.mode_flags)
    r.clock = pygame.time.Clock()
 
    # Инициализация шрифта
    r.font = pygame.font.SysFont('Verdana', 30)

    # Загрузка изображения из файла (и помечаем, что прозрачный цвет - цвет левого верхнего пикселя)
    r.img = pygame.image.load('img/mario.png').convert()
    r.img.set_colorkey(r.img.get_at((0, 0)), pygame.RLEACCEL)

    # Загрузка изображения из файла, уже содержащего прозрачность
    #r.img = pygame.image.load('img/mario.png').convert_alpha()

    # Загрузка изображения из файла и растягивание его до нужных размеров
    r.bg_orig = pygame.image.load('img/bg.jpg').convert()
    r.bg = pygame.transform.scale(r.bg_orig, (WIDTH, HEIGHT))

def run():
    global r
    s = r.surface
    px, py = 10, 30
    sx, sy = 0, 0
    rm = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.VIDEORESIZE:
                RESOLUTION = WIDTH, HEIGHT = event.dict['size']
                r.bg = pygame.transform.scale(r.bg_orig, (WIDTH, HEIGHT))
            elif event.type == pygame.KEYDOWN:
                if(event.key == pg.K_EQUALS): rm += 1
                if(event.key == pg.K_MINUS): rm -= 1

        # Get delta time in milliseconds
        dt = r.clock.tick(FPS) / 1000.0

        # Получить список нажатых клавиш. Список тут: https://www.pygame.org/docs/ref/key.html
        keys = pygame.key.get_pressed()

        # В зависимости от нажатых клавиш, выполняем действия
        csx, csy = 0, 0
        if(keys[pg.K_LEFT]): csx = -10 * dt
        if(keys[pg.K_RIGHT]): csx = 10 * dt
        if(keys[pg.K_UP]): csy = -10 * dt
        if(keys[pg.K_DOWN]): csy = 10 * dt
        sx = min(10, max(-10, sx + csx))
        sy = min(10, max(-10, sy + csy))
        px += sx
        py += sy
        if(not csx):
          if(abs(sx) > 1):
            sx -= 3 * (dt if sx > 1 else -dt if sx < 1 else 0)
          else: 
            sx = 0
        if(not csy):
          if(abs(sy) > 1):
            sy -= 3 * (dt if sy > 1 else -dt if sy < 1 else 0)
          else: 
            sy = 0

        # Рисовать фон (или изображение или очистка экрана)
        s.blit(r.bg, (0, 0)) # Рисуем фоновое изображение
        #s.fill('black')     # Заполняем фон чёрным цветом

        # Рисовать изображение
        s.blit(r.img, (px, py))
        # Рисовать круг
        x, y, radius = 310, 120, 40
        pygame.draw.circle(s, pygame.Color('gainsboro'), (x, y), radius * rm, 7)
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