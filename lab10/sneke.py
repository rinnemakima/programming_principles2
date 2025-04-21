# importing libraries
import pygame
import time
import random
import psycopg2

#initial snake speed
snake_speed = 20
 
# Window size
window_x = 720
window_y = 480
 
# defining colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
 
# Initialising pygame
pygame.init()

conn = psycopg2.connect(
    dbname="SNEKE",
    user="postgres",
    password="L@remIpsum228",
    host="localhost"
)
cur = conn.cursor()

def execute_query(query):
    try:
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

query_create_table_user_and_userscore = """
    CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE
    );

    CREATE TABLE IF NOT EXISTS user_scores (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id),
        score INTEGER,
        level INTEGER,
        saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
"""

execute_query(query_create_table_user_and_userscore)

def get_user(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result:
        return result[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        return user_id

def get_user_data(username):
    cur.execute("SELECT id, username FROM users WHERE username = %s", (username,))
    user_data = cur.fetchone()
    if user_data:
        user_id = user_data[0]
        cur.execute("""
            SELECT score, level FROM user_scores 
            WHERE user_id = %s 
            ORDER BY saved_at DESC 
            LIMIT 1
        """, (user_id,))
        last_score = cur.fetchone()
        return {
            "user_id": user_id,
            "score": last_score[0] if last_score else 0,
            "level": last_score[1] if last_score else 1
        }
    return None

def save_user_score(user_id, score, level):
    cur.execute(""" 
        INSERT INTO user_scores (user_id, score, level) 
        VALUES (%s, %s, %s) 
    """, (user_id, score, level))
    conn.commit()
 
# Initialise game window
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))
 
# FPS
fps = pygame.time.Clock()
 
# snake head
snake_position = [100, 50]
 
# defining first 4 blocks of snake body
snake_body = [[100, 50], [90, 50], [80, 50],[70, 50]]

# fruit position
fruit_position = [random.randint(10, 60) * 10, random.randint(10, 30) * 10]

# Is fruit in the game?
fruit_spawn = True
 
# setting default snake direction
direction = 'RIGHT'
change_to = direction
 
# initial score
score = 0
level = 1
weight = random.randrange(10, 70, 10)
 
# displaying Score
def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect() 
    game_window.blit(score_surface, score_rect)

#displaying level
def show_level(color, font, size):
    # creating font object score_font
    level_font = pygame.font.SysFont(font, size)
    # create the display surface object 
    level_surface = level_font.render('Level : ' + str(level), True, color)
    # create a rectangular object for the text
    level_rect = level_surface.get_rect()
    level_rect.topright = (window_x - 10, 0)
    # displaying text
    game_window.blit(level_surface, level_rect)
 
# game over function
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)    # creating font
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red) # creating a text surface
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x/2, window_y/4) # setting position of the text
    game_window.blit(game_over_surface, game_over_rect) # blit will draw the text on screen
    pygame.display.flip()
     
    time.sleep(2)
    pygame.quit()
    quit()

#Foods which are disappearing after some time(timer)
CUSTOM_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CUSTOM_EVENT, 10000)
 
# Main Function
while True:
    for event in pygame.event.get(): # handling key events
        if event.type == CUSTOM_EVENT:#disapperaing fruit
            fruit_spawn = False

        if event.type == pygame.QUIT:
            game_over()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
 
    
    if change_to == 'UP' and direction != 'DOWN': # If two keys pressed simultaneously
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
 
    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10
 
    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if (fruit_position[0] <= snake_position[0] < fruit_position[0] + weight) and (fruit_position[1] <= snake_position[1] < fruit_position[1] + weight):
        score += weight
        level = 1 + score // 100
        fruit_spawn = False
        weight = random.randrange(10, 70, 10)
    else:
        snake_body.pop()

    #speed
    snake_speed = level * 20

    #if fruit is not on the map spawn it    
    if not fruit_spawn:
        fruit_position = [random.randint(10, 60) * 10, random.randint(10, 30) * 10]
         
    fruit_spawn = True
    game_window.fill(black)
    
    #drawing
    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
        
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], weight, weight))
 
    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > window_x-10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y-10:
        game_over()
 
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()
 
    # displaying score continuously
    show_score(white, 'times new roman', 20)
    show_level(white, 'times new roman', 20)

    
 
    # Refresh game screen
    pygame.display.update()
 
    # Frame Per Second /Refresh Rate
    fps.tick(snake_speed)