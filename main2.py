import pygame
from random import randint
from pygame import mixer

pygame.init()
SCREEN=pygame.display.set_mode((1000,800))

#game icon and caption
pygame.display.set_caption("Crumbling Building")
icon= pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

FPS=60

class player():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.jumping=False
        self.crouch=False
    def draw(self):
        if self.jumping:
            player_model=pygame.image.load("img/alien_jump.png")
            SCREEN.blit(player_model,(self.x,self.y))
        elif self.crouch:
            player_model=pygame.image.load("img/alien_crouch.png")
            SCREEN.blit(player_model,(self.x,self.y))
        else:
            player_model=pygame.image.load("img/alien_normal.png")
            SCREEN.blit(player_model,(self.x,self.y))

class block():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        # pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.x,self.y,100,100))  
    # def draw(self):
    #     pygame.draw.rect(SCREEN,(0,0,0),pygame.Rect(self.x,self.y,100,100))           

def player_move(keys_pressed,player):
    playerx_change=0
    playery_change=0
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_a]:
        playerx_change-=5
        player.x+=playerx_change  
    if keys_pressed[pygame.K_RIGHT] or keys_pressed[pygame.K_d]:
        playerx_change+=5
        player.x+=playerx_change
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_w] or keys_pressed[pygame.K_SPACE]:
        player.jumping=True
    if keys_pressed[pygame.K_DOWN] or keys_pressed[pygame.K_s]:
        player.crouch=True
    else:
        player.crouch=False
    if player.x<=0:
        player.x=0
    elif player.x>=936:
        player.x=936  

def block_move(block,player):
    pygame.draw.rect(SCREEN,(255,0,255),pygame.Rect(block.x,block.y,100,100))
    block.y+=10
    pygame.draw.rect(SCREEN,(255,0,255),pygame.Rect(block.x,block.y,100,100))
    if block.y>=700:
        block.y=0
        block.x=player.x
        return True
    return False

def collision(block,player):
    #player.y<block.y+100 and player.y>block.y
    if((player.y<block.y+100 and player.y>block.y) or (player.y+64>block.y and player.y+64<block.y+100)):
        if( (player.x>block.x and player.x<block.x+100) or (player.x+64>block.x and player.x+64< block.x+100)):
            print("Game over")
            return False
    return True

def ScoreBoard(scorechange):
    font= pygame.font.Font("freesansbold.ttf",32)
    score=font.render("Score: "+ str(scorechange),True,(0,0,0))
    SCREEN.blit(score,(0,0))

def main():
    #music for background
    mixer.music.load("audio/background_music.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.5)

    clock=pygame.time.Clock()
    GRAVITY=1
    JUMP_HEIGHT=20
    Y_VELOCITY=JUMP_HEIGHT
    run=True
    player1=player(370,700)
    block_X=player1.x
    block_Y=50
    block1=block(block_X,block_Y)
    score=0
    ScoreBoard(score)
    
    bg=pygame.image.load("img/background.jpg")
    bg=pygame.transform.scale(bg,(1000,800))
    #code to keep the screen running
    while run:
        # SCREEN.fill((255,255,255))
        SCREEN.blit(bg,(0,0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                print("here")
                return

        keys_pressed=pygame.key.get_pressed()
        player_move(keys_pressed,player1)
        if player1.jumping:
            player1.y-=Y_VELOCITY
            Y_VELOCITY-=GRAVITY
            if Y_VELOCITY < -JUMP_HEIGHT:
                player1.jumping=False
                Y_VELOCITY=JUMP_HEIGHT


        player1.draw()
        if(block_move(block1,player1)):
            score+=1
        run=collision(block1,player1)
        ScoreBoard(score)
        pygame.display.update()
main()