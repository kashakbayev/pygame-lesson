import pygame 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Car(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height, speed):  # car = Car(RED, 50, 100)
        
        super().__init__() # Нужно, чтобы спрайт нормально работал в Pygame
        self.image = pygame.Surface([width, height]) # создается невидимый пустой прямоугольник
        self.image.fill(WHITE) # закрашиваем поверхность белым
        self.image.set_colorkey(WHITE) # Белый цвет не показывать (сделать прозрачным)

        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

        pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height]) # рисуем внутри поверхности прямоугольник
        self.rect = self.image.get_rect() # получаем координаты объекта

    
    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveRight(self, pixels):
        self.rect.x += pixels
    
    def moveForward(self, speed):
        self.rect.y += self.speed * speed / 20

    def moveBackward(self, speed):
        self.rect.y -= self.speed * speed / 20

    def changeSpeed(self, speed):
        self.speed = speed

    

