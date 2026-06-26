import sys, pygame # Подключаем библиотеки:
pygame.init() # Запускаем Pygame.
width = 800
height = 600
size = [width, height] #Размер окна: ширина = 600 , высота = 500
speed = [1, 2] # Скорость мяча:  X = 0 (вправо и влево не движется) , Y = 2 (движется вниз)
white = (255, 255, 255) # Белый цвет в формате RGB.
screen = pygame.display.set_mode(size) #Создаём окно размером 600×500.
ball = pygame.image.load("ball.webp") #Загружаем картинку мяча из файла ball.bmp.
ballrect = ball.get_rect() #Получаем прямоугольник картинки. Он хранит координаты мяча.
while 1: # Бесконечный цикл программы
    for event in pygame.event.get(): #Проверяем события.
        if event.type == pygame.QUIT: # Если нажали крестик.
            sys.exit() #Закрываем программу.
    ballrect = ballrect.move(speed) # Перемещаем мяч.
    if ballrect.left < 0 or ballrect.right > width: #Проверяем: мяч коснулся левой границы или правой границы.
        speed[0] = -speed[0] #Меняем направление по X.
    if ballrect.top < 0 or ballrect.bottom > height: #верхнюю границу или нижнюю границу.
        speed[1] = -speed[1] # Меняем направление по Y.
    screen.fill(white) #Закрашиваем окно белым цветом.
    screen.blit(ball, ballrect) #Рисуем мяч в новых координатах.
    pygame.display.flip() #Обновляем экран.