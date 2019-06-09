import numpy as np
import pygame
import sys
import random
import time


A=np.zeros([50,50])
for i in range(3,6):
    A[3,i]=i-2


class timer():
    def __init__(self):
        self.start_time=0
        self.end_time=0
    def start(self):
        self.start_time=time.time()
    def end(self):
        self.end_time=time.time()
    def get(self):
        return int(self.end_time-self.start_time)

class bug():
    def __init__(self):
        self.start=[3,5]
        self.end=[3,3]
        self.mode=2
        self.num=3
    
    def move(self,mode,A):
        if mode==1:
            if A[self.start[0],self.start[1]-1]==0:
                A[self.start[0],self.start[1]-1]=1
                A[self.end[0],self.end[1]]=0
                self.start=[self.start[0],self.start[1]-1]
                self.set_end()
                self.set_ord(A)
                return True
            else:
                return False
        elif mode==2:
            if A[self.start[0],self.start[1]+1]==0:
                A[self.start[0],self.start[1]+1]=1
                A[self.end[0],self.end[1]]=0
                self.start=[self.start[0],self.start[1]+1]
                self.set_end()
                self.set_ord(A)
                return True
            else:
                return False
        elif mode==3:
            if A[self.start[0]+1,self.start[1]]==0:
                A[self.start[0]+1,self.start[1]]=1
                A[self.end[0],self.end[1]]=0
                self.start=[self.start[0]+1,self.start[1]]
                self.set_end()
                self.set_ord(A)
                return True
            else:
                return False
        elif mode==4:
            if A[self.start[0]-1,self.start[1]]==0:
                A[self.start[0]-1,self.start[1]]=1
                A[self.end[0],self.end[1]]=0
                self.start=[self.start[0]-1,self.start[1]]
                self.set_end()
                self.set_ord(A)
                return True
            else:
                return False
    
    def set_end(self):
        if A[self.end[0]-1,self.end[1]]==self.num-1:
            self.end=[self.end[0]-1,self.end[1]]
        elif A[self.end[0]+1,self.end[1]]==self.num-1:
            self.end=[self.end[0]+1,self.end[1]]
        elif A[self.end[0],self.end[1]-1]==self.num-1:
            self.end=[self.end[0],self.end[1]-1]
        else:
            self.end=[self.end[0],self.end[1]+1]
    def set_mode(self,mode):
        self.mode=mode
    def add_end(self,A):
        self.num_add(A)
        if A[self.end[0]-1,self.end[1]]==self.num-2:
            self.end=[self.end[0]+1,self.end[1]]
            A[self.end[0],self.end[1]]=self.num
        elif A[self.end[0]+1,self.end[1]]==self.num-2:
            self.end=[self.end[0]-1,self.end[1]]
            A[self.end[0],self.end[1]]=self.num
        elif A[self.end[0],self.end[1]-1]==self.num-2:
            self.end=[self.end[0],self.end[1]+1]
            A[self.end[0],self.end[1]]=self.num
        else:
            self.end=[self.end[0],self.end[1]-1]
            A[self.end[0],self.end[1]]=self.num
        
    def num_add(self,A):
        self.num+=1
    def set_ord(self,A):
        for i in range(50):
            for j in range(50):
                if A[i,j]>0 and [i,j]!=self.start:
                    A[i,j]+=1

bug1=bug()
timer1=timer()

def generator(A):
    while True:
        apple_x=random.randint(5,42)
        apple_y=random.randint(5,42)
        if A[apple_y,apple_x]==1:
            continue
        else:
            loc=[apple_y,apple_x]
            return loc

loc=generator(A)

class bomb():
    def __init__(self):
        pass
    def loc(self,A):
        while True:
            self.x=random.randint(5,42)
            self.y=random.randint(5,42)

            if A[self.y,self.x]==1 or [self.x,self.y]==loc:
                continue
            else:
                break

bomb1=bomb()
bomb1.loc(A)

pygame.init()
win=pygame.display.set_mode([600,500])

font=pygame.font.SysFont('utf-8',30)

def count():
    i=1
    font=pygame.font.SysFont('utf-8',30)
    while timer1.count:
        w=font.render(chr(i+48),False,(0,0,0))
        i+=1
        win.blit(w,(500,450))
        pygame.display.update()
        time.sleep(1)
def draw():
    win.fill((255,255,255))
    pygame.draw.line(win,(0,0,0),(500,0),(500,500),4)
    pygame.draw.line(win,(0,0,0),(0,0),(0,500),4)
    pygame.draw.line(win,(0,0,0),(0,500),(500,500),4)
    pygame.draw.line(win,(0,0,0),(0,0),(500,0),4)
    for i in range(50):
        for j in range(50):
            if A[j,i]>0:
                pygame.draw.circle(win,(255,0,0),(i*10+5,j*10+5),5)
    pygame.draw.circle(win,(0,0,0),(bug1.start[1]*10+5,bug1.start[0]*10+5),2)
    pygame.draw.circle(win,(0,0,0),(bomb1.x*10+5,bomb1.y*10+5),5)


    pygame.draw.circle(win,(0,255,0),(loc[1]*10+5,loc[0]*10+5),5)
    pygame.display.update()

score=0


run=True
timer1.start()

while run:
    
    press=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                try:
                    if bug1.move(1,A):    
                                    
                        bug1.set_mode(1)
                        press=True
                    else:
                        word='crash snack'
                        break
                except:
                    word='crash wall'
                    break
            if event.key==pygame.K_RIGHT:
                try:
                    if bug1.move(2,A):
                        
                        bug1.set_mode(2)
                        press=True
                    else:
                        word='crash snack'
                        break
                except:
                    word='crash wall'
                    break
            if event.key==pygame.K_UP:
                try:
                    if bug1.move(4,A):
                        bug1.set_mode(4)
                        press=True
                    else:
                        word='crash snack'
                        break
                except:
                    word='crash wall'
                    break

            if event.key==pygame.K_DOWN:
                try:
                    if bug1.move(3,A):
                        
                        bug1.set_mode(3)
                        press=True
                    else:
                        word='crash snack'
                        break
                except:
                    word='crash wall'
                    break
    if bug1.mode==1 and bug1.start[1]<0 and press:
        break
    elif bug1.mode==4 and bug1.start[0]<0 and press:
        break
    
    
    
    if not press:
        if bug1.mode==1 and bug1.start[1]<=0:
            word='crash wall'
            break
        elif bug1.mode==4 and bug1.start[0]<=0:
            word='crash wall'
            break
        try:
            if not bug1.move(bug1.mode,A):
                word='crash snack'
                break
        except:
            word='crash wall'
            break
    if bug1.start==loc:
        score+=1
        bug1.add_end(A)
        loc=generator(A)
    if score>100:
        word='finish'
        break
    if bug1.start==[bomb1.y,bomb1.x]:
        word='eat bomb'
        break
    
    

    draw()
    word=font.render('score:{}'.format(score),False,(0,0,0))
    win.blit(word,(520,50))
    pygame.display.update()

    pygame.time.wait(135)
    continue

timer1.end()

win.fill((255,255,255))
word1=font.render('score:{}'.format(score),False,(0,0,0))
word2=font.render('elapsed time:{} second'.format(timer1.get()),False,(0,0,0))
word3=font.render(word,False,(0,0,0))
win.blit(word1,(220,230))
win.blit(word2,(220,270))
win.blit(word3,(220,310))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break
    
    continue