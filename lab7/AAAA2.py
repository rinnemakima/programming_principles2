import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
running = True
is_red = True
WIDTH = 800
HEIGHT = 400
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)

movement_speed = 10

up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

clock = pygame.time.Clock()
FPS = 60

circle_x = WIDTH//2
circle_y = HEIGHT//2

while running: #game loop
    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT:
            pygame.quit()#running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
            if event.key == pygame.K_UP:
                up_pressed = True
            if event.key == pygame.K_DOWN:
                down_pressed = True
            if event.key == pygame.K_LEFT:
                left_pressed = True
            if event.key == pygame.K_RIGHT:
                right_pressed = True
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            if event.key == pygame.K_DOWN:
                down_pressed = False
            if event.key == pygame.K_LEFT:
                left_pressed = False
            if event.key == pygame.K_RIGHT:
                right_pressed = False

    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_UP]:
        circle_y -= movement_speed
    if pressed_keys[pygame.K_DOWN]:
        circle_y += movement_speed
    if pressed_keys[pygame.K_LEFT]:
        circle_x -= movement_speed
    if pressed_keys[pygame.K_RIGHT]:
        circle_x += movement_speed

    if is_red:
        screen.fill(COLOR_RED)            
    else:
        screen.fill(COLOR_BLUE)

    if not is_red:
        pygame.draw.circle(screen, COLOR_RED, (circle_x, circle_y), 40)
    else:
        pygame.draw.circle(screen, COLOR_BLUE, (circle_x, circle_y), 40)

    pygame.display.flip() #update screen
    clock.tick(FPS)
