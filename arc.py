import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение размеров экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Арканоид")

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Определяем параметры ракетки
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 7

# Определяем параметры мяча
BALL_SIZE = 10
BALL_SPEED = 5

# Определяем параметры кирпичей
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLUMNS = 10

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)

class MousePaddle(Paddle):
    def move(self, x):
        self.rect.x = x - self.rect.width // 2
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.dx = 0
        self.dy = 0
        self.start_speed = BALL_SPEED
        self.last_hit_by = None

    def start_moving(self):
        self.dx = self.start_speed
        self.dy = self.start_speed

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx
        if self.rect.top < 0:
            self.dy = -self.dy

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            x = col * (BRICK_WIDTH + 5) + 35
            y = row * (BRICK_HEIGHT + 5) + 35
            bricks.append(Brick(x, y))
    return bricks

def countdown():
    font = pygame.font.Font(None, 74)
    for i in range(3, 0, -1):
        SCREEN.fill(BLACK)
        text = font.render(str(i), True, WHITE)
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        SCREEN.blit(text, rect)
        pygame.display.flip()
        pygame.time.wait(1000)

def main():
    clock = pygame.time.Clock()
    paddle1 = Paddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 50)
    paddle2 = MousePaddle(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2 + 5, SCREEN_HEIGHT - 50 - PADDLE_HEIGHT - 5)
    ball = Ball()
    bricks = create_bricks()

    player1_score = 0
    player2_score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle1.move(-paddle1.speed)
        if keys[pygame.K_RIGHT]:
            paddle1.move(paddle1.speed)

        # Управление второй платформой с помощью мыши
        mouse_x, _ = pygame.mouse.get_pos()
        paddle2.move(mouse_x)

        if ball.dx == 0 and ball.dy == 0:  # Если мяч еще не начал двигаться
            countdown()  # Показываем отсчет
            ball.start_moving()  # Начинаем движение мяча

        ball.move()

        if ball.rect.colliderect(paddle1.rect):
            ball.dy = -ball.dy
            ball.last_hit_by = 1

        if ball.rect.colliderect(paddle2.rect):
            ball.dy = -ball.dy
            ball.last_hit_by = 2

        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.dy = -ball.dy
                bricks.remove(brick)
                break

        SCREEN.fill(BLACK)
        paddle1.draw(SCREEN)
        paddle2.draw(SCREEN)
        ball.draw(SCREEN)
        for brick in bricks:
            brick.draw(SCREEN)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
