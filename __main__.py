import sys
import pygame
from PIL import Image
import os
from natsort import natsorted, ns
pygame.init()
WIDTH = 1280
HEIGHT = 720
attack = False
frameList = [0, 0, 0]
facing = False #This boolean dictates wich direction loogey is facing
class playerObject: #Creates the player controllable object
    def __init__(self, image, height, speed):
        global loogeyMeleeAttackList
        global loogeyWalkingList
        global loogeyJumpingList
        global finished
        finished = True
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
        loogeyMeleeAttackList = []
        loogeyWalkingList = []
        loogeyJumpingList = []
        #These three FOR loops load the animation frames into the lists
        for frame in os.scandir('loogeyAnimations/loogeyMeleeAttack'):
            if frame.is_file():
                frame = pygame.image.load(frame).convert_alpha()
                loogeyMeleeAttackList.append(frame)
        for frame in os.scandir('loogeyAnimations/loogeyWalking'):
            if frame.is_file():
                frame = pygame.image.load(frame).convert_alpha()
                loogeyWalkingList.append(frame)
        for frame in os.scandir('loogeyAnimations/loogeyWalking'):
            if frame.is_file():
                frame = pygame.image.load(frame).convert_alpha()
                loogeyJumpingList.append(frame)

    #This move function activates functions via keypresses    
    def move(self, up = False, down = False, left = False, right = False, space = False):
        global attack
        global finished
        global facing
        if right:
            facing = True
            self.pos.right += self.speed
            #Does the walk animation of loogey is not attacking
            if attack == False:
                player.walk()
        if left:
            facing = False
            self.pos.right -= self.speed
            #Does the walk animation if loogey is not attacking
            if attack == False:
                player.walk()
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if space:
            attack = True
        #Do stuff
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT-SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT-SPRITE_HEIGHT
    def attack(self):
        global tick
        global finished
        global attack
        global frameList
        if finished == True:
            frameList[0] = 0
            finished = False
        if frameList[0] < len(loogeyMeleeAttackList):
            frame = frameList[0]    
            print(str(frame))
            self.image = loogeyMeleeAttackList[frame]
            frameList[0] = frameList[0] + 1
        else:
            frameList[0] = 0
            attack = False
            finished = True
    def jump(self):
        global tick 
        global jump
        i1 = 0
        if tick % 3 == 0:
            self.image = loogeyJumpingList[i1]
            jump = jump + 1
            if jump >= len(loogeyJumpingList):
                jump = 0
                
    def walk(self):
        global tick
        global frameList
        frame = frameList[1]
        if tick % 3 == 0 and frameList[1] < len(loogeyWalkingList):
            self.image = loogeyWalkingList[frame]
            frameList[1] = frameList[1] + 1
            if frameList[1] >= len(loogeyWalkingList):
                frameList[1] = 0
    
        
class gameObjectStatic:
    def __init__(self, color, width, height, posX, posY):
        self.color = color
        self.width = width
        self.height = height
        self.posX = posX
        self.posY = posY
        
    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.posX, self.posY, self.width, self.height))
    

screen = pygame.display.set_mode((1280, 720)) #Creates the screen
clock = pygame.time.Clock()                   #get a pygame clock object
playerImgPG = pygame.image.load('loogeySprite.png').convert_alpha() #opens and converts the image
playerImgPil = Image.open('loogeySprite.png')
SPRITE_HEIGHT = playerImgPil.height
SPRITE_WIDTH = playerImgPil.width
background = pygame.image.load('ResizedGameMenu.png').convert() #Opens and converts the image
screen.blit(background, (0, 0)) #Creates the background
objects = []            #Object list
props = []              #The props list
player = playerObject(playerImgPG, 0, 5) #Creates the player object
rectangle = gameObjectStatic((3, 3, 3), WIDTH, 60, 0, 660)
tick = 0
while True: #Main game loop
    #This if block slows the attack animation down to 20fps and activates 
    if attack == True and tick % 3 == 0:
        player.attack()  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, player.pos, player.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player.move(up=True)
    if keys[pygame.K_DOWN]:
        player.move(down=True)
    if keys[pygame.K_LEFT]:
        player.move(left=True)
    if keys[pygame.K_RIGHT]:
        player.move(right=True)
    if keys[pygame.K_SPACE]:
        player.move(space=True)
    rectangle.draw()
    screen.blit(player.image, player.pos)

    
    pygame.display.update()
    clock.tick(60)
    tick = tick + 1
    if tick >= 60:
        tick = 0
    