import pygame
import random
import sys



# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Цвета
PLAYER_COLOR = pygame.Color('blue')
ENEMY_COLOR = pygame.Color('red')
BACKGROUND_COLOR = pygame.Color('white')


class Controller:
    """Базовый класс контроллера"""
    
    def get_input(self):
        """Получение ввода. Должен быть переопределен в наследниках"""
        raise NotImplementedError("Метод get_input должен быть реализован в подклассе")


class KeyboardController(Controller):
    """Контроллер управления от клавиатуры"""
    
    def __init__(self):
        self.keys = {
            'up': pygame.K_w,
            'down': pygame.K_s,
            'left': pygame.K_a,
            'right': pygame.K_d
        }
    
    def get_input(self):
        """Получение ввода от клавиатуры"""
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        
        if keys[self.keys['left']]:
            dx = -1
        if keys[self.keys['right']]:
            dx = 1
        if keys[self.keys['up']]:
            dy = -1
        if keys[self.keys['down']]:
            dy = 1
        
        return dx, dy


class RandomController(Controller):
    """Контроллер случайного движения"""
    
    def __init__(self, change_direction_chance=0.1):
        self.dx = random.choice([-1, 0, 1])
        self.dy = random.choice([-1, 0, 1])
        self.change_direction_chance = change_direction_chance
    
    def get_input(self):
        """Получение случайного направления движения"""
        # С повышенной вероятностью меняем направление
        if random.random() < self.change_direction_chance:
            self.dx = random.choice([-1, 0, 1])
            self.dy = random.choice([-1, 0, 1])
        
        return self.dx, self.dy


class Entity:
    """Базовый класс для всех игровых объектов"""
    
    def __init__(self, x, y, width, height, color, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)
    
    def move(self, dx, dy):
        """Базовое движение"""
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        """Обновление состояния. Должен быть переопределен в наследниках"""
        pass
    
    def draw(self, screen):
        """Отрисовка объекта"""
        pygame.draw.rect(screen, self.color, self.rect)


class Player(Entity):
    """Класс игрока с управлением от клавиатуры"""
    
    def __init__(self, x, y):
        super().__init__(x, y, 40, 40, PLAYER_COLOR, 5)
        self.controller = KeyboardController()
    
    def update(self):
        """Обновление состояния игрока"""
        dx, dy = self.controller.get_input()
        self.move(dx * self.speed, dy * self.speed)


class Enemy(Entity):
    """Класс врага со случайным движением"""
    
    def __init__(self, x, y):
        super().__init__(x, y, 35, 35, ENEMY_COLOR, 3)
        self.controller = RandomController(change_direction_chance=0.1)
    
    def update(self):
        """Обновление состояния врага"""
        dx, dy = self.controller.get_input()
        self.move(dx * self.speed, dy * self.speed)


class Game:
    """Главный класс игры"""
    
    def __init__(self):
        # Инициализация экрана
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Простая игра")
        self.clock = pygame.time.Clock()
        
        # Создание игровых объектов
        self.entities = [
            Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2),
            Enemy(100, 100),
            Enemy(700, 100),
            Enemy(100, 500),
            Enemy(700, 500)
        ]
        
        # Состояние игры
        self.running = True
    
    def handle_events(self):
        """Обработка событий"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
    
    def update(self):
        """Обновление игровых объектов"""
        # Полиморфизм: вызываем update() для всех entity
        for entity in self.entities:
            entity.update()
    
    def draw(self):
        """Отрисовка всех объектов"""
        # Очистка экрана
        self.screen.fill(BACKGROUND_COLOR)
        
        # Полиморфизм: вызываем draw() для всех entity
        for entity in self.entities:
            entity.draw(self.screen)
        
        # Обновление экрана
        pygame.display.flip()
        self.clock.tick(FPS)
    
    def run(self):
        """Главный игровой цикл"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
        
        pygame.quit()
        sys.exit()


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.run()
