# подключаем модули
import pygame

# задаем константы
FPS = 60    # частота кадров

# инициация, создание объектов и тд
pygame.init()
screen = pygame.display.set_mode((600, 400))    # создали окно
bgColor = 255, 255, 255    # задали цвет фона
clock = pygame.time.Clock()
pygame.display.set_caption("Задание 1")    # дали название окну

# главный цикл
while 1:

    # закрашивание фона
    screen.fill(bgColor)

    # обновление экрана
    pygame.display.update()

    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    # тут пишем основной код
