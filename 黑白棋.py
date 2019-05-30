import numpy as np
import pygame


def fix(A,n,a,b):
    
    suc=False
    
    black=False
    white=False
    x=a-1
    
    if A[a,b]==1:
        while x>=0:
            if A[x,b]==-1:
                white=True
            elif A[x,b]==1:
                if not white:
                    break
                else:
                    for i in range(a,x,-1):
                        A[i,b]=1
                    suc=True
                    break
            else:
                break
            x-=1
            continue
        
    elif A[a,b]==-1:
        while x>=0:
            if A[x,b]==1:
                black=True
            elif A[x,b]==-1:
                if not black:
                    break
                else:
                    for i in range(a,x,-1):
                        A[i,b]=-1
                    suc=True
                    break
            else:
                break
            x-=1
            continue
    black=False
    white=False
    x=a+1
    if A[a,b]==1:
        while x<n:
            if A[x,b]==-1:
                white=True
            elif A[x,b]==1:
                if not white:
                    break
                else:
                    for i in range(a,x):
                        A[i,b]=1
                    suc=True
                    break
            else:
                break
            
            x+=1
            continue
        y=b+1
        
        
    elif A[a,b]==-1:
        while x<n:
            if A[x,b]==1:
                black=True
            elif A[x,b]==-1:
                if not black:
                    break
                else:
                    for i in range(a,x):
                        A[i,b]=-1
                    suc=True
                    break
            else:
                break
            
            x+=1
            continue
    
    black=False
    white=False
    y=b-1
    
    if A[a,b]==1:
        while y>=0:
            if A[a,y]==-1:
                white=True
            elif A[a,y]==1:
                if not white:
                    break
                else:
                    for i in range(b,y,-1):
                        A[a,i]=1
                    suc=True
                    break
            else:
                break
            y-=1
            continue
    elif A[a,b]==-1:
        while y>=0:
            if A[a,y]==1:
                black=True
            elif A[a,y]==-1:
                if not black:
                    break
                else:
                    for i in range(b,y,-1):
                        A[a,i]=-1
                    suc=True
                    break
            else:
                break
            y-=1
            continue
            
    black=False
    white=False
    
    y=b+1
    if A[a,b]==1:
        while y<n:
            if A[a,y]==-1:
                white=True
                
            elif A[a,y]==1:
                if not white:
                    break
                else:
                    for i in range(b,y):
                        A[a,i]=1
                    suc=True
                    break

            else:
               break
            y+=1
            continue
            
    elif A[a,b]==-1:
        while y<n:
            if A[a,y]==1:
                black=True
                
            elif A[a,y]==-1:
                if not black:
                    break
                else:
                    for i in range(b,y):
                        A[a,i]=-1
                    suc=True
                    break
            else:
                break
            y+=1
            continue
    black=False
    white=False
    
    x=a-1
    y=b-1
    if A[a,b]==1:
        while x>=0 and y>=0:
            if A[x,y]==-1:
                white=True
            elif A[x,y]==1:
                if not white:
                    break
                else:
                    for i in range(b,y,-1):
                        A[i-b+a,i]=1
                    suc=True
                    break
            else:
                break
            x-=1
            y-=1
            continue
    elif A[a,b]==-1:
        while x>=0 and y>=0:
            if A[x,y]==1:
                black=True
            elif A[x,y]==-1:
                if not black:
                    break
                else:
                    for i in range(b,y,-1):
                        A[i-b+a,i]=-1
                    suc=True
                    break
            else:
                break
            x-=1
            y-=1
            continue
    black=False
    white=False
    
    x=a+1
    y=b+1
    
    if A[a,b]==1:
        while x<n and y<n:
            if A[x,y]==-1:
                white=True
            elif A[x,y]==1:
                if not white:
                    break
                else:
                    for i in range(a,x):
                        A[i,i-a+b]=1
                    suc=True
                    break
            else:
                break
            x+=1
            y+=1
            continue
    elif A[a,b]==-1:
        while x<n and y<n:
            if A[x,y]==1:
                black=True
            elif A[x,y]==-1:
                if not black:
                    break
                else:
                    for i in range(a,x):
                        A[i,i-a+b]=-1
                    suc=True
                    break
            else:
                break
            x+=1
            y+=1
            continue
    
    black=False
    white=False
    x=a+1
    y=b-1
    if A[a,b]==1:
        while x<n and y>=0:
            if A[x,y]==-1:
                white=True
            elif A[x,y]==1:
                if not white:
                    break
                else:
                    for i in range(a,x):
                        A[i,b-i+a]=1
                    suc=True
                    break
            else:
                break
            x+=1
            y-=1
            continue
    elif A[a,b]==-1:
        while x<n and y>=0:
            if A[x,y]==1:
                black=True
            elif A[x,y]==-1:
                if not black:
                    break
                else:
                    for i in range(a,x):
                        A[i,b-i+a]=-1
                    suc=True
                    break
            else:
                break
            x+=1
            y-=1
            continue
    black=False
    white=False
    x=a-1
    y=b+1
    
    if A[a,b]==1:
        while x>=0 and y<n:
            if A[x,y]==-1:
                white=True
            elif A[x,y]==1:
                if not white:
                    break
                else:
                    for i in range(b,y):
                        A[a-i+b,i]=1
                    suc=True
                    break
            else:
                break
            x-=1
            y+=1
            continue
    elif A[a,b]==-1:
        while x>=0 and y<n:
            if A[x,y]==1:
                black=True
            elif A[x,y]==-1:
                if not black:
                    break
                else:
                    for i in range(b,y):
                        A[a-i+b,i]=-1
                    suc=True
                    break
            else:
                break
            x-=1
            y+=1
            continue
    
    if suc:
        return True
    else:
        return False
    
def win_judge(A,n):
    bla=0
    whi=0
    for i in range(n):
        for j in range(n):
            if A[i,j]==1:
                bla+=1
            elif A[i,j]==-1:
                whi+=1
    
    return(bla,whi)
   
def con_judge(A,n,c):
    for i in range(n):
        for j in range(n):
            if A[i,j]==0:
                B=A.copy()
                B[i,j]=c
                if fix(B,n,i,j):
                    return True
    
    return False
def all_judge(A,n):
    for i in range(n):
        for j in range(n):
            if A[i,j]==0:
                return False
    return True
def game():
    pygame.init()
    win=pygame.display.set_mode([500,400])
    
        
    pygame.display.update()
    
    black=True
    white=False
    
    A=np.zeros([8,8])
    A[3,3]=-1
    A[3,4]=1
    A[4,3]=1
    A[4,4]=-1
    
    win.fill((0,255,0))
    
    for j in range(1,8,1):
        pygame.draw.line(win,(0,0,0),(0,j*50),(400,j*50),5)
        pygame.draw.line(win,(0,0,0),(j*50,0),(j*50,400),5)
    pygame.draw.line(win,(0,0,0),(400,0),(400,400),5)
    for i in range(8):
        for j in range(8):
            if A[i,j]==1:
                pygame.draw.circle(win,(0,0,0),(i*50+25,j*50+25),20)
            elif A[i,j]==-1:
                pygame.draw.circle(win,(255,255,255),(i*50+25,j*50+25),20)
    
    pygame.display.update()
    
    while True:
        if not con_judge(A,8,1) and con_judge(A,8,-1):
            white=True
            black=False
        elif not con_judge(A,8,1):
            break
            
        while black:
            pygame.draw.rect(win,(0,0,0),(450,50,40,40))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if pos[0]<400:
                        x=pos[0]//50
                    else:
                        continue
                    if pos[1]!=400:
                        y=pos[1]//50
                    else:
                        continue
                    if A[x,y]==0:
                        A[x,y]=1
                        if fix(A,8,x,y):
                            pygame.draw.circle(win,(0,0,0),(x*50+25,y*50+25),20)
                            white=True
                            black=False
                            pygame.display.update()
                            break
                        else:
                            A[x,y]=0
                            continue
                    else:
                        continue
                elif event.type==pygame.QUIT:
                    pygame.quit()
                    break
            
        win.fill((0,255,0))
        for j in range(1,8,1):
            pygame.draw.line(win,(0,0,0),(0,j*50),(400,j*50),5)
            pygame.draw.line(win,(0,0,0),(j*50,0),(j*50,400),5)
        pygame.draw.line(win,(0,0,0),(400,0),(400,400),5)
        for i in range(8):
            for j in range(8):
                if A[i,j]==1:
                    pygame.draw.circle(win,(0,0,0),(i*50+25,j*50+25),20)
                elif A[i,j]==-1:
                    pygame.draw.circle(win,(255,255,255),(i*50+25,j*50+25),20)
                continue
            continue
        pygame.display.update()
            
        if not con_judge(A,8,-1) and con_judge(A,8,1):
            white=False
            black=True
        elif not con_judge(A,8,-1):
            break
        
        while white:
            pygame.draw.rect(win,(255,255,255),(450,50,40,40))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pos=pygame.mouse.get_pos()
                    if pos[0]<400:
                        x=pos[0]//50
                    else:
                        continue
                    if pos[1]!=400:
                        y=pos[1]//50
                    else:
                        continue
                    if A[x,y]==0:
                        A[x,y]=-1
                        if fix(A,8,x,y):
                            pygame.draw.circle(win,(255,255,255),(x*50+25,y*50+25),20)
                            white=False
                            black=True
                            pygame.display.update()
                            break
                        else:
                            A[x,y]=0
                            continue
                    else:
                        continue
                elif event.type==pygame.QUIT:
                    pygame.quit()
                    break
        
        
        win.fill((0,255,0))
        for j in range(1,8,1):
            pygame.draw.line(win,(0,0,0),(0,j*50),(400,j*50),5)
            pygame.draw.line(win,(0,0,0),(j*50,0),(j*50,400),5)
        pygame.draw.line(win,(0,0,0),(400,0),(400,400),5)
        for i in range(8):
            for j in range(8):
                if A[i,j]==1:
                    pygame.draw.circle(win,(0,0,0),(i*50+25,j*50+25),20)
                elif A[i,j]==-1:
                    pygame.draw.circle(win,(255,255,255),(i*50+25,j*50+25),20)
                
            
        pygame.display.update()
        continue
    
    win.fill((255,255,255))
    font=pygame.font.SysFont('cp950'.encode('cp950','ignore').decode('cp950','ignore'),40)
    
    if win_judge(A,8)[0]>win_judge(A,8)[1]:
        word=font.render('black win'.encode('cp950','ignore').decode('cp950','ignore'),False,(0,0,0))
    elif win_judge(A,8)[0]<win_judge(A,8)[1]:
        word=font.render('white win'.encode('cp950','ignore').decode('cp950','ignore'),False,(0,0,0))
    else:
        word=font.render('flat'.encode('cp950','ignore').decode('cp950','ignore'))
    win.blit(word,(170,300))
    word2=font.render('black:{};white:{}'.format(win_judge(A,8)[0],win_judge(A,8)[1]).encode('cp950','ignore').decode('cp950','ignore'),False,(0,0,0))
    win.blit(word2,(170,100))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                break
            
game()
