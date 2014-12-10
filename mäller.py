import pygame
import random
from constants import *
green = (0,200,0)
red = (200,0,0)
white = (255,255,255)
black = (0,0,0)
bright_green = (0,255,0)
bright_red = (255,0,0)

all_sprites_list = pygame.sprite.Group()
platform_sprites_list = pygame.sprite.Group()
    
class Block(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = pygame.image.load(gray_brick)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(WHITE)
        self.rect.x = x
        self.rect.y = y

class Platform(Block):
    floortiles = []
    def __init__(self, x=0, y=0, generate=False):
        super().__init__()
        if generate:
            self.generate()
    def generate(self):
        self.generate_floor()
        self.generate_on_floor(5)
    def generate_floor(self, x=0, y=DISPLAY_HEIGHT):
        for i in range(int(x), int(DISPLAY_WIDTH), self.image.get_size()[0]):
            tile = Block(x=i, y= y - self.image.get_size()[1])
            self.floortiles.append(tile)
    def generate_on_floor(self, n=1):
        for i in range(n):
            position = random.randint(2,18) *64
            obstacle = random.choice(OBSTACLES)
            for coordinates in obstacle:
                X = coordinates[0] + position
                Y = coordinates[1] + DISPLAY_HEIGHT-128
                tile = Block(x= X, y= Y)
                self.floortiles.append(tile)

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

class Player(Character):
    #pilt_liigubvasemale = []
    #pilt_liigubparemale = []
    #pilt_hüppabvasemale = []
    #pilt_hüppabparemale = []
    kiirus = 10

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(liigubparemale1).convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()

    def hüppa(self):
        ...

    def mollingusse(self):
        self.image = pygame.image.load(mollingusse_p)

    def liiguvasemale(self):
        self.rect.x -= self.kiirus
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.x += self.kiirus
        else:
            # X = self.rect.x
            # Y = self.rect.y
            self.image = pygame.image.load(liigubvasemale1)
            # self.rect.x = X
            # self.rect.y = Y
    def liiguparemale(self):
        self.rect.x += self.kiirus
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.x -= self.kiirus
        else:
            self.image = pygame.image.load(liigubparemale1)

            # X = self.rect.x
            # Y = self.rect.y
            #self.image = pygame.image.load(liigubparemale1)
            #jooksebparemale.play()
            # self.rect = self.image.get_rect()
            # self.rect.x = X
            # self.rect.y = Y
    def liiguülesse(self):
        self.rect.y -= self.kiirus*2
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.y += self.kiirus
        else:
            # X, Y = self.rect.x, self.rect.y
            self.image = pygame.image.load(seisab)
            # self.rect = self.image.get_rect()
            # # self.rect.x = X
            # self.rect.y = Y
    def liigualla(self):
        self.rect.y += self.kiirus
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.y -= self.kiirus
        else:
            # X, Y = self.rect.x, self.rect.y
            self.image = pygame.image.load(seisab)
            # self.rect = self.image.get_rect()
            # self.rect.x = X
            # self.rect.y = Y

    def dogravity(self):
        self.rect.y += 10
        if pygame.sprite.spritecollide(self, platform_sprites_list, False):
            self.rect.y -= 10

def nupp(msg,x,y,laius,kõrgus,värv1,värv2,action=None):
    font = pygame.font.Font(None, 100)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+laius > mouse[0] > x and y+kõrgus > mouse[1] > y:
        pygame.draw.rect(gameDisplay, värv2, (x,y,laius,kõrgus))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, värv1, (x,y,laius,kõrgus))
    smallText = font.render(msg,1,black)
##    textSurf, textRect = text_objects(msg, smallText) 
##    textRect.center = ((x+(w/2)), (y+(h/2)))
    gameDisplay.blit(smallText, (x, y+50))
        
def game_intro():
    intro = True
    pygame.event.pump()
    key = pygame.key.get_pressed()
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.blit(background, (0,0))
        nupp("Start Game!",150,450,400,200,green,bright_green,game_loop)
        nupp("Quit Game!",750,450,400,200,red,bright_red,quit)
        pygame.display.update()
        clock.tick(15)

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
background = pygame.image.load("background1.png").convert()
clock = pygame.time.Clock()

x = (DISPLAY_WIDTH * 0.25)
y = (DISPLAY_HEIGHT * 0.5)

def game_loop():
    pygame.display.set_caption("Maskantje")
    crashed = False

    player = Player()
    põrand = Platform(generate=True)
    all_sprites_list.add(player, põrand.floortiles)
    platform_sprites_list.add(põrand.floortiles)
    player.rect.x = x
    player.rect.y = y
    
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        gameDisplay.blit(background, (0,0))

        pygame.event.pump()
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            player.liiguülesse()
        if key[pygame.K_DOWN]:
            player.liigualla()
        if key[pygame.K_LEFT]:
            player.liiguvasemale()
        if key[pygame.K_RIGHT]:
            player.liiguparemale()

        player.dogravity()

        if key[pygame.K_ESCAPE]:
            crashed = True

        all_sprites_list.draw(gameDisplay)
        pygame.display.update()
        clock.tick(30)
        
pygame.init()
game_intro()
pygame.quit()
quit()
