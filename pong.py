import pygame
import time
import random

ai_reaction_time = time.time()  # Time when the AI should react
ai_reaction_delay = 0.07  # Adjust for desired delay (in seconds)

# Initialize the game
pygame.init()

# Setting up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Ball settings
ball_size = 20
ball_x = screen_width // 2 - ball_size // 2
ball_y = screen_height // 2 - ball_size // 2
ball_dx = 5
ball_dy = 5

# Paddle settings
paddle_width = 20
paddle_height = 100
paddle_speed = 20  # This will be used for moving the paddles

# Player 1 Paddle
paddle1_x = 50  # Distance from the left edge
paddle1_y = screen_height // 2 - paddle_height // 2  # Centered vertically

# Player 2 Paddle
paddle2_x = screen_width - 50 - paddle_width  # Distance from the right edge
paddle2_y = screen_height // 2 - paddle_height // 2  # Centered vertically

def draw_ball(x, y):
    pygame.draw.rect(screen, white, (x, y, ball_size, ball_size))

def draw_paddle(x, y):
    pygame.draw.rect(screen, white, (x, y, paddle_width, paddle_height))

def ai_movement(paddle_y, ball_y):
    """AI strategy with more efficient delay handling"""
    global ai_reaction_time

    if time.time() > ai_reaction_time:  # Check if it's time for the AI to react
        ai_reaction_time = time.time() + ai_reaction_delay  # Schedule the next reaction

        # Calculate movement direction 
        if paddle_y + paddle_height // 2 < ball_y:
            return paddle_speed  # Move down
        elif paddle_y + paddle_height // 2 > ball_y:
            return -paddle_speed  # Move up
        else:
            return 0  # Stay in place
    else:
        return 0  # Don't move yet

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with black
    screen.fill(black)
    
    # Draw the ball and paddles
    draw_ball(ball_x, ball_y)
    draw_paddle(paddle1_x, paddle1_y)
    draw_paddle(paddle2_x, paddle2_y)
    
    # Updating the display
    pygame.display.flip()
    
    # Cap the frame rate
    pygame.time.Clock().tick(60)

    # Handling keyboard input for paddles movement
    keys = pygame.key.get_pressed()
    # Player 1 Controls
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < screen_height - paddle_height:
        paddle1_y += paddle_speed

    # Player 2 Controls (Optional: Can be replaced with AI or second player controls)
    # if keys[pygame.K_UP] and paddle2_y > 0:
    #     paddle2_y -= paddle_speed
    # if keys[pygame.K_DOWN] and paddle2_y < screen_height - paddle_height:
    #     paddle2_y += paddle_speed
        
    # AI Movement
    paddle2_y += ai_movement(paddle2_y, ball_y)

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Bounce off top and bottom walls
    if ball_y <= 0 or ball_y + ball_size >= screen_height:
        ball_dy = -ball_dy

    # Reset ball to the center if it goes past a paddle
    if ball_x <= 0 or ball_x + ball_size >= screen_width:
        ball_x, ball_y = screen_width // 2 - ball_size // 2, screen_height // 2 - ball_size // 2
        ball_dx = -ball_dx

    # Collision detection with paddles
    if ball_x <= paddle1_x + paddle_width and paddle1_y < ball_y + ball_size and paddle1_y + paddle_height > ball_y:
        ball_dx = -ball_dx
    if ball_x + ball_size >= paddle2_x and paddle2_y < ball_y + ball_size and paddle2_y + paddle_height > ball_y:
        ball_dx = -ball_dx


