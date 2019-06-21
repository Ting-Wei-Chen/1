import numpy as np
import pygame
import random
import sys

size=11
class player():
    def __init__(self):
        self.player_map=np.zeros([size,size])
        self.player_map[size-1,1]=1
        self.loc=1
    def move(self,dir):
        self.player_map[size-1,self.loc]=0
        self.loc+=dir
        self.player_map[size-1,self.loc]=1

class bomb():
    def __init__(self):
        self.bomb_map=np.zeros([size,size])
    def grt(self):
        self.bomb_map[0,random.randint(0,size-1)]=1
    def move_down(self):
        for i in range(size-1,-1,-1):
            for j in range(size):
                if self.bomb_map[i,j]==1:
                    if i==size-1:
                        self.bomb_map[i,j]=0
                    else:
                        self.bomb_map[i,j]=0
                        self.bomb_map[i+1,j]=1

class bullet():
    def __init__(self):
        self.bullet_map=np.zeros([size,size])
    def move(self):
        for i in range(size):
            for j in range(size):
                if self.bullet_map[i,j]==1:
                    if i==0:
                        self.bullet_map[i,j]=0
                    else:
                        self.bullet_map[i,j]=0
                        self.bullet_map[i-1,j]=1


player1=player()
bomb1=bomb()
bullet1=bullet()

def killed_test():
    if bomb1.bomb_map[size-1,player1.loc]==1:
        return True
    else:
        return False

def crashed():
    for i in range(size):
        for j in range(size):
            if bullet1.bullet_map[i,j]==1 and bomb1.bomb_map[i,j]==1:
                bullet1.bullet_map[i,j]=0
                bomb1.bomb_map[i,j]=0
                return True

pygame.init()
win=pygame.display.set_mode([size*50,size*50])

def draw_player():
    pygame.draw.circle(win,(255,0,0),(player1.loc*50+25,(size-1)*50+25),24)
def draw_bomb():
    for i in range(size):
        for j in range(size):
            if bomb1.bomb_map[i,j]==1:
                pygame.draw.circle(win,(0,0,0),(j*50+25,i*50+25),24)
            continue
def draw_bullet():
    for i in range(size):
        for j in range(size):
            if bullet1.bullet_map[i,j]==1:
                pygame.draw.circle(win,(192,192,192),(j*50+25,i*50+25),24)
def update():
    win.fill((255,255,255))
    draw_player()
    draw_bomb()
    draw_bullet()
    pygame.display.update()

def main():
    score=0
    while True:
        if random.randint(1,2)%2==0:
            bomb1.grt()
            draw_bomb()
            pygame.display.update()
        if killed_test():
            break
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if player1.loc>0:
                        player1.loc-=1
                if event.key==pygame.K_RIGHT:
                    if player1.loc<size-1:
                        player1.loc+=1
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            bullet1.bullet_map[size-2,player1.loc]=1
        
        if crashed():
            score+=1
        update()
        bullet1.move()
        if crashed():
            score+=1
        update()
        bomb1.move_down()
        update()
        
        font=pygame.font.SysFont('utf-8',30)
        word1=font.render('score:{}'.format(score),False,(0,0,0))
        win.blit(word1,(size*50-80,60))
        word2=font.render('time:{}'.format(pygame.time.get_ticks()//1000),False,(150,0,0))
        win.blit(word2,(size*50-80,100))
        pygame.display.update()

        if pygame.time.get_ticks()>=120000:
            break

        pygame.time.wait(135)
        continue
    font=font=pygame.font.SysFont('utf-8',100)
    win.fill((255,255,255))
    word=font.render('score:{}'.format(score),False,(0,0,0))
    win.blit(word,(size*19,size*19))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
    
if __name__=='__main__':
    main()
    
    