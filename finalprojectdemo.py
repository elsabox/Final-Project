# 15-112 Fundamentals of Programming and Computer Science: Final Project
# Author: Elizabeth Marella
# AndrewID: emarella
# File Created: 7 Nov, 2017

"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc

 button function code:

 https://www.youtube.com/watch?v=kK4xhHr1QeQ

 menu background:

 http://wallpapershdfre.blogspot.qa/2013/09/simple-plain-hd-desktop-wallpapers.html
 
"""
 
import pygame
 
# Define some colors
black = (0, 0, 0)
grey = (150,150,150)
white= (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

num1_1 = ""
num1_2 = ""
num1_6 = ""
num1_8 = ""
num1_9 = ""
num2_1 = ""
num2_3 = ""
num2_4 = ""
num2_8 = ""
num3_1 = ""
num3_2 = ""
num3_3 = ""
num3_4 = ""
num3_7 = ""
num3_8 = ""
num4_3 = ""
num4_5 = ""
num4_6 = ""
num4_9 = ""
num5_1 = ""
num5_2 = ""
num5_4 = ""
num5_5 = ""
num5_6 = ""
num5_8 = ""
num5_9 = ""
num6_1 = ""
num6_4 = ""
num6_5 = ""
num6_7 = ""
num7_2 = ""
num7_3 = ""
num7_6 = ""
num7_7 = ""
num7_8 = ""
num7_9 = ""
num8_2 = ""
num8_6 = ""
num8_7 = ""
num8_9 = ""
num9_1 = ""
num9_2 = ""
num9_4 = ""
num9_8 = ""
newN = ""
 
pygame.init()
pygame.display.init()

defimg = pygame.image.load("menubackground.jpg")
defimg = pygame.transform.scale(defimg,(550,610))
rect = defimg.get_rect()
 
# Set the width and height of the screen
size = (550, 610)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sudoku")
 
# variables for the main loops
done = False
freeOps = False
timedOps = False
inst = False
scores = False
easy = False
med = False
hard = False
slct = False

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",25)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w/2)),(y + (h/2)))
    screen.blit(textSurf,textRect)
    return msg

def changeNum(x,y,w,h):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    one = pygame.key.get_pressed()[pygame.K_1]
    two = pygame.key.get_pressed()[pygame.K_2]
    three = pygame.key.get_pressed()[pygame.K_3]
    four = pygame.key.get_pressed()[pygame.K_4]
    five = pygame.key.get_pressed()[pygame.K_5]
    six = pygame.key.get_pressed()[pygame.K_6]
    seven = pygame.key.get_pressed()[pygame.K_7]
    eight = pygame.key.get_pressed()[pygame.K_8]
    nine = pygame.key.get_pressed()[pygame.K_9]
    delete = pygame.key.get_pressed()[pygame.K_BACKSPACE]
    if x+w > mouse[0] > x and y+h > mouse[1] > y and one == 1:
        newN = "1"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and two == 1:
        newN = "2"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and three == 1:
        newN = "3"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and four == 1:
        newN = "4"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and five == 1:
        newN = "5"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and six == 1:
        newN = "6"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and seven == 1:
        newN = "7"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and eight == 1:
        newN = "8"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and nine == 1:
        newN = "9"
        return newN
    elif x+w > mouse[0] > x and y+h > mouse[1] > y and delete == 1:
        newN = ""
        return newN
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # when the exit button is pressed
        if 200+150 > mouse[0] > 200 and 300+50 > mouse[1] > 300 and click[0] == 1:
            done = True
        # when the free play button is pressed
        if 100+150 > mouse[0] > 100 and 160+50 > mouse[1] > 160 and click[0] == 1:
            freeOps = True
            while freeOps:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        freeOps = False
                        done = True
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    # when back key is pressed
                    if 200+150 > mouse[0] > 200 and 440+50 > mouse[1] > 440 and click[0] == 1:
                        freeOps = False
                    # when easy button is pressed
                    if 200+150 > mouse[0] > 200 and 160+50 > mouse[1] > 160 and click[0] == 1:
                        easy = True
                        while easy:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    easy = False
                                    freeOps = False
                                    done = True
                                mouse = pygame.mouse.get_pos()
                                click = pygame.mouse.get_pressed()
                                one = pygame.key.get_pressed()[pygame.K_1]
                                two = pygame.key.get_pressed()[pygame.K_2]
                                three = pygame.key.get_pressed()[pygame.K_3]
                                four = pygame.key.get_pressed()[pygame.K_4]
                                five = pygame.key.get_pressed()[pygame.K_5]
                                six = pygame.key.get_pressed()[pygame.K_6]
                                seven = pygame.key.get_pressed()[pygame.K_7]
                                eight = pygame.key.get_pressed()[pygame.K_8]
                                nine = pygame.key.get_pressed()[pygame.K_9]
                                delete = pygame.key.get_pressed()[pygame.K_BACKSPACE]
                                
                                #box1_2
                                if 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and one == 1:
                                    num1_2 = "1"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and two == 1:
                                    num1_2 = "2"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and three == 1:
                                    num1_2 = "3"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and four == 1:
                                    num1_2 = "4"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and five == 1:
                                    num1_2 = "5"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and six == 1:
                                    num1_2 = "6"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and seven == 1:
                                    num1_2 = "7"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and eight == 1:
                                    num1_2 = "8"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and nine == 1:
                                    num1_2 = "9"
                                elif 85+50 > mouse[0] > 50 and 50+50 > mouse[1] > 50 and delete == 1:
                                    num1_2 = ""
                                    
                                # box1_6
                                if 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and one == 1:
                                    num1_6 = "1"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and two == 1:
                                    num1_6 = "2"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and three == 1:
                                    num1_6 = "3"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and four == 1:
                                    num1_6 = "4"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and five == 1:
                                    num1_6 = "5"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and six == 1:
                                    num1_6 = "6"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and seven == 1:
                                    num1_6 = "7"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and eight == 1:
                                    num1_6 = "8"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and nine == 1:
                                    num1_6 = "9"
                                elif 305+50 > mouse[0] > 305 and 50+50 > mouse[1] > 50 and delete == 1:
                                    num1_6 = ""

                                # box1_8
                                if 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and one == 1:
                                    num1_8 = "1"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and two == 1:
                                    num1_8 = "2"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and three == 1:
                                    num1_8 = "3"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and four == 1:
                                    num1_8 = "4"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and five == 1:
                                    num1_8 = "5"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and six == 1:
                                    num1_8 = "6"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and seven == 1:
                                    num1_8 = "7"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and eight == 1:
                                    num1_8 = "8"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and nine == 1:
                                    num1_8 = "9"
                                elif 415+50 > mouse[0] > 415 and 50+50 > mouse[1] > 50 and delete == 1:
                                    num1_8 = ""

                                # box1_9
                                if 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and one == 1:
                                    num1_9 = "1"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and two == 1:
                                    num1_9 = "2"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and three == 1:
                                    num1_9 = "3"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and four == 1:
                                    num1_9 = "4"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and five == 1:
                                    num1_9 = "5"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and six == 1:
                                    num1_9 = "6"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and seven == 1:
                                    num1_9 = "7"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and eight == 1:
                                    num1_9 = "8"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and nine == 1:
                                    num1_9 = "9"
                                elif 470+50 > mouse[0] > 470 and 50+50 > mouse[1] > 50 and delete == 1:
                                    num1_9 = ""

                                # box2_1
                                if 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and one == 1:
                                    num2_1 = "1"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and two == 1:
                                    num2_1 = "2"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and three == 1:
                                    num2_1 = "3"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and four == 1:
                                    num2_1 = "4"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and five == 1:
                                    num2_1 = "5"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and six == 1:
                                    num2_1 = "6"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and seven == 1:
                                    num2_1 = "7"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and eight == 1:
                                    num2_1 = "8"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and nine == 1:
                                    num2_1 = "9"
                                elif 30+50 > mouse[0] > 30 and 105+50 > mouse[1] > 105 and delete == 1:
                                    num2_1 = ""

                                # box2_3
                                if 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and one == 1:
                                    num2_3 = "1"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and two == 1:
                                    num2_3 = "2"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and three == 1:
                                    num2_3 = "3"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and four == 1:
                                    num2_3 = "4"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and five == 1:
                                    num2_3 = "5"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and six == 1:
                                    num2_3 = "6"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and seven == 1:
                                    num2_3 = "7"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and eight == 1:
                                    num2_3 = "8"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and nine == 1:
                                    num2_3 = "9"
                                elif 140+50 > mouse[0] > 140 and 105+50 > mouse[1] > 105 and delete == 1:
                                    num2_3 = ""

                                # box2_4
                                if 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and one == 1:
                                    num2_4 = "1"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and two == 1:
                                    num2_4 = "2"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and three == 1:
                                    num2_4 = "3"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and four == 1:
                                    num2_4 = "4"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and five == 1:
                                    num2_4 = "5"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and six == 1:
                                    num2_4 = "6"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and seven == 1:
                                    num2_4 = "7"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and eight == 1:
                                    num2_4 = "8"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and nine == 1:
                                    num2_4 = "9"
                                elif 195+50 > mouse[0] > 195 and 105+50 > mouse[1] > 105 and delete == 1:
                                    num2_4 = ""

                                # box2_8
                                if 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and one == 1:
                                    num2_8 = "1"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and two == 1:
                                    num2_8 = "2"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and three == 1:
                                    num2_8 = "3"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and four == 1:
                                    num2_8 = "4"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and five == 1:
                                    num2_8 = "5"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and six == 1:
                                    num2_8 = "6"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and seven == 1:
                                    num2_8 = "7"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and eight == 1:
                                    num2_8 = "8"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and nine == 1:
                                    num2_8 = "9"
                                elif 415+50 > mouse[0] > 415 and 105+50 > mouse[1] > 105 and delete == 1:
                                    num2_8 = ""

                                # box3_3
                                if 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_3 = "1"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_3 = "2"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_3 = "3"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_3 = "4"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_3 = "5"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_3 = "6"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_3 = "7"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_3 = "8"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_3 = "9"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_3 = ""

                                # box3_1
                                if 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_1 = "1"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_1 = "2"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_1 = "3"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_1 = "4"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_1 = "5"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_1 = "6"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_1 = "7"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_1 = "8"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_1 = "9"
                                elif 30+50 > mouse[0] > 30 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_1 = ""

                                # box3_2
                                if 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_2 = "1"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_2 = "2"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_2 = "3"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_2 = "4"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_2 = "5"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_2 = "6"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_2 = "7"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_2 = "8"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_2 = "9"
                                elif 85+50 > mouse[0] > 85 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_2 = ""

                                # box3_3
                                if 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_3 = "1"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_3 = "2"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_3 = "3"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_3 = "4"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_3 = "5"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_3 = "6"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_3 = "7"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_3 = "8"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_3 = "9"
                                elif 140+50 > mouse[0] > 140 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_3 = ""

                                # box3_4
                                if 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_4 = "1"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_4 = "2"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_4 = "3"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_4 = "4"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_4 = "5"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_4 = "6"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_4 = "7"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_4 = "8"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_4 = "9"
                                elif 195+50 > mouse[0] > 195 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_4 = ""

                                # box3_7
                                if 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_7 = "1"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_7 = "2"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_7 = "3"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_7 = "4"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_7 = "5"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_7 = "6"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_7 = "7"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_7 = "8"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_7 = "9"
                                elif 360+50 > mouse[0] > 360 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_7 = ""

                                # box3_8
                                if 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and one == 1:
                                    num3_8 = "1"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and two == 1:
                                    num3_8 = "2"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and three == 1:
                                    num3_8 = "3"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and four == 1:
                                    num3_8 = "4"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and five == 1:
                                    num3_8 = "5"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and six == 1:
                                    num3_8 = "6"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and seven == 1:
                                    num3_8 = "7"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and eight == 1:
                                    num3_8 = "8"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and nine == 1:
                                    num3_8 = "9"
                                elif 415+50 > mouse[0] > 415 and 160+50 > mouse[1] > 160 and delete == 1:
                                    num3_8 = ""

                                # box4_3
                                if 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and one == 1:
                                    num4_3 = "1"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and two == 1:
                                    num4_3 = "2"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and three == 1:
                                    num4_3 = "3"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and four == 1:
                                    num4_3 = "4"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and five == 1:
                                    num4_3 = "5"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and six == 1:
                                    num4_3 = "6"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and seven == 1:
                                    num4_3 = "7"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and eight == 1:
                                    num4_3 = "8"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and nine == 1:
                                    num4_3 = "9"
                                elif 140+50 > mouse[0] > 140 and 215+50 > mouse[1] > 215 and delete == 1:
                                    num4_3 = ""

                                # box4_5
                                if 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and one == 1:
                                    num4_5 = "1"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and two == 1:
                                    num4_5 = "2"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and three == 1:
                                    num4_5 = "3"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and four == 1:
                                    num4_5 = "4"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and five == 1:
                                    num4_5 = "5"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and six == 1:
                                    num4_5 = "6"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and seven == 1:
                                    num4_5 = "7"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and eight == 1:
                                    num4_5 = "8"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and nine == 1:
                                    num4_5 = "9"
                                elif 250+50 > mouse[0] > 250 and 215+50 > mouse[1] > 215 and delete == 1:
                                    num4_5 = ""

                                # box4_6
                                if 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and one == 1:
                                    num4_6 = "1"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and two == 1:
                                    num4_6 = "2"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and three == 1:
                                    num4_6 = "3"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and four == 1:
                                    num4_6 = "4"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and five == 1:
                                    num4_6 = "5"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and six == 1:
                                    num4_6 = "6"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and seven == 1:
                                    num4_6 = "7"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and eight == 1:
                                    num4_6 = "8"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and nine == 1:
                                    num4_6 = "9"
                                elif 305+50 > mouse[0] > 305 and 215+50 > mouse[1] > 215 and delete == 1:
                                    num4_6 = ""

                                # box4_9
                                if 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and one == 1:
                                    num4_9 = "1"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and two == 1:
                                    num4_9 = "2"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and three == 1:
                                    num4_9 = "3"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and four == 1:
                                    num4_9 = "4"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and five == 1:
                                    num4_9 = "5"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and six == 1:
                                    num4_9 = "6"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and seven == 1:
                                    num4_9 = "7"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and eight == 1:
                                    num4_9 = "8"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and nine == 1:
                                    num4_9 = "9"
                                elif 470+50 > mouse[0] > 470 and 215+50 > mouse[1] > 215 and delete == 1:
                                    num4_9 = ""

                                # box5_1
                                if 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_1 = "1"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_1 = "2"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_1 = "3"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_1 = "4"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_1 = "5"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_1 = "6"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_1 = "7"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_1 = "8"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_1 = "9"
                                elif 30+50 > mouse[0] > 30 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_1 = ""

                                # box5_2
                                if 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_2 = "1"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_2 = "2"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_2 = "3"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_2 = "4"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_2 = "5"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_2 = "6"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_2 = "7"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_2 = "8"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_2 = "9"
                                elif 85+50 > mouse[0] > 85 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_2 = ""

                                # box5_4
                                if 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_4 = "1"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_4 = "2"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_4 = "3"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_4 = "4"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_4 = "5"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_4 = "6"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_4 = "7"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_4 = "8"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_4 = "9"
                                elif 195+50 > mouse[0] > 195 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_4 = ""

                                # box5_5
                                if 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_5 = "1"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_5 = "2"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_5 = "3"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_5 = "4"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_5 = "5"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_5 = "6"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_5 = "7"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_5 = "8"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_5 = "9"
                                elif 250+50 > mouse[0] > 250 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_5 = ""

                                # box5_6
                                if 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_6 = "1"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_6 = "2"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_6 = "3"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_6 = "4"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_6 = "5"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_6 = "6"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_6 = "7"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_6 = "8"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_6 = "9"
                                elif 305+50 > mouse[0] > 305 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_6 = ""

                                # box5_8
                                if 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_8 = "1"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_8 = "2"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_8 = "3"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_8 = "4"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_8 = "5"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_8 = "6"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_8 = "7"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_8 = "8"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_8 = "9"
                                elif 415+50 > mouse[0] > 415 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_8 = ""

                                # box5_9
                                if 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and one == 1:
                                    num5_9 = "1"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and two == 1:
                                    num5_9 = "2"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and three == 1:
                                    num5_9 = "3"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and four == 1:
                                    num5_9 = "4"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and five == 1:
                                    num5_9 = "5"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and six == 1:
                                    num5_9 = "6"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and seven == 1:
                                    num5_9 = "7"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and eight == 1:
                                    num5_9 = "8"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and nine == 1:
                                    num5_9 = "9"
                                elif 470+50 > mouse[0] > 470 and 270+50 > mouse[1] > 270 and delete == 1:
                                    num5_9 = ""

                                # box6_1
                                if 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and one == 1:
                                    num6_1 = "1"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and two == 1:
                                    num6_1 = "2"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and three == 1:
                                    num6_1 = "3"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and four == 1:
                                    num6_1 = "4"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and five == 1:
                                    num6_1 = "5"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and six == 1:
                                    num6_1 = "6"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and seven == 1:
                                    num6_1 = "7"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and eight == 1:
                                    num6_1 = "8"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and nine == 1:
                                    num6_1 = "9"
                                elif 30+50 > mouse[0] > 30 and 325+50 > mouse[1] > 325 and delete == 1:
                                    num6_1 = ""

                                # box6_4
                                if 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and one == 1:
                                    num6_4 = "1"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and two == 1:
                                    num6_4 = "2"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and three == 1:
                                    num6_4 = "3"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and four == 1:
                                    num6_4 = "4"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and five == 1:
                                    num6_4 = "5"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and six == 1:
                                    num6_4 = "6"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and seven == 1:
                                    num6_4 = "7"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and eight == 1:
                                    num6_4 = "8"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and nine == 1:
                                    num6_4 = "9"
                                elif 195+50 > mouse[0] > 195 and 325+50 > mouse[1] > 325 and delete == 1:
                                    num6_4 = ""

                                # box6_5
                                if 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and one == 1:
                                    num6_5 = "1"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and two == 1:
                                    num6_5 = "2"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and three == 1:
                                    num6_5 = "3"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and four == 1:
                                    num6_5 = "4"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and five == 1:
                                    num6_5 = "5"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and six == 1:
                                    num6_5 = "6"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and seven == 1:
                                    num6_5 = "7"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and eight == 1:
                                    num6_5 = "8"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and nine == 1:
                                    num6_5 = "9"
                                elif 250+50 > mouse[0] > 250 and 325+50 > mouse[1] > 325 and delete == 1:
                                    num6_5 = ""

                                # box6_7
                                if 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and one == 1:
                                    num6_7 = "1"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and two == 1:
                                    num6_7 = "2"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and three == 1:
                                    num6_7 = "3"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and four == 1:
                                    num6_7 = "4"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and five == 1:
                                    num6_7 = "5"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and six == 1:
                                    num6_7 = "6"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and seven == 1:
                                    num6_7 = "7"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and eight == 1:
                                    num6_7 = "8"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and nine == 1:
                                    num6_7 = "9"
                                elif 360+50 > mouse[0] > 360 and 325+50 > mouse[1] > 325 and delete == 1:
                                    num6_7 = ""

                                # box7_2
                                if 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and one == 1:
                                    num7_2 = "1"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and two == 1:
                                    num7_2 = "2"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and three == 1:
                                    num7_2 = "3"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and four == 1:
                                    num7_2 = "4"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and five == 1:
                                    num7_2 = "5"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and six == 1:
                                    num7_2 = "6"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and seven == 1:
                                    num7_2 = "7"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and eight == 1:
                                    num7_2 = "8"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and nine == 1:
                                    num7_2 = "9"
                                elif 85+50 > mouse[0] > 85 and 380+50 > mouse[1] > 380 and delete == 1:
                                    num7_2 = ""

                                # box7_3
                                if 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and one == 1:
                                    num7_3 = "1"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and two == 1:
                                    num7_3 = "2"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and three == 1:
                                    num7_3 = "3"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and four == 1:
                                    num7_3 = "4"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and five == 1:
                                    num7_3 = "5"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and six == 1:
                                    num7_3 = "6"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and seven == 1:
                                    num7_3 = "7"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and eight == 1:
                                    num7_3 = "8"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and nine == 1:
                                    num7_3 = "9"
                                elif 140+50 > mouse[0] > 140 and 380+50 > mouse[1] > 380 and delete == 1:
                                    num7_3 = ""

                                # box7_6
                                if 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and one == 1:
                                    num7_6 = "1"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and two == 1:
                                    num7_6 = "2"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and three == 1:
                                    num7_6 = "3"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and four == 1:
                                    num7_6 = "4"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and five == 1:
                                    num7_6 = "5"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and six == 1:
                                    num7_6 = "6"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and seven == 1:
                                    num7_6 = "7"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and eight == 1:
                                    num7_6 = "8"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and nine == 1:
                                    num7_6 = "9"
                                elif 305+50 > mouse[0] > 305 and 380+50 > mouse[1] > 380 and delete == 1:
                                    num7_6 = ""

                                # box7_7
                                if 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and one == 1:
                                    num7_7 = "1"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and two == 1:
                                    num7_7 = "2"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and three == 1:
                                    num7_7 = "3"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and four == 1:
                                    num7_7 = "4"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and five == 1:
                                    num7_7 = "5"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and six == 1:
                                    num7_7 = "6"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and seven == 1:
                                    num7_7 = "7"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and eight == 1:
                                    num7_7 = "8"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and nine == 1:
                                    num7_7 = "9"
                                elif 360+50 > mouse[0] > 360 and 380+50 > mouse[1] > 380 and delete == 1:
                                    num7_7 = ""

                                # box7_8
                                if 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and one == 1:
                                    num7_8 = "1"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and two == 1:
                                    num7_8 = "2"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and three == 1:
                                    num7_8 = "3"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and four == 1:
                                    num7_8 = "4"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and five == 1:
                                    num7_8 = "5"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and six == 1:
                                    num7_8 = "6"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and seven == 1:
                                    num7_8 = "7"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and eight == 1:
                                    num7_8 = "8"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and nine == 1:
                                    num7_8 = "9"
                                elif 415+50 > mouse[0] > 415 and 380+50 > mouse[1] > 380 and delete == 1:
                                    num7_8 = ""

                                # box7_9
                                if 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and one == 1:
                                    num7_9 = "1"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and two == 1:
                                    num7_9 = "2"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and three == 1:
                                    num7_9 = "3"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and four == 1:
                                    num7_9 = "4"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and five == 1:
                                    num7_9 = "5"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and six == 1:
                                    num7_9 = "6"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and seven == 1:
                                    num7_9 = "7"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and eight == 1:
                                    num7_9 = "8"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and nine == 1:
                                    num7_9 = "9"
                                elif 470+50 > mouse[0] > 470 and 380+50 > mouse[1] > 380 and delete == 1:
                                    num7_9 = ""

                                # box8_2
                                if 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and one == 1:
                                    num8_2 = "1"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and two == 1:
                                    num8_2 = "2"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and three == 1:
                                    num8_2 = "3"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and four == 1:
                                    num8_2 = "4"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and five == 1:
                                    num8_2 = "5"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and six == 1:
                                    num8_2 = "6"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and seven == 1:
                                    num8_2 = "7"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and eight == 1:
                                    num8_2 = "8"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and nine == 1:
                                    num8_2 = "9"
                                elif 85+50 > mouse[0] > 85 and 435+50 > mouse[1] > 435 and delete == 1:
                                    num8_2 = ""

                                # box8_6
                                if 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and one == 1:
                                    num8_6 = "1"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and two == 1:
                                    num8_6 = "2"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and three == 1:
                                    num8_6 = "3"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and four == 1:
                                    num8_6 = "4"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and five == 1:
                                    num8_6 = "5"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and six == 1:
                                    num8_6 = "6"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and seven == 1:
                                    num8_6 = "7"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and eight == 1:
                                    num8_6 = "8"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and nine == 1:
                                    num8_6 = "9"
                                elif 305+50 > mouse[0] > 305 and 435+50 > mouse[1] > 435 and delete == 1:
                                    num8_6 = ""

                                # box8_7
                                if 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and one == 1:
                                    num8_7 = "1"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and two == 1:
                                    num8_7 = "2"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and three == 1:
                                    num8_7 = "3"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and four == 1:
                                    num8_7 = "4"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and five == 1:
                                    num8_7 = "5"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and six == 1:
                                    num8_7 = "6"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and seven == 1:
                                    num8_7 = "7"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and eight == 1:
                                    num8_7 = "8"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and nine == 1:
                                    num8_7 = "9"
                                elif 360+50 > mouse[0] > 360 and 435+50 > mouse[1] > 435 and delete == 1:
                                    num8_7 = ""

                                # box8_9
                                if 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and one == 1:
                                    num8_9 = "1"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and two == 1:
                                    num8_9 = "2"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and three == 1:
                                    num8_9 = "3"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and four == 1:
                                    num8_9 = "4"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and five == 1:
                                    num8_9 = "5"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and six == 1:
                                    num8_9 = "6"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and seven == 1:
                                    num8_9 = "7"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and eight == 1:
                                    num8_9 = "8"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and nine == 1:
                                    num8_9 = "9"
                                elif 470+50 > mouse[0] > 470 and 435+50 > mouse[1] > 435 and delete == 1:
                                    num8_9 = ""

                                # box9_1
                                if 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and one == 1:
                                    num9_1 = "1"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and two == 1:
                                    num9_1 = "2"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and three == 1:
                                    num9_1 = "3"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and four == 1:
                                    num9_1 = "4"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and five == 1:
                                    num9_1 = "5"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and six == 1:
                                    num9_1 = "6"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and seven == 1:
                                    num9_1 = "7"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and eight == 1:
                                    num9_1 = "8"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and nine == 1:
                                    num9_1 = "9"
                                elif 30+50 > mouse[0] > 30 and 490+50 > mouse[1] > 490 and delete == 1:
                                    num9_1 = ""

                                # box9_2
                                if 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and one == 1:
                                    num9_2 = "1"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and two == 1:
                                    num9_2 = "2"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and three == 1:
                                    num9_2 = "3"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and four == 1:
                                    num9_2 = "4"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and five == 1:
                                    num9_2 = "5"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and six == 1:
                                    num9_2 = "6"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and seven == 1:
                                    num9_2 = "7"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and eight == 1:
                                    num9_2 = "8"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and nine == 1:
                                    num9_2 = "9"
                                elif 85+50 > mouse[0] > 85 and 490+50 > mouse[1] > 490 and delete == 1:
                                    num9_2 = ""

                                # box9_4
                                if 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and one == 1:
                                    num9_4 = "1"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and two == 1:
                                    num9_4 = "2"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and three == 1:
                                    num9_4 = "3"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and four == 1:
                                    num9_4 = "4"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and five == 1:
                                    num9_4 = "5"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and six == 1:
                                    num9_4 = "6"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and seven == 1:
                                    num9_4 = "7"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and eight == 1:
                                    num9_4 = "8"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and nine == 1:
                                    num9_4 = "9"
                                elif 195+50 > mouse[0] > 195 and 490+50 > mouse[1] > 490 and delete == 1:
                                    num9_4 = ""

                                # box9_8
                                if 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and one == 1:
                                    num9_8 = "1"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and two == 1:
                                    num9_8 = "2"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and three == 1:
                                    num9_8 = "3"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and four == 1:
                                    num9_8 = "4"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and five == 1:
                                    num9_8 = "5"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and six == 1:
                                    num9_8 = "6"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and seven == 1:
                                    num9_8 = "7"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and eight == 1:
                                    num9_8 = "8"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and nine == 1:
                                    num9_8 = "9"
                                elif 415+50 > mouse[0] > 415 and 490+50 > mouse[1] > 490 and delete == 1:
                                    num9_8 = ""
                                    
                            screen.blit(defimg,rect)

                            midText = pygame.font.Font("freesansbold.ttf",20)
                            textSurf, textRect = text_objects("Easy", midText)
                            textRect.center = (size[0]/2,25)
                            screen.blit(textSurf, textRect)
                            
                            # ROW 1
                            box1_1 = button("4",30,50,50,50,white,white)
                            box1_2 = button(num1_2,85,50,50,50,white,grey)
                            box1_3 = button("3",140,50,50,50,white,white)
                            box1_4 = button("8",195,50,50,50,white,white)
                            box1_5 = button("2",250,50,50,50,white,white)
                            box1_6 = button(num1_6,305,50,50,50,white,grey)
                            box1_7 = button("6",360,50,50,50,white,white)
                            box1_8 = button(num1_8,415,50,50,50,white,grey)
                            box1_9 = button(num1_9,470,50,50,50,white,grey)
                            # ROW 2
                            box2_1 = button(num2_1,30,105,50,50,white,grey)
                            box2_2 = button("9",85,105,50,50,white,white)
                            box2_3 = button(num2_3,140,105,50,50,white,grey)
                            box2_4 = button(num2_4,195,105,50,50,white,grey)
                            box2_5 = button("3",250,105,50,50,white,white)
                            box2_6 = button("7",305,105,50,50,white,white)
                            box2_7 = button("2",360,105,50,50,white,white)
                            box2_8 = button(num2_8,415,105,50,50,white,grey)
                            box2_9 = button("1",470,105,50,50,white,white)
                            # ROW 3
                            box3_1 = button(num3_1,30,160,50,50,white,grey)
                            box3_2 = button(num3_2,85,160,50,50,white,grey)
                            box3_3 = button(num3_3,140,160,50,50,white,grey)
                            box3_4 = button(num3_4,195,160,50,50,white,grey)
                            box3_5 = button("6",250,160,50,50,white,white)
                            box3_6 = button("5",305,160,50,50,white,white)
                            box3_7 = button(num3_7,360,160,50,50,white,grey)
                            box3_8 = button(num3_8,415,160,50,50,white,grey)
                            box3_9 = button("4",470,160,50,50,white,white)
                            # ROW 4
                            box4_1 = button("9",30,215,50,50,white,white)
                            box4_2 = button("6",85,215,50,50,white,white)
                            box4_3 = button(num4_3,140,215,50,50,white,grey)
                            box4_4 = button("2",195,215,50,50,white,white)
                            box4_5 = button(num4_5,250,215,50,50,white,grey)
                            box4_6 = button(num4_6,305,215,50,50,white,grey)
                            box4_7 = button("5",360,215,50,50,white,white)
                            box4_8 = button("4",415,215,50,50,white,white)
                            box4_9 = button(num4_9,470,215,50,50,white,grey)
                            # ROW 5
                            box5_1 = button(num5_1,30,270,50,50,white,grey)
                            box5_2 = button(num5_2,85,270,50,50,white,grey)
                            box5_3 = button("1",140,270,50,50,white,white)
                            box5_4 = button(num5_4,195,270,50,50,white,grey)
                            box5_5 = button(num5_5,250,270,50,50,white,grey)
                            box5_6 = button(num5_6,305,270,50,50,white,grey)
                            box5_7 = button("8",360,270,50,50,white,white)
                            box5_8 = button(num5_8,415,270,50,50,white,grey)
                            box5_9 = button(num5_9,470,270,50,50,white,grey)
                            # ROW 6
                            box6_1 = button(num6_1,30,325,50,50,white,grey)
                            box6_2 = button("5",85,325,50,50,white,white)
                            box6_3 = button("4",140,325,50,50,white,white)
                            box6_4 = button(num6_4,195,325,50,50,white,grey)
                            box6_5 = button(num6_5,250,325,50,50,white,grey)
                            box6_6 = button("3",305,325,50,50,white,white)
                            box6_7 = button(num6_7,360,325,50,50,white,grey)
                            box6_8 = button("1",415,325,50,50,white,white)
                            box6_9 = button("2",470,325,50,50,white,white)
                            # ROW 7
                            box7_1 = button("6",30,380,50,50,white,white)
                            box7_2 = button(num7_2,85,380,50,50,white,grey)
                            box7_3 = button(num7_3,140,380,50,50,white,grey)
                            box7_4 = button("7",195,380,50,50,white,white)
                            box7_5 = button("4",250,380,50,50,white,white)
                            box7_6 = button(num7_6,305,380,50,50,white,grey)
                            box7_7 = button(num7_7,360,380,50,50,white,grey)
                            box7_8 = button(num7_8,415,380,50,50,white,grey)
                            box7_9 = button(num7_9,470,380,50,50,white,grey)
                            # ROW 8
                            box8_1 = button("3",30,435,50,50,white,white)
                            box8_2 = button(num8_2,85,435,50,50,white,grey)
                            box8_3 = button("2",140,435,50,50,white,white)
                            box8_4 = button("5",195,435,50,50,white,white)
                            box8_5 = button("9",250,435,50,50,white,white)
                            box8_6 = button(num8_6,305,435,50,50,white,grey)
                            box8_7 = button(num8_7,360,435,50,50,white,grey)
                            box8_8 = button("6",415,435,50,50,white,white)
                            box8_9 = button(num8_9,470,435,50,50,white,grey)
                            # ROW 9
                            box9_1 = button(num9_1,30,490,50,50,white,grey)
                            box9_2 = button(num9_2,85,490,50,50,white,grey)
                            box9_3 = button("5",140,490,50,50,white,white)
                            box9_4 = button(num9_4,195,490,50,50,white,grey)
                            box9_5 = button("8",250,490,50,50,white,white)
                            box9_6 = button("6",305,490,50,50,white,white)
                            box9_7 = button("7",360,490,50,50,white,white)
                            box9_8 = button(num9_8,415,490,50,50,white,grey)
                            box9_9 = button("9",470,490,50,50,white,white)

                            pygame.draw.line(screen,black,(192,50),(192,540),5)
                            pygame.draw.line(screen,black,(357,50),(357,540),5)
                            pygame.draw.line(screen,black,(30,212),(520,212),5)
                            pygame.draw.line(screen,black,(30,377),(520,377),5)
                            
                            pygame.display.flip()
                            clock.tick(50)
            
                    # when medium button is pressed
                    if 200+150 > mouse[0] > 200 and 230+50 > mouse[1] > 230 and click[0] == 1:
                        medium = True

                    # when hard button is pressed
                    if 200+150 > mouse[0] > 200 and 300+50 > mouse[1] > 300 and click[0] == 1:
                        hard = True
                    # when load game button is pressed
                    if 200+150 > mouse[0] > 200 and 370+50 > mouse[1] > 370 and click[0] == 1:
                        freeOps = True
                screen.blit(defimg,rect)
                midText = pygame.font.Font("freesansbold.ttf",60)
                textSurf, textRect = text_objects("Sudoku", midText)
                textRect.center = (size[0]/2,(size[1]/2)-200)
                screen.blit(textSurf, textRect)
    
                button("Easy",200,160,150,50,white,grey)
                button("Medium",200,230,150,50,white,grey)
                button("Hard",200,300,150,50,white,grey)
                button("Load Game",200,370,150,50,white,grey)
                button("Back",200,440,150,50,white,grey)
    
                pygame.display.flip()
                clock.tick(50)
        # when the timed play button is pressed
        if 100+150 > mouse[0] > 100 and 230+50 > mouse[1] > 230 and click[0] == 1:
            timedOps = True
            while timedOps:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        timedOps = False
                        done = True
                    mouse = pygame.mouse.get_pos()
                    click = pygame.mouse.get_pressed()
                    if 200+150 > mouse[0] > 200 and 440+50 > mouse[1] > 440 and click[0] == 1:
                        timedOps = False
                screen.blit(defimg,rect)
                midText = pygame.font.Font("freesansbold.ttf",60)
                textSurf, textRect = text_objects("Sudoku", midText)
                textRect.center = (size[0]/2,(size[1]/2)-200)
                screen.blit(textSurf, textRect)
    
                button("Easy",200,160,150,50,white,grey)
                button("Medium",200,230,150,50,white,grey)
                button("Hard",200,300,150,50,white,grey)
                button("Load Game",200,370,150,50,white,grey)
                button("Back",200,440,150,50,white,grey)
    
                pygame.display.flip()
                clock.tick(50)
        # when the instructions button is pressed
        if 300+150 > mouse[0] > 300 and 160+50 > mouse[1] > 160 and click[0] == 1:
            inst = True
        # when the high scores button is pressed
        if 300+150 > mouse[0] > 300 and 230+50 > mouse[1] > 230 and click[0] == 1:
            scores = True
            
    # puts the background image
    screen.blit(defimg,rect)
 
    midText = pygame.font.Font("freesansbold.ttf",60)
    textSurf, textRect = text_objects("Sudoku", midText)
    textRect.center = (size[0]/2,(size[1]/2)-200)
    screen.blit(textSurf, textRect)
    
    button("Free Play",100,160,150,50,white,grey)
    button("Timed Play",100,230,150,50,white,grey)
    button("Instructions",300,160,150,50,white,grey)
    button("High Scores",300,230,150,50,white,grey)
    button("Exit",200,300,150,50,white,grey)
    
    
    # update the screen
    pygame.display.flip()
 
    clock.tick(50)
 
# Close the window and quit.
pygame.quit()
















