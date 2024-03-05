import pygame

pygame.init()
screen=pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    #pygame.QUIT event means that the user clicked X to exit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#fill the screen with a color to wipe away anything from last frame
screen.fill("black")


#flip() the display to put your work on screen
pygame.display.flip()

#limits fps to 60
clock.tick(60)
        