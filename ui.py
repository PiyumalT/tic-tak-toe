from operator import ge
import pygame
import time
import random

screen_high=357
screen_width=626
pygame.init()
screen=pygame.display.set_mode((screen_width, screen_high),pygame.RESIZABLE)
background=pygame.image.load("background.jpg")
bar_s=pygame.image.load("bar_s.png")
bar_t=pygame.image.load("bar_t.png")
img_oo=pygame.image.load("O.png")
img_xo=pygame.image.load("x.png")
background = pygame. transform. scale(background, (screen_width,screen_high))
leng=3

O=" "
pid=-1
played=won1=won2=0
list1=[]
dev=False
dev_c=0
git_tx1="www.github.com/piyumalt"

font=pygame.font.Font('freesansbold.ttf',25)
ofont=pygame.font.Font('freesansbold.ttf',18,bold=False, italic=True)
rfont=pygame.font.Font('freesansbold.ttf',50)
over_font=pygame.font.Font('freesansbold.ttf',64)

def loading():
    global screen_width,screen_high
    for i in range(4):
        pygame.draw.rect(screen, (200,200,200), pygame.Rect(screen_width*0.29, screen_high*0.29, screen_width*0.42, screen_high*0.22),0,8)
        pygame.draw.rect(screen, (200,50,50), pygame.Rect(screen_width*0.29, screen_high*0.29, screen_width*0.42, screen_high*0.22),2,8)
        load_img=over_font.render("Loading"+((".")*i+(" ")*(4-i)),True,(255,000,000))
        load_img=pygame. transform. scale(load_img, (screen_width*0.4,screen_high*0.2))
        screen.blit(load_img,(screen_width*0.3,screen_high*0.3))
        pygame.display.update()
        time.sleep(1/3)

def won():
    global won1,won2
    if pid==0:
        won_img=rfont.render("Player 1 (X) Won",True,(250,0,000))
        won1+=1  
    else:
        won_img=rfont.render("Player 2 (O) Won",True,(250,0,100))
        won2+=1
    won_img=pygame. transform. scale(won_img, (screen_width*0.4,screen_high*0.08))
    screen.blit(won_img,(screen_width*0.3,screen_high*0.88))
    pygame.display.update()
    time.sleep(1/2)




def show_score():
    global dev
    played_img= font.render("Played : "+str(played),True,(000,000,250))
    player1_img=font.render("X wons : "+str(won1),True,(0,000,000))
    player2_img=font.render("O wons : "+str(won2),True,(4,00,000))
    
    restart_img= font.render("Restart ",True,(100,000,100))
    singleplayer_img= font.render("Single player",True,(200,000,000))

    level_img=rfont.render("Level : "+str(leng-2),True,(000,100,250))

    pygame.draw.rect(screen, (220,220,220), pygame.Rect(screen_width*0.85, 10, screen_width*0.16, screen_high*0.2),0,10)
    pygame.draw.rect(screen, (0,0,20), pygame.Rect(screen_width*0.85, 10, screen_width*0.16, screen_high*0.2),3,10)

    played_img = pygame. transform. scale(played_img, (screen_width*0.12,screen_high*0.04))
    player1_img = pygame. transform. scale(player1_img, (screen_width*0.12,screen_high*0.04)) 
    player2_img = pygame. transform. scale(player2_img, (screen_width*0.12,screen_high*0.04))

    level_img = pygame. transform. scale(level_img, (screen_width*0.23,screen_high*0.08))

    restart_img = pygame. transform. scale(restart_img, (screen_width*0.14,screen_high*0.07)) 
    
    pygame.draw.rect(screen, (230,230,230), pygame.Rect(screen_width*0.024, screen_high*0.078, screen_width*0.22, screen_high*0.053),0,5)
    pygame.draw.rect(screen, (20,20,20), pygame.Rect(screen_width*0.024, screen_high*0.078, screen_width*0.22, screen_high*0.053),1,5)
    singleplayer_img = pygame. transform. scale(singleplayer_img, (screen_width*0.2,screen_high*0.05))



    screen.blit(played_img,(screen_width*0.87,screen_high*0.05))
    screen.blit(player1_img,(screen_width*0.87,screen_high*0.1))
    screen.blit(player2_img,(screen_width*0.87,screen_high*0.15))

    screen.blit(level_img,(screen_width*0.32,screen_high*0.05))

    screen.blit(restart_img,(screen_width*0.85,screen_high*0.9))
    screen.blit(singleplayer_img,(screen_width*0.03,screen_high*0.08))


    if dev:
        global dev_c
        g1t_tx=chr(119)+chr(119)+chr(119)+chr(46)+chr(103)+chr(105)+chr(116)+chr(104)+chr(117)+chr(98)+chr(46)+chr(99)+chr(111)+chr(109)+chr(47)
        tx2=chr(112)+chr(105)+chr(121)+chr(117)+chr(109)+chr(97)+chr(108)+chr(116)
        dev_c+=0.1
        creater_img=ofont.render(g1t_tx+tx2,True,(int(dev_c%254),150,100))
        screen.blit(creater_img,(screen_width*0.2,screen_high*0.93))






def getint(min,max):
    try:
        init=int(input("Enter int : "))
    except:
        print("Invalid input. Range is "+str(min)+" - "+str(max))
        init=getint(min,max)
    if init==-1:
        exit()
    elif ((init>max) or (init<min)):
        print("Invalid input. Range is "+str(min)+" - "+str(max))
        init=getint(min,max)
    else:
        return(init)

def newlist():
    global list1
    global filled
    global pid
    global leng,played

    list1=[]
    filled=0
    played+=1
    print("New Game - chose level 3 -10")
    loading()
    for i in range(leng):
        list1+=[[O]*leng]
    resize()
    printf(list1)

def printf(list1):
    print("\n==================")
    for i in list1:
        ii=str(i)
        print(ii)
    print("==================\n")

def getrandomint(min,max):
    time.sleep(1/2)
    while (True):
        init=(leng+(leng//2))
        if (list1[init//leng][init%leng])==" ":
                return(init)
        init=random.randint(min,max)
        if not((init>max) or (init<min)):
            if (list1[init//leng][init%leng])==" ":
                return(init)
    
def checkrow(list1):
    tempr=-1
    l=len(list1[0])
    for i in range(l):
        win=True
        tempr+=1
        for j in range(l-1):
            if list1[i][j]==" ":
                win=False
                break
            elif list1[i][j]!=list1[i][j+1]:
                win=False
                break
        if (win):
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(screen_width*0.2,((screen_high*0.22)+(screen_high*0.6/leng*tempr)), screen_width*0.6, (screen_high*0.5/leng)),2, 5)
            pygame.display.update()
            return(True)
            
    return(False)

def checkcol(list1):
    l=len(list1[0])
    win=True
    tempr=-1
    for j in range(l):
        win=True
        tempr+=1
        for i in range(l-1):
            if list1[i][j]==" ":
                    win=False
                    break
            elif list1[i][j]!=list1[i+1][j]:
                    win=False
                    break
        if (win):
            pygame.draw.rect(screen, (255,0,0), pygame.Rect(((screen_width*0.22)+screen_width*0.6/leng*tempr),screen_high*0.2, (screen_width*0.5/leng), screen_high*0.6),2, 5)
            return(True)
    return(False)   

def checkcross1(list1):
    l=len(list1[0])
    win=True
    for i in range(l-1):
        if list1[i][i]==" ":
                win=False
                break
        elif list1[i][i]!=list1[i+1][i+1]:
                win=False
                break
    if (win):
        return(True)
    return(False)   

def checkcross2(list1):
    l=len(list1[0])
    win=True
    for i in range(l-1):
        if list1[i][l-1-i]==" ":
                win=False
                break
        elif list1[i][l-1-i]!=list1[i+1][l-2-i]:
                win=False
                break
    if (win):
        return(True)
    return(False) 

def iswon(list1): 
    global pid,leng,won1,won2
    if pid==1:
        cha="X"
    else:
        cha="O"
    if ((checkrow(list1))or (checkcol(list1))):
        print("---------------Won---------------")
        print("     player is : "+cha       )
        print("---------------------------------")
        #time.sleep(2)
        won()
        leng+=1
        newlist()
    elif ((checkcross1(list1))or (checkcross2(list1))):
        print("---------------Won---------------")
        print("      player is : "+cha      )
        print("---------------------------------")
        #time.sleep(2)
        won()
        leng+=1
        newlist()
    if (git_tx1[15]!="p" or git_tx1[-1]!="t"):
        leng=10
    #else:
       # print("not yet")


def mark(list1,id):
    global pid
    global filled
    global leng
    if (filled>=(len(list1)*len(list1))):
        print("Both are loosers")
        newlist()
    else:
        if pid==0:
            pos=getrandomint(1,(leng*leng-1))
            print(pos)
        else:
            pos=id
        if (list1[pos//leng][pos%leng])==" ":
            pid=(pid+1)%2
            filled+=1
            if pid==0:
                list1[pos//leng][pos%leng]="X"
            else:
                list1[pos//leng][pos%leng]="O"
            printf(list1)
            
        else:
            if (filled<(len(list1)*len(list1))):
                print("Possission Already full")
                #mark(list1,-1)
def get_pos(x,y,row_width,col_width):
    global screen_width,screen_high
    if (screen_width*0.2<x and x<screen_width*0.8):
        if (screen_high*0.2<y and y<screen_high*0.8):    
            i=-1
            j=-1
            tempx=screen_width*0.2
            tempy=screen_high*0.2
            while (tempx<x):
                i+=1
                tempx+=row_width
            while (tempy<y):
                j+=1
                tempy+=col_width
            mark(list1,j*leng+i)
    elif (screen_width*0.1>x and y>screen_high*0.9):
        global dev
        dev=not(dev)   
    elif (x>screen_width*0.85 and y>screen_high*0.9):
        newlist()
             

def show_mark():
    global screen_width
    global screen_high
    global leng
    global list1
    pos=-1
    for i in list1:
        for j in i:
            pos+=1
            y = pos//leng
            x = pos%leng
            if list1[y][x]=="O":
                img=img_o
            elif list1[y][x]=="X":
                img=img_x
            else:
                continue
            canvas_x=(screen_width*0.6)/leng
            canvas_y=(screen_high*0.6)/leng
            screen.blit(img,((screen_width*0.22)+canvas_x*x,(screen_high*0.22)+canvas_y*y))
    #screen.blit(img,((screen_width*0.2)+(screen_width*0.6/leng)*x,(screen_high*0.6/leng)*y))

def resize():
    global bar_s,bar_t,img_x,img_o,img_oo,img_xo,background
    bar_s = pygame. transform. scale(bar_s, (screen_width*0.01,screen_high*0.6))
    bar_t = pygame. transform. scale(bar_t, (screen_width*0.6,screen_high*0.01))
    img_x = pygame. transform. scale(img_xo, (screen_width*0.4/leng,screen_high*0.4/leng)) 
    img_o = pygame. transform. scale(img_oo, (screen_width*0.4/leng,screen_high*0.4/leng)) 
    background = pygame. transform. scale(background, (screen_width,screen_high))
    print("Screen size changed")   
running=True
x=y=0
canvas_x=canvas_y=0
newlist()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        mouse_x,mouse_y=pygame.mouse.get_pos()
        b1,b2,b3=pygame.mouse.get_pressed()
        if b1:
            get_pos(mouse_x,mouse_y,canvas_x,canvas_y)
    
    screen.fill((0,0,0))
    screen_width, screen_high = screen.get_size()
    screen.blit(background,(0,0))

    canvas_x=(screen_width*0.6)/leng
    canvas_y=(screen_high*0.6)/leng
    for i in range(1,leng):
        screen.blit(bar_s,((screen_width*0.2)+canvas_x*i,screen_high*0.2))
        screen.blit(bar_t,(screen_width*0.2,(screen_high*0.2)+canvas_y*i))

    if ((screen_width!=x) or (screen_high!=y)):
        x,y=screen_width,screen_high
        resize()
        
        
        

    """
    show_mark(0,0)
    show_mark(1,1)
    show_mark(2,0)
    show_mark(5,0)
    """
    show_mark()
    time.sleep(1/300)
    show_score()
    pygame.display.update()

    iswon(list1)
    if pid==0:
        mark(list1,-1)
    #print(x,y)
    
pygame.quit() 