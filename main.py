# from random import randint
# import pygame

# pygame.init()

# screen=pygame.display.set_mode((1000,800))

# #game icon and caption
# pygame.display.set_caption("Crumbling Building")
# icon= pygame.image.load("img/ufo.png")
# pygame.display.set_icon(icon)

# #player model
# player_model=pygame.image.load("img/alien_normal.png")
# playerX=370
# playerY=500
# playerx_change=0
# def player(x,y):
#     #blit draws the image
#     screen.blit(player_model,(x,y))

# #building blocks
# blockX=randint(0,900)
# blockY=50
# blocky_change=0
# # def block(x,y):
# #     pygame.draw.rect(screen,(0,0,0),pygame.Rect(x,y,100,100))
# class block:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         pygame.draw.rect(screen,(0,0,0),pygame.Rect(self.x,self.y,100,100))
#     def delete(self):
#         self.remove()
#         del self


# #keeps the game window running and close when the close window button is clicked on
# def main():
#     screen_running=True
#     while screen_running:

#         screen.fill((255,255,255))

#         for event in pygame.event.get():
#             if event.type==pygame.QUIT:
#                 screen_running=False
            
#             #movement keys
#             if event.type==pygame.KEYDOWN:
#                 if event.key == pygame.K_LEFT or event.key ==pygame.K_a:
#                     playerx_change-=0.1
#                 elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#                     playerx_change+=0.1
#             if event.type == pygame.KEYUP:
#                 if event.key == pygame.K_LEFT or event.key ==pygame.K_a or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
#                     print("up")
#                     playerx_change=0
#         playerX+=playerx_change
#         blocky_change=+0.1

#         blockY+=blocky_change
#         #setting a border on the game for player
#         if playerX<=0:
#             playerX=0
#         elif playerX>=936:
#             playerX=936

#         #setting a border on the gamer for the blocks
#         if blockY>=700:
#             blockY=700
#             block1.delete()

#         block1=block(blockX,blockY)
#         player(playerX,playerY)

#         pygame.display.update()
# main()
def add(num):
    num=num+1
a=1
add(1)
print(a)