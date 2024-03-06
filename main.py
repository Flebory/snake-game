import pygame
import random

pygame.init()
screen_width = 1280
screen_height = 720
screen=pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True

#Function that generates starting position
def generate_starting_position():
    position_range = (pixel_width // 2, screen_width - pixel_width // 2, pixel_width)
    return [random.randrange(*position_range), random.randrange(*position_range)]

#playground
pixel_width = 50

snake_pixel = pygame.rect.Rect([0, 0, pixel_width, pixel_width])
snake_pixel.center = generate_starting_position()
snake = [snake_pixel.copy()]

while running:
    #pygame.QUIT event means that the user clicked X to exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "purple", snake_pixel)

    #flip() the display to put your work on screen
    pygame.display.flip()

    #limits fps to 60
    clock.tick(60)

pygame.quit()
        