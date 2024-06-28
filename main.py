import pygame
import game

pygame.init()

# Screen setup
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Welcome!")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 100, 0)
BLUE = (0, 0, 255)

# Button setup
button_surface = pygame.Surface((150, 50))
button_font = pygame.font.SysFont('verdana', 20)
button_rect = pygame.Rect(210, 250, 200, 70)
button_text_start = button_font.render("Start Game", True, BLUE)
text_rect = button_text_start.get_rect(center=button_rect.center)

clock = pygame.time.Clock()

start_game = False  # Flag to indicate if game should start/grid should form

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                start_game = True  # Set flag to start the game

    # Clear screen
    screen.fill("sky blue")

    # Draw button and handle hover effect
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(button_surface, "light green", (0,0,150,50))
    else:
        pygame.draw.rect(button_surface, BLACK, (0, 0, 150, 50))
        pygame.draw.rect(button_surface, WHITE, (1, 1, 148, 48))
        pygame.draw.rect(button_surface, BLACK, (1, 1, 148, 1), 2)

    button_surface.blit(button_text_start, (button_surface.get_width() / 2 - text_rect.width / 2, button_surface.get_height() / 2 - text_rect.height / 2))
    screen.blit(button_surface, (button_rect.x, button_rect.y))

    # Main menu font
    font = pygame.font.SysFont("Futura", 68)
    img = font.render('TIC TAC TOE', True, "yellow")
    screen.blit(img, (100, 100))


    if start_game:
        game.main()  # Draw the grid on the screen

    pygame.display.update()
    clock.tick(60)

pygame.quit()
