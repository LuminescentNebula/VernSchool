import pygame
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# === ГОТОВЫЙ КЛАСС (для примера) ===
class FallingBall:
    def __init__(self):
        self.x = random.randint(50, 550)
        self.y = 0
        self.radius = 15
        self.speed = 3

    def update(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.x = random.randint(50, 550)
            self.y = 0


# === ЗАДАНИЕ: допишите класс Player ===
class Player:
    def __init__(self, x:float, y:float):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 10
        self.speed = 5
        pass

    def move_right(self)->None:
        self.x += self.speed
        print(self.x)
        if self.x+self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH-self.width

    def move_left(self)->None:
        self.x -= self.speed
        if self.x - self.width < 0:
            self.x = 0
        pass

    def check_collision(self, ball:FallingBall)->bool:
        # TODO: верните True, если мяч коснулся игрока
        # Касания (коллизия) определяются с помощью сравнения позиций объектов с учетом их размеров
        pass


# === ГОТОВЫЙ КОД ИГРЫ (трогать не нужно) ===
player = Player(300, 500)
ball = FallingBall()
score = 0

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():    #Проверка что окно не закрыли
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: #Если стрелочка вправо нажата
        player.move_right() #То двигаться вправо
    else:
        player.move_left() #Иначе двигаться влево

    ball.update() #Подвигать мяч

    #Увеличить счёт, если есть столкновение
    if player.check_collision(ball):
        score += 1
        ball.y = 0
        ball.x = random.randint(50, 550)

    screen.fill((30, 30, 30))
    pygame.draw.circle(screen,
                       (255, 100, 100),
                       (int(ball.x), int(ball.y)), ball.radius) #Рисуем мяч
    pygame.draw.rect(screen,
                     (100, 255, 100),
                     (player.x, player.y, player.width, player.height)) #Рисуем игрока

    font = pygame.font.Font(None, 36)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
