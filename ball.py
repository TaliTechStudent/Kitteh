import pygame
import winreg

def is_windows_dark_mode():
    try:
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        # AppsUseLightTheme returns 0 for Dark Mode and 1 for Light Mode
        value, _ = winreg.QueryValueEx(key, "AppsUseLightTheme")
        return value == 0
    except Exception:
        # Fallback if the registry key doesn't exist (older Windows versions)
        print("no")
        return False
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800,600))
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        player_pos.x += 0.1
    if keys[pygame.K_LEFT]:
        player_pos.x -= 0.1
    if keys[pygame.K_UP]:
        player_pos.y -= 0.1
    if keys[pygame.K_DOWN]:
        player_pos.y += 0.1

    if is_windows_dark_mode():
            screen.fill((0,0,0))
            pygame.draw.circle(screen, "white", player_pos, 40)
    else:
            screen.fill((255,255,255))
            pygame.draw.circle(screen, "black", player_pos, 40)
    pygame.display.flip()
    clock.tick()