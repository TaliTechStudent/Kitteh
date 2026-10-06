import pygame, sys

pygame.init()

# Game Setup
WIDTH, HEIGHT = 1280, 720
FONT = pygame.font.SysFont("Consolas", int(WIDTH/20))
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong!")
CLOCK = pygame.time.Clock()

# Paddles
player = pygame.Rect(WIDTH-110, HEIGHT/2-50, 10, 100)
opponent = pygame.Rect(100, HEIGHT/2-50, 10, 100)
player_score = float(-0)
opponent_score = float(-0)
# Ball/cube
cube = pygame.Rect(0
                   ,0
                   ,20
                   ,20
                )

cube.center = (int(WIDTH/2), int(HEIGHT/2))
x_speed, y_speed = 1,1
def movement():
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_UP]:
                player.top -= 2
    if keys_pressed[pygame.K_DOWN]:
                player.top += 2
    if keys_pressed[pygame.K_w]:
                opponent.top -= 2
    if keys_pressed[pygame.K_s]:
                opponent.top += 2
def draw():
    SCREEN.fill((0, 0, 0)) # black
    pygame.draw.rect(SCREEN, (255, 255, 255), player) # player
    pygame.draw.rect(SCREEN, (255, 255, 255), opponent) #opponent
    pygame.draw.rect(SCREEN, (255, 255, 255), cube) # cube
    SCREEN.blit(FONT.render(str(int(opponent_score)),True, white),(100,100)) # placeholder
    SCREEN.blit(FONT.render(str(int(opponent_score)),True, white),(WIDTH-100, 100)) # placeholder
    pygame.display.update()
    CLOCK.tick(300)


def collisions():
    global y_speed, x_speed
   # edge of screen collisions
    if cube.y >= HEIGHT:
            y_speed *= -1
    if cube.y <= 0:
            y_speed *= -1
    if cube.x >= WIDTH:
            x_speed *= -1
    if cube.x <= 0:
            x_speed *=-1
   # paddle collisions
    if player.x - cube.width <= cube.x <= player.right and cube.y in range(player.top - cube.width, player.bottom + cube.width):
        x_speed *= -1
    if opponent.x - cube.width <= cube.x <= opponent.right and cube.y in range(opponent.top - cube.width, opponent.bottom + cube.width):
        x_speed *= -1

       
while True:
    
    white = (255,255,255)
    movement()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    collisions()
    cube.x += x_speed * 2
    cube.y += y_speed * 2
    draw()
    

