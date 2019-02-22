# подключаем модули
import pygame
from random import randint

# задаем константы
FPS = 60    # частота кадров
SCREEN_WIDTH = 600    # ширина окна
SCREEN_HEIGHT = 400   # высота окна
BALLRADIUS = 111    # радиус мячика


# создаем класс мячиков
class Balls(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("intro_ball.gif")  # добавляем изображение мячика
        self.rect = self.image.get_rect(center=(x, y))
        self.speedX = randint(1, 3)   # задаем случайную скорость движения
        self.speedY = randint(0, 2)

    def ball_motion(self):
        # описываем движение вдоль оси Х
        if self.rect.x + self.speedX >= SCREEN_WIDTH - BALLRADIUS:
            self.speedX = -self.speedX
        elif self.rect.x + self.speedX <= 0:
            self.speedX = -self.speedX
        else:
            self.rect.x += self.speedX

        # описываем движение вдоль оси Y
        if self.rect.y + self.speedY >= SCREEN_HEIGHT - BALLRADIUS:
            self.speedY = -self.speedY
        elif self.rect.y + self.speedY <= 0:
            self.speedY = -self.speedY
        else:
            self.rect.y += self.speedY


if __name__ == "__main__":

    # инициация, создание объектов и тд
    numberOfBalls = 6  # количество мячиков
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # создали окно
    bgColor = 255, 255, 255  # задали цвет фона
    clock = pygame.time.Clock()
    pygame.display.set_caption("Задание 1")  # дали название окну
    ball_list = []  # для хранения мячиков

    # создаем объекты принадлежащие классу
    for i in range(numberOfBalls):
        ball = Balls(randint(BALLRADIUS, SCREEN_WIDTH - BALLRADIUS), randint(BALLRADIUS, SCREEN_HEIGHT - BALLRADIUS))
        ball_list.append(ball)

    # главный цикл
    while 1:

        # цикл обработки событий
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()

        # закрашивание фона
        screen.fill(bgColor)

        # рисуем мячики
        for ball in ball_list:
            screen.blit(ball.image, ball.rect)

        pygame.display.update()  # обновление экрана

        # задержка
        clock.tick(FPS)

        # объекты движутся
        for ball in ball_list:
            ball.ball_motion()
