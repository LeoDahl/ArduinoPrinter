import pygame
import sys
import random
import subprocess
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Sim")
## Variables and stuff
x = 0
y = 0
width = 50
height =  50
vel=0.1
run = True
## While game is running
while run:
 for event in pygame.event.get():
   if event.type == pygame.QUIT:
     run =False

 keys=pygame.key.get_pressed()
 if keys[pygame.K_LEFT]:
      x-=vel
 if keys[pygame.K_RIGHT]:
      x+=vel
 if keys[pygame.K_UP]:
      y-=vel
 if keys[pygame.K_DOWN]:
      y+=vel
    
 win.fill((0,0,0))         
 pygame.draw.rect(win, (0,255,0), (0,y+((50-10)/2),500,10))
 pygame.draw.rect(win, (0,0,255), (x+((50-10)/2),0,10,500))
 pygame.draw.rect(win, (255,0,0), (x,y,width,height))
 pygame.display.update()
 

pygame.quit()