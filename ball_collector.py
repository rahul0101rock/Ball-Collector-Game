import pygame
from pygame import *

pygame.init()
xmax,ymax = 640,480
screen = pygame.display.set_mode((xmax,ymax))
clock = pygame.time.Clock()

background = pygame.image.load('assets/background.png').convert()
gameover = pygame.image.load('assets/game_over.png').convert()

ballth = pygame.image.load('assets/ball_thrower.png').convert()
ballth.set_alpha(200)
xballth = ballth.get_height()
yballth = ballth.get_width()

ball1 = pygame.image.load('assets/ball1.png').convert()
xball1 = ball1.get_height()
yball1 = ball1.get_width()

ball2 = pygame.image.load('assets/ball2.png').convert()
xball2 = ball2.get_height()
yball2 = ball2.get_width()

ball3 = pygame.image.load('assets/ball3.png').convert()
xball3 = ball3.get_height()
yball3 = ball3.get_width()

ball4 = pygame.image.load('assets/ball4.png').convert()
xball4 = ball4.get_height()
yball4 = ball4.get_width()

ball5 = pygame.image.load('assets/ball5.png').convert()
xball5 = ball5.get_height()
yball5 = ball5.get_width()

# [ x, y, step_x, step_y, height, width, surface, rect]

ball1_list = [100,200,1,1, xball5, yball5, ball5, pygame.Rect((100,200),(xball5,yball5))]
ball2_list = [100,200,1,1, xball2, yball2, ball2, pygame.Rect((100,200),(xball2,yball2))]
ball3_list = [100,200,1,1, xball3, yball3, ball3, pygame.Rect((100,200),(xball3,yball3))]
ball4_list = [100,200,1,1, xball4, yball4, ball4, pygame.Rect((100,200),(xball4,yball4))]
ball5_list = [100,200,-1,-1, xball1, yball1, ball1, pygame.Rect((100,200),(xball1,yball1))]

balls_dict = {'1':ball1_list, '2':ball2_list, '3':ball3_list, '4':ball4_list, 'special ball':ball5_list}

el_dict = {'ball1':ball4_list, 'special ball': ball5_list}

n,n_ball,tp_ball,level,t = 1,1,1,1,2000
seconds,points,catched,hsc = 0,0,0,0
print('--------Welcome to the "Ball Collector" Game--------\n-----------------By Rahul choudhary-----------------')
print("Instructions:\nTouch the Yellow Ball\nSave your cursor from remaining balls")
def change_ball(tp_ball, n_ball, n, special_mode = 0):
    a = 1
    b = 1    
    if special_mode:
        key = 'special ball'
        key2 = 'special ball'
        a = -a
        if (seconds % 2):
            b = -b
    else:
        key = str(tp_ball)
        key2 = 'ball' + str(n_ball)

    el_dict[key2] = [0,0,0,0,0,0,0,0]
    el_dict[key2][0] = (100 + n)
    el_dict[key2][1] = (200 + n/3)
    el_dict[key2][2] = balls_dict[key][2] * a
    el_dict[key2][3] = balls_dict[key][3] * b
    el_dict[key2][4] = balls_dict[key][4]
    el_dict[key2][5] = balls_dict[key][5]
    el_dict[key2][6] = balls_dict[key][6]
    el_dict[key2][7] = pygame.Rect((100,200),(balls_dict[key][4],balls_dict[key][5]))
    tp_ball += 1
    if tp_ball == 5:
        tp_ball = 1
    return tp_ball

def game_over():
    global hsc
    hsc=max(hsc,points)
    print('-------------------- GAME OVER ---------------------\n\nPoints:',points,'\tHigh Score',hsc,'\n')
    size = 30
    font = pygame.font.Font(None, size)
    re=font.render('CLICK TO PLAY AGAIN', 1, (255, 255, 255))
    text = font.render('Touch the Yellow Ball', 1, (255, 255, 255))
    text2 = font.render('Save your cursor from remaining balls', 1, (255, 255, 255))
    re_pos=text.get_rect(centerx = int(screen.get_width()/2-5), centery = int(screen.get_height()/2 - size*4))
    text_pos = text.get_rect(centerx = int(screen.get_width()/2), centery = int(screen.get_height()/2 + size*5))
    text2_pos = text.get_rect(centerx = int(screen.get_width()/2 -80), centery = int(screen.get_height()/2 + size*4))
    credit = font.render('Created by Rahul Choudhary', 1, (178, 181, 181))
    gameover.set_alpha(230)
    screen.blit(gameover,(0,0))
    screen.blit(re,re_pos)
    screen.blit(text, text_pos)
    screen.blit(text2, text2_pos)
    screen.blit(credit,(0,(ymax-(size))))
    show_level(level)
    show_time(seconds)
    show_points(points)
    pygame.display.flip()
    h = 1
    while h:
       for e in pygame.event.get():
           if e.type == QUIT:
               exit()
           if e.type == MOUSEBUTTONDOWN:
               h = 0

def show_level(level):
    size = 24
    font = pygame.font.Font(None, size)
    text = font.render('Level: ' + str(level), 1, (255, 255, 255))
    text_pos = text.get_rect(centerx = int(screen.get_width()/2))
    screen.blit(text, text_pos)

def show_time(seconds):
    size = 24
    font = pygame.font.Font(None, size)
    text = font.render('Time: ' + str(seconds), 1, (255, 255, 255))
    screen.blit(text, (0, 0))

def show_points(points):
    size = 24
    font = pygame.font.Font(None, size)
    text = font.render('Points: ' + str(points), 1, (255, 255, 255))
    screen.blit(text, ((xmax-len(str(points))*5-70),0))
    
pygame.time.set_timer(USEREVENT, t)
pygame.time.set_timer(USEREVENT+1, 1000)

while True:
    screen.blit(background, (0,0))

    xy = pygame.mouse.get_pos()

    for key in el_dict:

        el = el_dict[key]
        if (el[0] + el[4])>xmax or el[0]<0:
            el[2] = -el[2]
        if (el[1] + el[5])>ymax or el[1]<0:
            el[3] = -el[3]
        el[0] += (el[2])
        el[1] += (el[3])

        screen.blit(el[6], (int(el[0]),int(el[1])))
    
        el[7] = pygame.Rect((int(el[0]), int(el[1])),(int(el[4]),int(el[5])))

        if el[7].collidepoint(xy):
            if key == 'special ball':
                points += 5
                catched = 1
            else:
                game_over()
                level,n_ball,seconds,points = 1,1,0,0
                el_dict = {'ball1':ball1_list, 'special ball': ball5_list}
                pygame.time.set_timer(USEREVENT, t)
                break
    if catched:
        del el_dict['special ball']
        catched = 0
        change_ball(0, 0, n, 1)

    for e in pygame.event.get():
        if e.type == QUIT:
            exit()
        if e.type == USEREVENT:
            n_ball += 1
            level += 1
            n += 10
            if n > (xmax - 100 - xballth) :
                n = 0
            pygame.time.set_timer(USEREVENT, t)
            tp_ball = change_ball(tp_ball, n_ball, n)
        if e.type == USEREVENT+1:
            points += 1
            seconds += 1
            
    show_level(level)
    show_time(seconds)
    show_points(points)
    screen.blit(ballth, (int(100 + n),int(200 + n/3)))
    pygame.display.flip()        
