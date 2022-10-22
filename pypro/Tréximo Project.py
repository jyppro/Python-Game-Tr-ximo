import pygame
import random
from time import sleep
from pygame.rect import *

#게임 초기화 및 기본 설정
pygame.init()
pad_width = 1200
pad_height = 800
gamepad = pygame.display.set_mode((pad_width, pad_height))
pygame.display.set_caption('tréximo')
WHITE = [255,255,255]
RED = [255, 0, 0]
b = 1
w = 2

t1s = w
t2s = w

item_cnt = 20
item_list1 = []
item_list2 = []
item_list3 = []
item_list4 = []

#스테이지 초기화
stage = 1
m = 0
stagestair = 1500

#플레이어1 캐릭터
if (t1s == b):
    turtle1 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_b.png')
elif (t1s == w):
    turtle1 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_w.png')
    
turtle1_size = turtle1.get_rect().size
turtle1_width = turtle1_size[0]
turtle1_height = turtle1_size[1]

#플레이어2 캐릭터
if (t2s == b):
    turtle2 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_b.png')
elif (t2s == w):
    turtle2 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_w.png')
    
turtle2_size = turtle2.get_rect().size
turtle2_width = turtle2_size[0]
turtle2_height = turtle2_size[1]


#장애물
item1 = pygame.image.load('C:/Users/Master/Desktop/pypro/spear_w.png')
item2 = pygame.image.load('C:/Users/Master/Desktop/pypro/spear_b.png')
item3 = pygame.image.load('C:/Users/Master/Desktop/pypro/fire_w.png')
item4 = pygame.image.load('C:/Users/Master/Desktop/pypro/fire_b.png')

item1_size = item1.get_rect().size
item1_width = item1_size[0]
item1_height = item1_size[1]
item2_size = item2.get_rect().size
item2_width = item2_size[0]
item2_height = item2_size[1]
item3_size = item3.get_rect().size
item3_width = item3_size[0]
item3_height = item3_size[1]
item4_size = item4.get_rect().size
item4_width = item4_size[0]
item4_height = item4_size[1]

#장애물 위치 지정
for i in range(item_cnt):
    x = random.randrange(0, pad_width)
    y = 0 - item1_height
    item_list1.append([x, y])

for i in range(item_cnt):
    x = random.randrange(0, pad_width)
    y = 0 - item2_height
    item_list2.append([x, y])

for i in range(item_cnt):
    x = random.randrange(0, pad_width)
    y = 0 - item3_height
    item_list3.append([x, y])

for i in range(item_cnt):
    x = random.randrange(0, pad_width)
    y = 0 - item4_height
    item_list4.append([x, y])
    
#배경 지정
def back(background, x, y):
    global gamepad
    gamepad.blit(background,(x,y))

def P1(x,y):
    global gamepad, turtle1
    gamepad.blit(turtle1,(x,y))

def P2(a,b):
    global gamepad, turtle2_1
    gamepad.blit(turtle2,(a,b))

def it(item_list1, item_list2, item_list3, item_list4):
    global gamepad
    gamepad.blit(item1,item_list1)
    gamepad.blit(item2,item_list2)
    gamepad.blit(item3,item_list3)
    gamepad.blit(item4,item_list4)


#미터, 스테이지 표시
def draw_m():
    font_01 = pygame.font.SysFont("FixedSsy", 30, True, False)
    text_m = font_01.render(str(m) + "M", True, WHITE)
    gamepad.blit(text_m,[15, 15])

    text_stage = font_01.render("STAGE :" + str(stage), True, WHITE)
    gamepad.blit(text_stage, [600, 15])

def gameover1():
    global gamepad
    dispmessage('1P WIN')

def gameover2():
    global gamepad
    dispmessage('2P WIN')

def textObj(text, font):
    textSurface = font.render(text, True, RED)
    return textSurface


def dispmessage(text):
    global gamepad
    largetext = pygame.font.SysFont("FixedSsy", 120)
    TextSurf = textObj(text, largetext)
    gamepad.blit(TextSurf, [450, 350])
    pygame.display.update()
    sleep(200)
    

#미터 증가
def increse_m():
    global m, stage, stagestair
    
    m += 1
    
    if m >= stagestair:
        stage += 1
        stagestair += 1500
    

def trun():
    global bg1, bg2, bg3, bg4, bg5, bg6, clock, turtle1, turtle2, t1s, t2s

    x = 900
    y = 700
    y_change = 0
    x_change = 0
    a = 200
    b = 700
    a_change = 0
    b_change = 0

    bg1_y = 0
    bg2_y = -pad_height
    bg3_y = 0
    bg4_y = -pad_height
    bg5_y = 0
    bg6_y = -pad_height

    count1 = 1
    count2 = 1
    
    Done = False
    while not Done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_LEFT:
                    x_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    b_change = -5
                elif event.key == pygame.K_s:
                    b_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_s:
                    b_change = 0

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    a_change = 5
                elif event.key == pygame.K_a:
                    a_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == pygame.K_a:
                    a_change = 0

            #거북이 색 바꾸기
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    count1 += 1
                    if (count1 % 2 == 0):
                        turtle1 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_b.png')
                        t1s = b
                    else:
                        turtle1 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_w.png')
                        t1s = w
                            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    count2 += 1
                    if (count2 % 2 == 0):
                        turtle2 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_b.png')
                        t2s = b
                    else:
                        turtle2 = pygame.image.load('C:/Users/Master/Desktop/pypro/turtle_w.png')
                        t2s = w
                        

        for i in range(len(item_list1)):
            item_list1[i][1] += 5

            if item_list1[i][1] >= pad_height:
                item_list1[i][1] = 0 - item1_height
                item_list1[i][0] = random.randrange(0, pad_width)

        for i in range(len(item_list2)):
            item_list2[i][1] += 4

            if item_list2[i][1] >= pad_height:
                item_list2[i][1] = 0 - item2_height
                item_list2[i][0] = random.randrange(0, pad_width)
                
        for i in range(len(item_list3)):
            item_list3[i][1] += 10

            if item_list3[i][1] >= pad_height:
                item_list3[i][1] = 0 - item3_height
                item_list3[i][0] = random.randrange(0, pad_width)

        for i in range(len(item_list4)):
            item_list4[i][1] += 12

            if item_list4[i][1] >= pad_height:
                item_list4[i][1] = 0 - item4_height
                item_list4[i][0] = random.randrange(0, pad_width)
                
        #turtle1
        # 왼쪽으로 벗어나는 것 방지
        if x < 600:
            x = 600

        # 오른쪽으로 벗어나는 것 방지
        if x > pad_width - turtle1_width:
            x = pad_width - turtle1_width

        # 위쪽으로 벗어나는 것 방지
        if y < 0:
            y = 0

        # 아래쪽으로 벗어나는 것 방지
        if y > pad_height - turtle1_height:
            y = pad_height - turtle1_height

        #turtle2
        # 왼쪽으로 벗어나는 것 방지
        if a < 0:
            a = 0

        # 오른쪽으로 벗어나는 것 방지
        if a > 600 - turtle2_width:
            a = 600 - turtle2_width

        # 위쪽으로 벗어나는 것 방지
        if b < 0:
            b = 0

        # 아래쪽으로 벗어나는 것 방지
        if b > pad_height - turtle2_height:
            b = pad_height - turtle2_height

        #거북이 움직임
        y += y_change
        x += x_change

        b += b_change
        a += a_change

        #배경 움직임
        bg1_y += 2
        bg2_y += 2
        bg3_y += 2
        bg4_y += 2
        bg5_y += 2
        bg6_y += 2

        if bg1_y == pad_height:
         bg1_y = -pad_height

        if bg2_y == pad_height:
         bg2_y = -pad_height

        if bg3_y == pad_height:
         bg3_y = -pad_height

        if bg4_y == pad_height:
         bg4_y = -pad_height

        if bg5_y == pad_height:
         bg5_y = -pad_height

        if bg6_y == pad_height:
         bg6_y = -pad_height

        #스테이지 제어
        if (stage % 3 == 1):
            back(bg1, 0, bg1_y)
            back(bg2, 0, bg2_y)
        elif (stage % 3 == 2):
            back(bg3, 0, bg3_y)
            back(bg4, 0, bg4_y)
        elif (stage % 3 == 0):
            back(bg5, 0, bg5_y)
            back(bg6, 0, bg6_y)

        turtle1_rect = turtle1.get_rect()
        turtle1_rect.top = y
        turtle1_rect.left = x
        
        turtle2_rect = turtle2.get_rect()
        turtle2_rect.top = b
        turtle2_rect.left = a

        item1_rect = item1.get_rect()
        item1_rect.top = item_list1[i][1]
        item1_rect.left = item_list1[i][0]
        
        item2_rect = item2.get_rect()
        item2_rect.top = item_list2[i][1]
        item2_rect.left = item_list2[i][0]
        
        item3_rect = item3.get_rect()
        item3_rect.top = item_list3[i][1]
        item3_rect.left = item_list3[i][0]
        
        item4_rect = item4.get_rect()
        item4_rect.top = item_list4[i][1]
        item4_rect.left = item_list4[i][0]

        if (t1s == b):
            if turtle1_rect.colliderect(item1_rect) \
            or turtle1_rect.colliderect(item3_rect):
                gameover2()
        elif (t1s == w):
            if turtle1_rect.colliderect(item2_rect) \
            or turtle1_rect.colliderect(item4_rect):
                gameover2()
                
        if (t2s == b):
            if turtle2_rect.colliderect(item1_rect) \
            or turtle2_rect.colliderect(item3_rect):
                gameover1()
        elif (t2s == w):
            if turtle2_rect.colliderect(item2_rect) \
            or turtle2_rect.colliderect(item4_rect):
                gameover1()
         
        P1(x,y)
        P2(a,b)
        it(item_list1[i], item_list2[i], item_list3[i], item_list4[i])

        increse_m()
        draw_m()
        pygame.display.flip()
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

bg1 = pygame.image.load('C:/Users/Master/Desktop/pypro/bg_forest.jpg')
bg2 = bg1.copy()
bg3 = pygame.image.load('C:/Users/Master/Desktop/pypro/bg_ground.jpg')
bg4 = bg3.copy()
bg5 = pygame.image.load('C:/Users/Master/Desktop/pypro/bg_river.jpg')
bg6 = bg5.copy()

clock = pygame.time.Clock()
trun()

