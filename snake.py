import pygame

#initailizing pygame and creating window
pygame.init()

# this is setting up the size of window 
screen_width = 300
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tic Tac Toe by Bipin")

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

# Set the font
font = pygame.font.SysFont(None, 25)

# Set the clock
clock = pygame.time.Clock()

# Define the board as a list of lists
# board = [
#     ['-', '-', '-'],
#     ['-', '-', '-'],
#     ['-', '-', '-']
# ]

# Load the X and O images
x_img = pygame.image.load('x.png')
x_img = pygame.transform.scale(x_img, (100, int(x_img.get_height() * (100 / x_img.get_width()))))

o_img = pygame.image.load('o.png')
o_img = pygame.transform.scale(o_img, (100, int(o_img.get_height() * (100 / o_img.get_width()))))

# Define a function to draw the board
def draw_board():
    for row in range(3):
        for col in range(3):
            rect = pygame.Rect(col * 100, row * 100, 100, 100)
            pygame.draw.rect(screen, white, rect)
            pygame.draw.rect(screen, black, rect, 2)
            if board[row][col] == 'X':
                screen.blit(x_img, rect)
            elif board[row][col] == 'O':
                screen.blit(o_img, rect)

# Define a function to check if the board is full
def is_board_full():
    for row in board:
        if '-' in row:
            return False
    return True

# Define a function to check if the game is over
def is_game_over():
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[0][col] != '-' for row in range(len(board))):
            return True

    # Check diagonals
    if all(board[i][i] == board[0][0] and board[0][0] != '-' for i in range(len(board))) or \
       all(board[i][len(board)-i-1] == board[0][len(board)-1] and board[0][len(board)-1] != '-' for i in range(len(board))):
        return True

    # Check if the board is full
    if is_board_full():
        return True

    # If none of the above conditions are met, the game is not over
    return False

# Define a function to get the player's move
def get_move(player):
    text = font.render(f"Player {player}'s turn", True, black)
    screen.blit(text, (10, screen_height - 30))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                row = event.pos[1] // 100
                col = event.pos[0] // 100
                if board[row][col] == '-':
                    return row, col

# Define the main game loop
# Define the main game loop
def play_game():
    while True:
        # Initialize the board
        global board
        board = [
            ['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']
        ]

        player = 'X'
        while not is_game_over():
            draw_board()
            row, col = get_move(player)
            board[row][col] = player
            player = 'O' if player == 'X' else 'X'
            clock.tick(10)

        draw_board()
        if is_board_full():
            text = font.render("The game is a tie!", True, black)
        else:
            text = font.render(f"Player {player} wins!", True, black)
        screen.blit(text, (10, screen_height - 30))
        pygame.display.update()

        # Prompt the user to play again or quit
        text = font.render("Press 'Y' to play again or any other key to quit", True, black)
        screen.blit(text, (10, screen_height - 60))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_y:
                continue
            elif event.type == pygame.KEYDOWN:
                return

# Start the game
play_game()

# Quit Pygame
pygame.quit()