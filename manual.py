# Import and initialize the pygame library
import pygame as py
from random import randrange

def snake_Tails(snake_List, SquareSize):
    for i in range(0, len(snake_List)):
        if i == len(snake_List) - 1: 
            py.draw.rect(screen, (0,204,0,255), [snake_List[i][0] * SquareSize, snake_List[i][1] * SquareSize, SquareSize, SquareSize])
        else:
            py.draw.rect(screen, (0,102,0,255), [snake_List[i][0] * SquareSize, snake_List[i][1] * SquareSize, SquareSize, SquareSize])
def gameover_menu(screen, w, h):
    width = (w * 10)/2
    height = (h * 10)/2
    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()

        f1 = py.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        text1 = f1.render("GameOver", 1, (0, 0, 0, 255))
        screen.blit(text1, (width + 25, height))
        py.display.flip()
        
def startMenu(scr, width, height):
    scr.fill((255,255,255,255))

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE: 
                    return
        f1 = py.font.Font("C:\Windows\Fonts\Arial.ttf", 50)
        f2 = py.font.Font("C:\Windows\Fonts\Arial.ttf", 20)

        text1 = f1.render("Welcome! To Snake", 1, (0, 0, 0, 255))
        text2 = f2.render("- You", 1, (0, 0, 0, 255))
        text3 = f2.render("- Fruit", 1, (0, 0, 0, 255))
        text4 = f1.render("press Space to Continue", 1, (0, 0, 0, 255))
        

        py.draw.rect(screen, (0,204,0,255), [width, height * 7, SquareSize, SquareSize])
        py.draw.rect(screen, (153,51,255,255), [width, height * 10, SquareSize, SquareSize]) # draw fruit

        scr.blit(text2, (width + 50, height * 7 - 5))
        scr.blit(text3, (width + 50, height * 10 - 5))
        scr.blit(text4, (width + 25, height * 15))
        scr.blit(text1, ((width * 17) - text1.get_width(), height))
        py.display.flip()

py.init()
# Set up the drawing window varibule
FieldW = 32 #64/2
FieldH = 18 #36/2
SquareSize = 20

screen = py.display.set_mode([FieldW * SquareSize, FieldH * SquareSize]) # Screen properties
py.display.set_caption('Snake Game')

clock = py.time.Clock()

Direction = 1
snake_speed = 15

snake_head = [5,5]

snake_List = [] # List of Snake tails x & y
snake_Count = 0

foodx = 4
foody = 10
step = 1

startMenu(screen, FieldW, FieldH) # Start Menu

f1 = py.font.Font("C:\Windows\Fonts\Arial.ttf", 20) # Text properties

# Run until the user asks to quit
while True:
    # Did the user click the window close button?
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.KEYDOWN: # If key was pressed, then change direction
            if event.key == py.K_LEFT:
                if(Direction != 1):
                    Direction = 0
            elif event.key == py.K_RIGHT:
                if(Direction != 0):
                    Direction = 1
            elif event.key == py.K_UP:
                if(Direction != 3):
                    Direction = 2
            elif event.key == py.K_DOWN:
                if(Direction != 2):
                    Direction = 3
    # Fill the background with light green
    screen.fill((240,240,240,255))

    for i in range(0, FieldW):
        for j in range(0, FieldH):
            if (i + j) % 2 == 0:
                py.draw.rect(screen, (210,210,210,255), [i * SquareSize, j * SquareSize, SquareSize, SquareSize])

    if Direction == 0: # Direction Left
        snake_head[0] += -1
    if Direction == 1: # Direction Right
        snake_head[0] += 1
    if Direction == 2: # Direction Up
        snake_head[1] += -1
    if Direction == 3: # Direction Down
        snake_head[1] += 1

    
    for i in range(0, len(snake_List)): # Mirroring snake
        if snake_head[0] >= FieldW:
            snake_head[0] = 0
        elif snake_head[0] < 0:
            snake_head[0] = FieldW - 1
        elif snake_head[1] >= FieldH:
            snake_head[1] = 0
        elif snake_head[1] < 0:
            snake_head[1] = FieldH - 1
    print(snake_head)
    print(snake_List)
               
    for i in range(0, len(snake_List)): # GameOver cycle
        if snake_List[-1][0] == snake_List[i][0] and snake_List[-1][1] == snake_List[i][1] and i != len(snake_List) - 1:
            gameover_menu(screen, FieldW, FieldH)
    
    snake_List.append([snake_head[0], snake_head[1]]) # Make line of squar's
    if len(snake_List) > snake_Count + 1: # Deleate other squar's 
        del snake_List[0]

    snake_Tails(snake_List, SquareSize) # Output all snake
    py.draw.rect(screen, (153,51,255,255), [foodx * SquareSize, foody * SquareSize, SquareSize, SquareSize]) # draw fruit

    if snake_head[0] == foodx and snake_head[1] == foody: # Check if we on fruit
        # Disable tail fruit spawning PLS!!!!!!
        foodx = randrange(0, FieldW)
        foody = randrange(0, FieldH)
        snake_Count += 1

    Score = f1.render(f"Score: {snake_Count}", 1, (0, 0, 0, 255))
    screen.blit(Score, (10, 10))
    # Flip the display
    py.display.flip()
    clock.tick(snake_speed) # Time tick