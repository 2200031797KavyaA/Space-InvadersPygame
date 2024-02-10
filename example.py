import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Image
enemy = pygame.image.load('enemy.png')

a = 1

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
 
    # Background Image
    screen.blit(background, (0, 0))

    screen.blit(enemy, (a,100))
    a = a + 1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
