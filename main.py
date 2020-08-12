import pygame
import random

width = 1080
height = 900
resolution = 20
cols = width//resolution 
rows = 11 + height//resolution # Why the fuck do I need to add 11 to get it to draw the entire screen with squares?

WHITE = (255,255,255)
BLACK = (0,0,0)

field = [[0 for row in range(rows)] for col in range(cols)]
print(f"rows:{rows}")
print(f"cols:{cols}")
#Assign values to squares
for col in range(cols):
    for row in range(rows):
        field[col][row] = (int)(random.uniform(0,2))

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Marching squares!')
screen.fill((220,220,220))
running = True
dotColor = pygame.Color(255)
def getBinaryState(a,b,c,d):
    return a*8 + b*4 + c*2 + d*1
SETUP = True
while running:
    for event in pygame.event.get():
        #print(pygame.mouse.get_pos())
        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()
            running = False
            quit()
        if SETUP:
            for col in range(cols):
                for row in range(rows):
                    #print(f"Col:{col} \t Row:{row} \t {field[col][row]}\n")
                    #print(f"{col*resolution} \t {row*resolution} \t {i}")
                    # if field[col][row] == 1:
                    #     dotColor = BLACK
                    # else:
                    #     dotColor = WHITE
                    dotColor = BLACK if field[col][row] == 1 else WHITE
                    pygame.draw.circle(screen,dotColor,(row*resolution,col*resolution),4)
                    SETUP = False
            print("START")
            for col in range(0,cols-1):
                for row in range(0,rows-1):
                    #pygame.display.update() 
                    #print(f"Col:{col} \t Row:{row} \t {field[col][row]}\n")
                    corners = []
                    corners.append(field[col][row]) #a
                    corners.append(field[col][row+1]) #b
                    corners.append(field[col+1][row+1]) #c
                    corners.append(field[col+1][row]) #d 
                    print(corners)
                    x = row * resolution
                    y = col * resolution
                    #Calcualte Midpoints for the square 
                    a = pygame.Vector2(x + resolution * 0.5, y                 )
                    b = pygame.Vector2(x + resolution    , y + resolution * 0.5)
                    c = pygame.Vector2(x + resolution * 0.5, y + resolution      )
                    d = pygame.Vector2(x                 , y + resolution * 0.5)
                    #Map  Isoline configurations to draw a specific line 
                    print("-------------------------------------------------------")
                    print(f"{corners[0]} \t {corners[1]} \t {corners[2]} \t {corners[3]}")
                    decimalValue = getBinaryState(corners[0],corners[1],corners[2],corners[3])
                    print(f"{corners[0]} \t {corners[1]} \t {corners[2]} \t {corners[3]}")
                    print("8 \t 4 \t 2 \t 1")
                    print("-------------------------------------------------------")
                    print(decimalValue)
                    print("-------------------------------------------------------")
                    if(decimalValue == 1):
                        pygame.draw.line(screen, BLACK, d,c , 2)
                    elif(decimalValue == 2):
                        pygame.draw.line(screen, BLACK, b,c , 2)
                    elif(decimalValue == 3):
                        pygame.draw.line(screen, BLACK, b,d , 2)
                    elif(decimalValue == 4):
                        pygame.draw.line(screen, BLACK, a,b , 2)
                    elif(decimalValue == 5):
                        pygame.draw.line(screen, BLACK, a,d , 2)
                        pygame.draw.line(screen, BLACK, b,c , 2)
                    elif(decimalValue == 6):
                        pygame.draw.line(screen, BLACK, a,c , 2)
                    elif(decimalValue == 7):
                        pygame.draw.line(screen, BLACK, a,d , 2)
                    elif(decimalValue == 8):
                        pygame.draw.line(screen, BLACK, a,d , 2)
                    elif(decimalValue == 9):
                        pygame.draw.line(screen, BLACK, a,c , 2)
                    elif(decimalValue == 10):
                        pygame.draw.line(screen, BLACK, a,b , 2)
                        pygame.draw.line(screen, BLACK, c,d , 2)
                    elif(decimalValue == 11):
                        pygame.draw.line(screen, BLACK, a,b , 2)
                    elif(decimalValue == 12):
                        pygame.draw.line(screen, BLACK, d,b , 2)
                    elif(decimalValue == 13):
                        pygame.draw.line(screen, BLACK, b,c , 2)
                    elif(decimalValue == 14):
                        pygame.draw.line(screen, BLACK, c,d , 2)
                    elif(decimalValue == 15):
                        pass
    pygame.display.update()        

