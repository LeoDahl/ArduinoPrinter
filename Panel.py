import pygame 
import math
import time
# RGB CODES
Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
# Settings
Size = (500,500)
grid = [[0 for _ in range(25)] for _ in range(25)]
print(grid)
# Init
pygame.init() 
mouse = pygame.mouse
# CREATING CANVAS 
canvas = pygame.display.set_mode((600,500))
canvas.fill(White)
##pygame.draw.rect(canvas, White, pygame.Rect(0, 0, 10, 10))
blockSize = 20 #Set the size of the grid block
## CREATE GRID
def drawGrid():
    for x in range(0, Size[0], blockSize):
        for y in range(0, Size[1], blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(canvas, Black, rect, 1)

# TITLE OF CANVAS 
pygame.display.set_caption("My Board") 
drawGrid()
exit = False
  
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current mouse position and state
    mouse_buttons = pygame.mouse.get_pressed()
    if mouse_buttons[0]:  # Left mouse button is pressed
        Pos = pygame.mouse.get_pos()
        color = canvas.get_at((Pos[0], Pos[1]))  # Correct function to get color
        if color != Black:  # Assuming black is the default background color with alpha
            XPos = math.floor((Pos[0] / Size[0]) * 25)
            YPos = math.floor((Pos[1] / Size[1]) * 25)
            if XPos <= 24 and YPos <= 24:
                grid[XPos][YPos] = 1
                print(grid)
                pygame.draw.rect(canvas, Black, pygame.Rect(XPos * blockSize, YPos * blockSize, blockSize, blockSize))
                print(XPos * blockSize, YPos * blockSize)
                pygame.display.update()  # Update the display after drawing




    pygame.display.update() 
