import pygame

pygame.init()

win=pygame.display.set_mode((800,200))
pygame.display.set_caption('jumping man')




def intro():
    
    run=False
    x=400
    y=150
    width=20
    height=20
    isjump=False
    jumpcount=6
    enemy_x=800
    enemy_y=150

    show='level 1'

    global score
    score=0
    font=pygame.font.SysFont('microsoft Yahei',40)
    
    while True:
        win.fill((230,230,230))
        word=font.render('press space to start',False,(0,0,0))
        win.blit(word,(300,100))
        pygame.display.update()
    
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                break
    
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            passed_time=pygame.time.get_ticks()
            run=True
            break
    
    while run:
    
        win.fill((0,0,0))
        surface=font.render('score:{}'.format(score),False,(0,0,0))
        sur=font.render(show,1,(0,0,0))
        win.blit(surface,(30,30))
        win.blit(sur,(600,30))
        pygame.time.delay(100)
    
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
                pygame.quit()
    
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            isjump=True
    
        if isjump:
            if jumpcount>=0:
                y-=(jumpcount**2)
                jumpcount-=1
            elif jumpcount>-7:
                y+=(jumpcount**2)
                jumpcount-=1
            else:
                jumpcount=6
                isjump=False
            
            
        win.fill((230,230,230))
        surface=font.render('score:{}'.format(score),False,(0,0,0))
        time=font.render('time:{}'.format((pygame.time.get_ticks()-passed_time)//1000),False,(0,0,0))
        win.blit(surface,(30,30))
        win.blit(sur,(600,30))
        win.blit(time,(30,60))
        pygame.draw.rect(win,(0,0,0),(x,y,height,width))
        pygame.draw.rect(win,(255,0,0),(enemy_x,enemy_y,height,width))
    
    
        if y==enemy_y and x==enemy_x:
            run=False
        elif y!=enemy_y and x ==enemy_x:
            score+=1
        if enemy_x<0:
            enemy_x=800
    
        
        if score>10 and score<=20:
            enemy_x-=25
            show='level 2'
        elif score>20 and score<=30:
            enemy_x-=40
            show='level 3'
        elif score>30 and score<=40:
            enemy_x-=50
            show='level 4' 
        elif score >40:
            enemy_x-=80
            show='level 5'
        else:
            enemy_x-=20
            pygame.display.update()
intro()

font=pygame.font.SysFont('microsoft Yahei',40)

while True:
    re=False
    
    win.fill((230,230,230))

    surface=font.render('score:{}'.format(score),False,(0,0,0))
    win.blit(surface,(400,30))

    text=font.render('END',False,(0,0,0))
    win.blit(text,(420,100))
    
    text2=font.render('press anyplace to restart game',False,(0,0,0))
    win.blit(text2,(350,150))
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            break
        elif event.type==pygame.MOUSEBUTTONDOWN:
            score=0
            re=True
            
    if re:
        intro()
        re=False
    
    continue