import pygame
import random

pygame.init()
square_width = 800
screen_height = 720
screen = pygame.display.set_mode([square_width] * 2)
clock = pygame.time.Clock()
running = True

#Function that generates starting position
def generate_starting_position():
    position_range = (pixel_width // 2, square_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]

#playground
pixel_width = 50

#snake
snake_pixel = pygame.rect.Rect([0, 0, pixel_width - 2, pixel_width - 2])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]
snake_direction = (0, 0)

#target
target = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
target.center = generate_starting_position()

while running:
    #pygame.QUIT event means that the user clicked X to exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    #Directional Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
       snake_direction = (0, - pixel_width)
    if keys[pygame.K_s]:
        snake_direction = (0, pixel_width)
    if keys[pygame.K_a]:
        snake_direction = (- pixel_width, 0)    
    if keys[pygame.K_d]:
        snake_direction = (pixel_width, 0)

    for snake_part in snake:
        pygame.draw.rect(screen, "green", snake_part)

    pygame.draw.rect(screen, "red", target)

    snake_pixel.move_ip(snake_direction)
    snake.append(snake_pixel.copy())
    snake = snake[-1:]

    #flip() the display to put your work on screen
    pygame.display.flip()

    #limits fps to 30
    clock.tick(10)

pygame.quit()
        