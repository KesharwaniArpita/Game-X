import pygame
import random 
    
# updating the platform as the game progresses
def update_platforms(my_list,y,change):
        global font,white,black,check,gray,width,height,background,player,fps,timer,score,high_score,game_over,player_x,player_y,platforms,jump,y_change,x_change,score_last,super_jumps,super_last,player_speed,screen,running
        if (check):
            if y<100 and change<0:
                for i in range(len(my_list)):
                    my_list[i][1]-=change
            else:
                pass
            for items in range(len(my_list)):
                if my_list[items][1]>500:
                    my_list[items]=[random.randint(10,350),50,70,10]
                    score+=1
            return my_list
        else:
            for i in range(len(my_list)):
                my_list[i][1] = 700
            return my_list

 #check for collisions with blocks
def check_collisions(rect_list,j):
        global font,white,black,gray,check,width,height,background,player,fps,timer,score,high_score,game_over,player_x,player_y,platforms,jump,y_change,x_change,score_last,super_jumps,super_last,player_speed,screen,running
    
        for i in range(len(rect_list)):
            if rect_list[i].colliderect([player_x+20,player_y+60,35,4]) and jump==False and y_change>0:
                j=True
        return j

#update player's position
def update_player(y):
        global font,white,black,gray,width,check,height,background,player,fps,timer,score,high_score,game_over,player_x,player_y,platforms,jump,y_change,x_change,score_last,super_jumps,super_last,player_speed,screen,running
    
        jump_h=10
        gravity=.3
        if jump:
            y_change=-jump_h
            jump=False
        y+=y_change
        y_change+=gravity
        return y

#library of game constants
def start_doodlejump():
    global font,white,black,gray,width,height,check,background,player,fps,timer,score,high_score,game_over,player_x,player_y,platforms,jump,y_change,x_change,score_last,super_jumps,super_last,player_speed,screen,running
    pygame.init()
    font=pygame.font.Font("font/Calibri.ttf",12)
    check = True
    white=(255,255,255)
    black=(0,0,0)
    gray=(128,128,128)
    width=500
    height=500
    background=white
    player=pygame.transform.scale(pygame.image.load("img/doodler.png"),(50,50))
    fps=60
    timer=pygame.time.Clock()
    score=0
    high_score=0

    game_over=False


    #game variables
    player_x=160
    player_y=360
    platforms=[[175,480,70,10],[85,37,70,10],[200,370,70,10],[55,260,70,10],[135,150,70,10],[265,150,70,10]]
    jump=False
    y_change=0
    x_change=0
    score_last=0
    super_jumps=2
    jump_last=0
    player_speed=3


    #create screen
    screen=pygame.display.set_mode([width ,height])
    pygame.display.set_caption("Doodler")
    running=True
    while running==True:
        timer.tick(fps)
        screen.fill(background)
        screen.blit(player,(player_x,player_y))
        blocks=[]
        score_text=font.render('Score: '+str(score),True,black,background)
        screen.blit(score_text,(260,20))
        high_score_text=font.render('High Score: '+str(high_score),True,black,background)
        screen.blit(high_score_text,(260,40))
        super_jump_text=font.render('Space jumps: '+str(super_jumps),True,black,background)
        screen.blit(super_jump_text,(260,60))
        if game_over==True:
            check = False
            game_over_text=font.render('game over: Please press space to restart ',True,(143,0,255),background)
            screen.blit(game_over_text,(150,150))
        
        for i in range(len(platforms)):
            block=pygame.draw.rect(screen,black,platforms[i],0,3 )
            blocks.append(block)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE and game_over==True:
                    game_over=False
                    check = True
                    score=0
                    player_x=160
                    player_y=360
                    background=white
                    super_jumps=2
                    jump_last=0
                    platforms=[[175,48,70,10],[85,37,70,10],[200,370,70,10],[55,260,70,10],[135,150,70,10],[265,150,70,10],]
                if event.key==pygame.K_SPACE and not game_over and super_jumps>0:
                    super_jumps-=1
                    y_change=-10
                if event.key==pygame.K_LEFT:
                    x_change=-player_speed
                if event.key==pygame.K_RIGHT:
                    x_change=player_speed
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_change=0
                if event.key==pygame.K_RIGHT:
                    x_change=0 




        jump=check_collisions(blocks,jump)
        player_x+=x_change

        if player_y<440:
            player_y=update_player(player_y)
        else:
            game_over=True
            y_change=0
            x_change=0
        platforms=update_platforms(platforms,player_y,y_change)


        if player_x<-20:
            player_x=-10
        elif player_x>330:
            player_x=320
        
        if x_change>0:
            player=pygame.transform.scale(pygame.image.load("img/doodler.png"),(50,50))
        elif x_change<0:
            player=pygame.transform.flip(pygame.transform.scale(pygame.image.load("img/doodler.png"),(50,50)),1,0)

        if score>high_score:
            high_score=score

        if score-score_last>15:
            score_last=score
            background=(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        if score-jump_last>50:
            jump_last=score
            super_jumps+=1

            
        pygame.display.flip()
    pygame.quit()

