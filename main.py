import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("тестовый проект")
image = pygame.image.load("pyt.png")
image = pygame.transform.scale(image, (100, 100))
image_rect = image.get_rect()

speed = 5

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        image_rect.x -= speed

    if keys[pygame.K_RIGHT]:
        image_rect.x += speed

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()