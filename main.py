import pygame, random # импортируем pygame и рандом
from Car import Car
from pygame.locals import * 
from sys import exit # импортируем exit чтобы закрывать программу
pygame.init()

RED = (255, 0, 0) 
GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

speed = 1

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Game")


cars_list = pygame.sprite.Group()
playerCar = Car(RED, 60, 80, 70) # создается новая машинка красного цвета и шириной 20 и высотой 30
playerCar.rect.x = 160 
playerCar.rect.y = HEIGHT - 100

car1 = Car(PURPLE, 60, 80, random.randint(50, 100))
car1.rect.x = 60
car1.rect.y = -100

car2 = Car(YELLOW, 60, 80, random.randint(50, 100))
car2.rect.x = 160
car2.rect.y = -600

car3 = Car(BLUE, 60, 80, random.randint(50, 100))
car3.rect.x = 260
car3.rect.y = -300

car4 = Car(CYAN, 60, 80, random.randint(50, 100))
car4.rect.x = 360
car4.rect.y = -900

cars_list.add(playerCar)
cars_list.add(car1)
cars_list.add(car2)
cars_list.add(car3)
cars_list.add(car4)

all_coming_cars = pygame.sprite.Group()
all_coming_cars.add(car1)
all_coming_cars.add(car2)
all_coming_cars.add(car3)
all_coming_cars.add(car4)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        playerCar.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        playerCar.moveRight(5)
    if keys[pygame.K_UP]:
        speed += 0.1
    if keys[pygame.K_DOWN]:
        speed -= 0.1


    for car in all_coming_cars:
        car.moveForward(speed)
        if car.rect.y > HEIGHT:
            car.changeSpeed(random.randint(50, 100))
            car.rect.y = -200

    car_collision_list = pygame.sprite.spritecollide(playerCar, all_coming_cars, False)

    for car in car_collision_list:
        print("Car crash!")
        running = False
    
    cars_list.update()

    screen.fill(GREEN)

    pygame.draw.rect(screen, GREY, [40, 0, 400, HEIGHT])

    pygame.draw.line(screen, WHITE, [140, 0], [140, HEIGHT], 5)

    pygame.draw.line(screen, WHITE, [240, 0], [240, HEIGHT], 5)

    pygame.draw.line(screen, WHITE, [340, 0], [340, HEIGHT], 5)

    cars_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()