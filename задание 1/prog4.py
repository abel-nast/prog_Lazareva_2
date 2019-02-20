# подключаем модули
import pygame
from random import randint

# задаем константы
FPS = 60    # частота кадров
SCREEN_WIDTH = 600    # ширина окна
SCREEN_HEIGHT = 400   # высота окна
ballRadius = 111    # радиус мячика

# инициация, создание объектов и тд
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    # создали окно
bgColor = 255, 255, 255    # задали цвет фона
clock = pygame.time.Clock()
pygame.display.set_caption("Задание 1")    # дали название окну


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
        if self.rect.x + self.speedX >= SCREEN_WIDTH - ballRadius:
            self.speedX = -self.speedX
        elif self.rect.x + self.speedX <= 0:
            self.speedX = -self.speedX
        else:
            self.rect.x += self.speedX

        # описываем движение вдоль оси Y
        if self.rect.y + self.speedY >= SCREEN_HEIGHT - ballRadius:
            self.speedY = -self.speedY
        elif self.rect.y + self.speedY <= 0:
            self.speedY = -self.speedY
        else:
            self.rect.y += self.speedY


# создаем объекты принадлежащие классу
ball1 = Balls(randint(ballRadius, SCREEN_WIDTH - ballRadius), randint(ballRadius, SCREEN_HEIGHT - ballRadius))
ball2 = Balls(randint(ballRadius, SCREEN_WIDTH - ballRadius), randint(ballRadius, SCREEN_HEIGHT - ballRadius))
ball3 = Balls(randint(ballRadius, SCREEN_WIDTH - ballRadius), randint(ballRadius, SCREEN_HEIGHT - ballRadius))


# главный цикл
while 1:

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    # закрашивание фона
    screen.fill(bgColor)

    # рисуем мячики
    screen.blit(ball1.image, ball1.rect)
    screen.blit(ball2.image, ball2.rect)
    screen.blit(ball3.image, ball3.rect)

    pygame.display.update()  # обновление экрана

    # задержка
    clock.tick(FPS)

    # объекты движутся
    ball1.ball_motion()
    ball2.ball_motion()
    ball3.ball_motion()
