import pygame
from random import randint
from pygame import mixer

#initializes the pygame
pygame.init()

#setting the screen width and length
SCREEN=pygame.display.set_mode((1000,800))

#game icon and caption
pygame.display.set_caption("Crumbling Building")
icon= pygame.image.load("img/ufo.png")
pygame.display.set_icon(icon)

#frames the game will run on
FPS=60

#class for player
#used to display and keep track of the player position
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

#block class used to keep track of each block's positioning
class block():
    def __init__(self,x,y):
        self.x=x
        self.y=y         

#player_move used to keep track of the player's horizontral movement based off of key inputs and keeps the player in bound
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

#creates the block dropping and makes sure to reset the block when it hits the bottom of te screen
def block_move(block,player,score):
    pygame.draw.rect(SCREEN,(255,0,255),pygame.Rect(block.x,block.y,100,100))
    block.y+=10
    pygame.draw.rect(SCREEN,(255,0,255),pygame.Rect(block.x,block.y,100,100))
    if block.y>=700:
        block.y=0
        block.x=randint(0,900)
        score=score+1
    return score

#used to keep track if the player and a block has collided
def collision(block,player):
    if((player.y<block.y+100 and player.y>block.y) or (player.y+64>block.y and player.y+64<block.y+100)):
        if( (player.x>block.x and player.x<block.x+100) or (player.x+64>block.x and player.x+64< block.x+100)):
            return True
    return False

#prints the score onto the screen
def ScoreBoard(scorechange):
    font= pygame.font.Font("freesansbold.ttf",32)
    score=font.render("Score: "+ str(scorechange),True,(0,0,0))
    SCREEN.blit(score,(0,0))

#the main function
def main():

    #music for background
    mixer.music.load("audio/background_music.mp3")
    mixer.music.play(-1)
    mixer.music.set_volume(0.3)

    #used to keep the while loop to run on the frame
    clock=pygame.time.Clock()

    #constants used to set up the physics of the player jump
    GRAVITY=1
    JUMP_HEIGHT=20
    Y_VELOCITY=JUMP_HEIGHT

    #run is used to keep the application/window open
    run=True

    #assigns the player and block positioning
    player1=player(370,700)
    block_X=randint(0,900)
    block_Y=50
    block_list=[block(block_X,block_Y) for i in range(0,5)]

    #used to keep track of score and print out the score value
    score=0
    ScoreBoard(score)

    #keeps track of level
    level=1

    #variable to track if the game is over
    end_state=False

    #code to load the background image
    bg=pygame.image.load("img/background.jpg")
    bg=pygame.transform.scale(bg,(1000,800))

    #code to keep the screen running
    while run:
        #code to keep the background stay
        SCREEN.blit(bg,(0,0))
        clock.tick(FPS)

        #Checks if the close application on the window is selected
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                return
        
        #checks if the game has ended
        if(end_state):
            #if ended then display the current box positioning and the player positioning when the collision occurred
            for i in range(0,level):
                pygame.draw.rect(SCREEN,(255,0,255),pygame.Rect(block_list[i].x,block_list[i].y,100,100))
            player1.draw()

            #to display the game over screen
            font= pygame.font.Font("freesansbold.ttf",80)
            game_over=font.render("GAME OVER",True,(0,0,0))
            SCREEN.blit(game_over,(280,400))
        else:
            #the game continues
            #keeps track of the keys selected
            keys_pressed=pygame.key.get_pressed()
            #calls for horizontal movement
            player_move(keys_pressed,player1)
            #physics for the character's vertical movement
            if player1.jumping:
                player1.y-=Y_VELOCITY
                Y_VELOCITY-=GRAVITY
                if Y_VELOCITY < -JUMP_HEIGHT:
                    player1.jumping=False
                    Y_VELOCITY=JUMP_HEIGHT
            player1.draw()

            #shows the amount of blocks based on the game level
            for i in range(0,level):
                score=block_move(block_list[i],player1,score)

            #checks the score and increases the level based on the score of the game
            if(score%3==0 and (score/5)<5 and score!=0 and block_list[0].y==50):
                level+=1
        #used to check for collision of player to each block
        for i in range(0,level):
            if(collision(block_list[i],player1)):
                end_state=True

        #used to show the current score
        ScoreBoard(score)
        #keeps the window constantly updated
        pygame.display.update()

main()