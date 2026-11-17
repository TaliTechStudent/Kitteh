import pygame
import numpy as np
import sys

# --- YOUR EXISTING LOGIC (UNCHANGED) ---
grid = np.zeros((3, 3), dtype=str)

def avalible_space(grid, x, y):
    try:
        if not grid[x, y] == '':
            return False
        else:
            return True
    except:
        return False

def check_winner(b, player):
    # Convert the board to True where it matches the player, False elsewhere
    mask = (b == player)
    
    # Check rows, columns, and both diagonals
    rows = np.any(np.all(mask, axis=1))
    cols = np.any(np.all(mask, axis=0))
    diag_main = np.all(np.diag(mask))
    diag_anti = np.all(np.diag(np.fliplr(mask)))
    
    return rows or cols or diag_main or diag_anti

# --- PYGAME VISUALIZATION ---
pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = WIDTH // 3
LINE_WIDTH = 10

BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
O_COLOR = (239, 231, 200)
X_COLOR = (84, 84, 84)
TEXT_COLOR = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")
font = pygame.font.SysFont("arial", 55, bold=True)

current_player = 'X'
game_over = False
status_text = ""

def draw_board():
    screen.fill(BG_COLOR)
    
    # Draw grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, HEIGHT), LINE_WIDTH)

    # Read your `grid` array to draw X's and O's
    padding = 45
    for x in range(3):
        for y in range(3):
            pixel_x = y * CELL_SIZE
            pixel_y = x * CELL_SIZE
            
            if grid[x, y] == 'O':
                center = (pixel_x + CELL_SIZE // 2, pixel_y + CELL_SIZE // 2)
                pygame.draw.circle(screen, O_COLOR, center, CELL_SIZE // 2 - padding, LINE_WIDTH)
                
            elif grid[x, y] == 'X':
                pygame.draw.line(screen, X_COLOR, (pixel_x + padding, pixel_y + padding),
                                 (pixel_x + CELL_SIZE - padding, pixel_y + CELL_SIZE - padding), LINE_WIDTH)
                pygame.draw.line(screen, X_COLOR, (pixel_x + padding, pixel_y + CELL_SIZE - padding),
                                 (pixel_x + CELL_SIZE - padding, pixel_y + padding), LINE_WIDTH)

def draw_banner(message):
    # Create a semi-transparent dark strip across the middle of the screen
    banner_height = 120
    overlay = pygame.Surface((WIDTH, banner_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 190))  # Black with 190/255 opacity
    screen.blit(overlay, (0, (HEIGHT - banner_height) // 2))
    
    # Render and center the winner text
    text_surface = font.render(message, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = event.pos
            
            x = mouse_y // CELL_SIZE
            y = mouse_x // CELL_SIZE
            
            if avalible_space(grid, x, y):
                grid[x, y] = current_player
                
                if check_winner(grid, current_player):
                    status_text = f"Player {current_player} Wins!"
                    game_over = True
                elif '' not in grid:
                    status_text = "It's a Draw!"
                    game_over = True
                else:
                    current_player = 'O' if current_player == 'X' else 'X'

    draw_board()
    if game_over:
        draw_banner(status_text)
    pygame.display.flip()
