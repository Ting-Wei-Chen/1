import numpy as np
import pygame

def white_five_point_judge(A,n):
    v=0
    h=0
    con1=False
    con2=False
    for i in range(n):
        for j in range(n):
            if A[i,j]==-1:
                if con1:
                    h+=1
                else:
                    h=1
                    con1=True
            else:
                con1=False
            if A[j,i]==-1:
                if con2:
                    v+=1
                else:
                    v=1
                    con2=True
            else:
                con2=False
            if v==5:
                return True
                
            if h==5:
                return True
            continue
        continue
    
    con1=False
    con2=False
    
    for i in range(n-4):
        for j in range(n-4):
            x=0
            y=0
            for k in range(5):
               if A[i+k,j+k]==-1:
                   if con1:
                       x+=1
                   else:
                       x=1
                       con1=True
               else:
                    con1=False
                    
               if  A[i+k,n-1-j-k]==-1:
                   if con2:
                       y+=1
                   else:
                       y=1
                       con2=True
               else:
                    con2=False
                   
               continue
            if x==5:
                return True
            if y==5:
                return True

        continue
    return False
def black_five_point_judge(A,n):
    v=0
    h=0
    con1=False
    con2=False
    for i in range(n):
        for j in range(n):
            if A[i,j]==1:
                if con1:
                    h+=1
                else:
                    h=1
                    con1=True
            else:
                con1=False
            if A[j,i]==1:
                if con2:
                    v+=1
                else:
                    v=1
                    con2=True
            else:
                con2=False
            if v==5:
                return True
                
            if h==5:
                return True
            continue
        continue
    
    con1=False
    con2=False
        
    for i in range(n-4):
        for j in range(n-4):
            x=0
            y=0
            for k in range(5):
               if A[i+k,j+k]==1:
                   if con1:
                       x+=1
                   else:
                       x=1
                       con1=True
               else:
                    con1=False
                    
               if  A[i+k,n-1-j-k]==1:
                   if con2:
                       y+=1
                   else:
                       y=1
                       con2=True
               else:
                    con2=False
                   
               continue
            if x==5:
                return True
            if y==5:
                return True

        continue
    return False

def game():
    pygame.init()
    win=pygame.display.set_mode((900,800))
    pygame.display.set_caption('五子棋')
    font=pygame.font.SysFont('utf-8',80)
    
    win.fill((205,162,123))
    for j in range(0,20,1):
        pygame.draw.line(win,(0,0,0),(20,j*40+20),(780,j*40+20),5)
        pygame.draw.line(win,(0,0,0),(j*40+20,20),(j*40+20,780),5)
    
    list1=[3,10,16]
    list2=[3,10,16]
    for i in list1:
        for j in list2:
            pygame.draw.circle(win,(0,0,0),(i*40+20,j*40+20),8)
    
    pygame.display.update()
    
    
        
    A=np.zeros([19,19])
    black=True
    white=False
        
    while (not white_five_point_judge(A,19)) and (not black_five_point_judge(A,19)):
        
            
        while black:
            pygame.draw.rect(win,(0,0,0),(830,100,50,50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if pos[0]<800:
                        x=pos[0]//40
                    else:
                        continue
                    if pos[1]!=800:
                        y=pos[1]//40
                    else:
                        continue
                    if A[x,y]==0 :
                        A[x,y]=1
                        pygame.draw.circle(win,(0,0,0),(x*40+20,y*40+20),19)
                        white=True
                        black=False
                        pygame.display.update()
                        break
                elif event.type==pygame.QUIT:
                    pygame.quit()
                    break
                continue
                    
        if black_five_point_judge(A,19):
            break
        while white:
            pygame.draw.rect(win,(255,255,255),(830,100,50,50))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if pos[0]<800:
                        x=pos[0]//40
                    else:
                        continue
                    if pos[1]!=800:
                        y=pos[1]//40
                    else:
                        continue
                    if A[x,y]==0:
                        A[x,y]=-1
                        pygame.draw.circle(win,(220,220,220),(x*40+20,y*40+20),19)
                        white=False
                        black=True
                        pygame.display.update()
                        break
                elif event.type==pygame.QUIT:
                    pygame.quit()
                    break
                continue
        continue
    pygame.time.delay(250)
    
    win.fill((255,255,255))
    if not black:
        word=font.render('black win',False,(0,0,0))
        win.blit(word,(400,400))
        pygame.display.update()
    if not white:
        word=font.render('white win',False,(0,0,0))
        win.blit(word,(400,400))
        pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                break
game()