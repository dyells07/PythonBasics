import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up window size
window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

# Set up game variables
velocity = 0
gravity = 0.1
box = pygame.Rect(25, 0, 25, 25)
pipe_vertical_gap = 200
pipe_width = 45
pipes = []
score = 0

# Set up fonts
font = pygame.font.SysFont("Arial", 30)

# Function to draw a box on the screen
def draw_box(box, color):
    pygame.draw.rect(screen, color, box)

# Function to generate new pipes
def generate_pipes():
    gap_position = random.randint(0, window_size[1] - pipe_vertical_gap)
    top_pipe = pygame.Rect(window_size[0], 0, pipe_width, gap_position)
    bottom_pipe = pygame.Rect(window_size[0], gap_position + pipe_vertical_gap, pipe_width, window_size[1] - gap_position - pipe_vertical_gap)
    pipes.append({"top_pipe": top_pipe, "bottom_pipe": bottom_pipe, "crossed": False})

# Function to end the game
def end_game():
    print("Game Over!")
    pygame.quit()
    sys.exit()

# Main game loop
clock = pygame.time.Clock()
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                velocity = velocity - 7
            elif event.key == pygame.K_LEFT:
                if box.left > 0:
                    box.left = box.left - 50
            elif event.key == pygame.K_RIGHT:
                if box.left < window_size[0] - box.width:
                    box.left = box.left + 50
            elif event.key == pygame.K_DOWN:
                if box.left < window_size[0] - box.width:
                    box.left = box.left + 50

    # Update game state
    screen.fill((0, 0, 0))
    velocity = velocity + gravity
    box.top = box.top + velocity

    # Box won't go up or down past edges of screen
    if box.top < 0:
        box.top = 0
        velocity = 0
    if box.top > window_size[1] - box.height:
        box.top = window_size[1] - box.height
        velocity = 0

    # Update pipes
    for i in range(len(pipes)):
        pygame.draw.rect(screen, (255, 0, 0), pipes[i]["top_pipe"])
        pygame.draw.rect(screen, (255, 0, 0), pipes[i]["bottom_pipe"])
        pipes[i]["top_pipe"].left -= 2
        pipes[i]["bottom_pipe"].left -= 2

        # Remove pipes that have gone off screen
        if pipes[i]["top_pipe"].left < -pipe_width:
            pipes.pop(i)
            i -= 1

        # Check for collision with the box
        if (box.left + box.width > pipes[i]["top_pipe"].left and
            box.left < pipes[i]["top_pipe"].left + pipe_width and
            (box.top < pipes[i]["top_pipe"].height or
             box.top + box.height > pipes[i]["bottom_pipe"].top)):
            end_game()

        # Check if box has passed a pipe
        if box.left > pipes[i]["top_pipe"].left + pipe_width and not pipes[i]["crossed"]:
            pipes[i]["crossed"] = True
            score += 1
            print(score)

    # Draw box and score
    draw_box(box, (128, 0, 128))
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (50, 50))

    # Generate new pipes at random intervals
    if random.randint(0, 30) == 0:
        generate_pipes()

    # Update display
    pygame.display.update()
    clock.tick(60)