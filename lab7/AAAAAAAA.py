import pygame

pygame.init()

screen = pygame.display.set_mode((800, 400))
running = True
is_red = True
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)


while running: #game loop
    for event in pygame.event.get(): #event loop
        if event.type == pygame.QUIT:
            pygame.quit()#running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red

    if is_red:
        screen.fill(COLOR_RED)            
    else:
        screen.fill(COLOR_BLUE)
    pygame.display.flip() #update screen
