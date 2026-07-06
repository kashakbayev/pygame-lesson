import pygame, random
pygame.init()

WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")
clock = pygame.time.Clock()

platform_x = 350
platform_y = 570
ball_x = 400
ball_y = 300
ball_dx = 3
ball_dy = 5
ball_radius = 10

running = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    
    ball_x = ball_x + ball_dx
    ball_y = ball_y + ball_dy

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_x > 0:
        platform_x -= 5
    if keys[pygame.K_RIGHT] and platform_x < WIDTH - 100:
        platform_x += 5

    if ball_x <= 0 or ball_x >= WIDTH:
        ball_dx = -ball_dx
    if ball_y <= 0:
        ball_dy = -ball_dy

    if platform_x <= ball_x <= platform_x + 100 and ball_y + ball_radius >= platform_y:
        ball_dy = -ball_dy

    if ball_y >= HEIGHT:
        ball_x = random.randint(0, WIDTH)
        ball_y = 0
        ball_dx = random.choice([-3, 3])
        ball_dy = random.choice([3, 5])

    screen.fill(SKY_BLUE)
    pygame.draw.rect(screen, BLUE, (platform_x, platform_y, 100, 20))
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()