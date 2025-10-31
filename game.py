import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.5
RADIUS = 20

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Physics Engine")
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self, x, y, vx, vy, color=BLUE):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color

    def update(self):
        self.vy += GRAVITY  # Apply gravity
        self.x += self.vx
        self.y += self.vy

        # Collision with walls
        if self.x - RADIUS < 0 or self.x + RADIUS > WIDTH:
            self.vx *= -1
            self.x = max(RADIUS, min(self.x, WIDTH - RADIUS))

        if self.y + RADIUS > HEIGHT:
            self.vy *= -0.9  # simulate bounce with energy loss
            self.y = HEIGHT - RADIUS
            if abs(self.vy) < 1:
                self.vy = 0  # stop small bouncing

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), RADIUS)

# Create balls
balls = [Ball(random.randint(100, 700), 100, random.uniform(-3, 3), 0) for _ in range(5)]

# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update and draw each ball
    for ball in balls:
        ball.update()
        ball.draw(screen)

    pygame.display.flip()

pygame.quit()
