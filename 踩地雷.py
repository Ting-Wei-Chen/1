import numpy as np
import random
import pygame
import sys

size=16

class bomb_loc():
    def __init__(self,size):
        self.map=np.zeros((size,size))
    def bomb_grt(self,num,size):
        i=0
        while i<num:
            x=random.randint(0,size-1)
            y=random.randint(0,size-1)
            if self.map[x,y]==1:
                continue
            else:
                self.map[x,y]=1
                i+=1
                continue


bomb=bomb_loc(size)
bomb.bomb_grt(18,size)

class map_loc():
    def __init__(self,size):
        self.map=(np.zeros((size,size))-np.ones((size,size)))
    def num_find(self,x,y,size):
        sum=0
        if x>0:
            if bomb.map[x-1,y]==1:
                sum+=1
        if x<size-1:
            if bomb.map[x+1,y]==1:
                sum+=1
        if y>0:
            if bomb.map[x,y-1]==1:
                sum+=1
        if y<size-1:
            if bomb.map[x,y+1]==1:
                sum+=1
        if x>0 and y>0:
            if bomb.map[x-1,y-1]==1:
                sum+=1
        if x<size-1 and y>0:
            if bomb.map[x+1,y-1]==1:
                sum+=1
        if x>0 and y<size-1:
            if bomb.map[x-1,y+1]==1:
                sum+=1
        if x<size-1 and y<size-1:
            if bomb.map[x+1,y+1]==1:
                sum+=1
        return sum
    def jud(self,x,y):
        if bomb.map[x,y]==1:
            return True
        else:
            return False
    def num_etr(self,x,y,size):
        self.map[x,y]=self.num_find(x,y,size)

        if self.map[x,y]==0:
            if x>0 and self.map[x-1,y]==-1:
                self.num_etr(x-1,y,size)
            if x<size-1 and self.map[x+1,y]==-1:
                self.num_etr(x+1,y,size)
            if y>0 and self.map[x,y-1]==-1:
                self.num_etr(x,y-1,size)
            if y<size-1 and self.map[x,y+1]==-1:
                self.num_etr(x,y+1,size)
            if x>0 and y>0 and self.map[x-1,y-1]==-1:
                self.num_etr(x-1,y-1,size)
            if x<size-1 and y>0 and self.map[x+1,y-1]==-1: 
                self.num_etr(x+1,y-1,size)
            if x>0 and y<size-1 and self.map[x-1,y+1]==-1:
                self.num_etr(x-1,y+1,size)
            if x<size-1 and y<size-1 and self.map[x+1,y+1]==-1:
                self.num_etr(x+1,y+1,size)
class flag():
    def __init__(self):
        self.map=np.zeros((size,size))
    def set_flag(self,x,y):
        if self.map[x,y]==1:
            self.map[x,y]=0
        else:
            self.map[x,y]=1
    
map=map_loc(size)
flag1=flag()

pygame.init()
win=pygame.display.set_mode([size*50,size*50])
win.fill((255,255,255))
pygame.display.update()

font=pygame.font.SysFont('utf-8',35)
def draw():
    
    for i in range(size):
        for j in range(size):
            pygame.draw.rect(win,(100,100,100),(i*50+3,j*50+3,44,44))
            

    pygame.display.update()
def set_num(mode):
    flag_img=pygame.image.load("flag.jpg")
    flag_img=pygame.transform.scale(flag_img,(40,40))
    for i in range(size):
        for j in range(size):
            
            if map.map[i,j]==0:
                word=font.render(chr(int(map.map[i,j])+48),False,(0,0,0))
                win.blit(word,(i*50+25,j*50+25))
            elif map.map[i,j]==1:
                word=font.render(chr(int(map.map[i,j])+48),False,(50,255,50))
                win.blit(word,(i*50+25,j*50+25))
            elif map.map[i,j]==2:
                word=font.render(chr(int(map.map[i,j])+48),False,(0,0,255))
                win.blit(word,(i*50+25,j*50+25))
            elif map.map[i,j]==3:
                word=font.render(chr(int(map.map[i,j])+48),False,(255,0,0))
                win.blit(word,(i*50+25,j*50+25))
            elif map.map[i,j]>3:
                word=font.render(chr(int(map.map[i,j])+48),False,(255,0,255))
                win.blit(word,(i*50+25,j*50+25))
            elif flag1.map[i,j]==1 and mode:
                win.blit(flag_img,(i*50+5,j*50+5))
    pygame.display.update()

def check():
    for i in range(size):
        for j in range(size):
            if map.map[i,j]==-1:
                if bomb.map[i,j]!=1:
                    return False
    
    return True
def end_check():
    for i in range(size):
        for j in range(size):
            if bomb.map[i,j]!=1:
                if map.map[i,j]==-1:
                    return True
    
    return False
def game():
    draw()
    
    run=True
    while run:
        press=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                if event.button==1:
                    if map.jud(pos[0]//50,pos[1]//50):
                        run=False
                        break
                    else:
                        map.num_etr(pos[0]//50,pos[1]//50,size)
                        press=True
                elif event.button==3:
                    flag1.set_flag(pos[0]//50,pos[1]//50)
                    press=True
             
        if press:
            draw()
            set_num(True)
        if end_check():
            continue
        else:
            break
def end():
    win.fill((255,255,255))
    draw()
    set_num(False)
    for i in range(size):
        for j in range(size):
            if bomb.map[i,j]==1:
                pygame.draw.circle(win,(0,0,0),(i*50+25,j*50+25),15)

    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        continue
game()
end()