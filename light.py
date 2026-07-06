import pygame

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Светофор")

clock = pygame.time.Clock()

# Цвета
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

light = "red"
timer = 0

running = True

while running:
    dt = clock.tick(60)  # 60 FPS
    timer = timer + dt   # сколько миллисекунд прошло

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Смена цвета
    if light == "red" and timer >= 3000:
        light = "yellow"
        timer = 0

    elif light == "yellow" and timer >= 1000:
        light = "green"
        timer = 0

    elif light == "green" and timer >= 3000:
        light = "red"
        timer = 0

    screen.fill(WHITE)

    # Корпус светофора
    pygame.draw.rect(screen, BLACK, (125, 100, 150, 350), border_radius=20)

    # Лампы
    pygame.draw.circle(screen, RED if light == "red" else GRAY, (200, 170), 45)
    pygame.draw.circle(screen, YELLOW if light == "yellow" else GRAY, (200, 275), 45)
    pygame.draw.circle(screen, GREEN if light == "green" else GRAY, (200, 380), 45)

    pygame.display.update()

pygame.quit()