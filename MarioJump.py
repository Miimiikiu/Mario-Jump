#TODO LIST:
#Make Mario move left & right
#Spawn Mushrooms
#Make Mushrooms move
#Add gravity for Mario
#Make Mario bounce on the mushrooms
#Spawn coins
#Make coins move
#Make score increase when touching coins



# Import and initialize the pygame library
import pygame
#TODO: imports

pygame.init()

WIDTH = 800
HEIGHT = 500
screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

bg = pygame.image.load(r'./Assets/bg.jpg')
bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
jump_sound = pygame.mixer.Sound('./Assets/jump.wav')
#time.sleep(2)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #TODO:  Initialize speed
        self.image = pygame.image.load(r'./Assets/mario.png')
        self.image = pygame.transform.scale(self.image,(150,150))
        
        self.rect = self.image.get_rect()
        #TODO:  Set initial position
    def update(self):
        
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            #TODO:  Change speed 
            pass
        elif keystate[pygame.K_RIGHT]:
            #TODO:  Change speed
            pass


        #TODO:  Gravity
        
        #TODO:  Translate


        if self.rect.y >= HEIGHT:
            #TODO:  Game over
            pass


        
    def jump(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE]:
            #TODO:  Bounce high
            pass
        else:
            #TODO:  Bounce low
            pass
        #jump_sound.play()
        
        
class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'./Assets/mushroom.png')
        # Make random size
        size = 50
        self.image = pygame.transform.scale(self.image,(size,size))
        self.rect = self.image.get_rect()
        # Initialize starting positions
        # Initialize speed
        
    def update(self):
        # Translate
        pass
        
        
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'./Assets/coin.png')
        size = 50
        self.image = pygame.transform.scale(self.image,(size, size))
        self.rect = self.image.get_rect()
        # Set starting position
        # Set random speed
        
    def update(self):
        # Translate
        pass
            
        


player = Player()
players = pygame.sprite.Group()
players.add(player)
mushroom = Mushroom()
mushrooms = pygame.sprite.Group()
mushrooms.add(mushroom)
coin = Coin()
coins = pygame.sprite.Group()
coins.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(mushroom)
all_sprites.add(coin)
all_sprites.add(player)
'''
def new_mushroom():
    #TODO:  Make new mushroom called m
    all_sprites.add(m)
    mushrooms.add(m)
    
def new_coin():
    #TODO:  Make new coin called c
    all_sprites.add(c)
    coins.add(c)
'''
    
#TODO: Set random pause for mushroom, minimum 1 sec
#TODO: Set random pause for coin, minimum 1 sec
#start_mushroom = time.time()
#start_coin = time.time()
#TODO:  Initialize score
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    all_sprites.update()
    hits = pygame.sprite.groupcollide(mushrooms, players, False, False)
    for hit in hits:
        #TODO:  Make mario jump
        break
    hits = pygame.sprite.groupcollide(coins, players, True, False)
    for hit in hits:
        #TODO:  Increase score by 1
        break
    #TODO:  Make new mushroom if it has been long enough
    #TODO:  Make new coin if it has been long enough

    #time.sleep(.03)
    screen.fill(BLACK)
    screen.blit(bg, (0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    

# Done! Time to quit.
#print(score)
pygame.quit()