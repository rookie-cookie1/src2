import sys
import pygame
pygame.init()



screenSize = width, height = 1280, 720
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(screenSize)

ball = pygame.image.load('loogeyTransparent.png')
ball2 = pygame.image.load('fabioTransparent.png')
ballrect = ball.get_rect()
ballrect2 = ball2.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    ballrect2 = ballrect2.move(speed)
    if ballrect2.left < 0 or ballrect2.right > width:
        speed[0] = -speed[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed[1] = -speed[1]
    

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()