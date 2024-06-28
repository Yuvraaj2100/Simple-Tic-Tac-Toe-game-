import pygame

# Function to draw the grid
def draw_grid(screen, block_size):
    screen.fill((255,255,237))  # Grey color
    for i in range(0, screen.get_width(), block_size):
        for j in range(0, screen.get_height(), block_size):
            rect = pygame.Rect(i, j, block_size, block_size)
            pygame.draw.rect(screen, (128, 128, 128), rect, 1)

# Function to draw X and O images
def draw_marks(screen, grid, X_IMAGE, O_IMAGE, block_size):
    for row in range(3):
        for col in range(3):
            if grid[row][col] == 'X':
                screen.blit(X_IMAGE, (col * block_size, row * block_size))
            elif grid[row][col] == 'O':
                screen.blit(O_IMAGE, (col * block_size, row * block_size))

# Main function
def main():
    pygame.init()
    w, h = 600, 600
    block_size = w // 3
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption('Tic Tac Toe')

    X_IMAGE = pygame.image.load('/Users/yuvraaj/Desktop/tic tac toe/res/x.png')
    O_IMAGE = pygame.image.load('/Users/yuvraaj/Desktop/tic tac toe/res/o.png')
    X_IMAGE = pygame.transform.scale(X_IMAGE, (block_size, block_size))
    O_IMAGE = pygame.transform.scale(O_IMAGE, (block_size, block_size))

    grid = [[None for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    running = True
    while running:
        draw_grid(screen, block_size)
        draw_marks(screen, grid, X_IMAGE, O_IMAGE, block_size)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                clicked_row = mouseY // block_size
                clicked_col = mouseX // block_size
                if grid[clicked_row][clicked_col] is None:
                    grid[clicked_row][clicked_col] = current_player
                    current_player = 'O' if current_player == 'X' else 'X'

    pygame.quit()

