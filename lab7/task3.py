import pygame

pygame.init()
WIDTH = 800
HEIGHT = 400
sc = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle")
run = True
x = WIDTH//2
y = HEIGHT//2
radius = 25
movement = 20
clock = pygame.time.Clock()
while run:
    clock.tick(100)
    sc.fill((255,255,255))
    circle = pygame.draw.circle(sc,(255, 0, 0), (x,y), radius)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x > radius:
                x-=movement
            if event.key == pygame.K_RIGHT and x < WIDTH-radius:
                x+=movement
            if event.key == pygame.K_UP and y > radius:
                y-=movement
            if event.key == pygame.K_DOWN and y < HEIGHT-radius:
                y+=movement