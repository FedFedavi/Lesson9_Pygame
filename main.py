import pygame
import time
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("тестовый проект")
image = pygame.image.load("pyt.png")
image = pygame.transform.scale(image, (100, 100))
image_rect = image.get_rect()

image2 = pygame.image.load("red.png")
image2 = pygame.transform.scale(image2, (100, 100))
image2_rect = image2.get_rect()

image2_rect.x = 200
image2_rect.y = 200

last_collision_time = 0

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX - 50
            image_rect.y = mouseY - 50

        current_time = time.time()
        if current_time - last_collision_time >= 1:
            if image_rect.colliderect(image2_rect):
                print("Бух")
                image2_rect.x = image_rect.x - 50 + 3
                image2_rect.y = image_rect.y - 50 + 3
                last_collision_time = current_time

    screen.fill((0, 0, 0))
    screen.blit(image2, image2_rect)
    screen.blit(image, image_rect)
    pygame.display.flip()

pygame.quit()
