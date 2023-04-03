from tkinter import *
from tkinter import dialog
import random
import math
from PIL import ImageTk, Image


def var_assign():
        global blocks,blocks1, count1, count2, count3,count4,count5,comp_done,player_done, cship_pos1, cship_pos2, cship_pos3, cship_pos4, cship_pos5, play, count_game_player,count_game_comp, pos5,pos1,pos2,pos3,pos4
        count_game_comp=0
        count_game_player=0
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        count5 = 0
        pos1 =[]
        pos2=[]
        pos3=[]
        pos4=[]
        pos5=[]
        cship_pos1=[]
        cship_pos2=[]
        cship_pos3=[]
        cship_pos4=[]
        cship_pos5=[]
        comp_done=[]
        player_done=[]
        play = 'no'

def change(var):
        global blocks,blocks1,comp_done,player_done, cship_pos1, cship_pos2, cship_pos3, cship_pos4, cship_pos5, play, count_game_player,count_game_comp, pos5,pos1,pos2,pos3,pos4
        if play=='yes' and var not in player_done:
            if var+1 in cship_pos1 or var+1 in cship_pos2 or var+1 in cship_pos3 or var+1 in cship_pos4 or var+1 in cship_pos5 :
                blocks[var] = Button(screen, bg='red', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 10, rowspan=50,columnspan=50)
                count_game_player+=1
                play = 'naa'
            else:
                blocks[var] = Button(screen, bg='white', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 10, rowspan=50,columnspan=50)
                play = 'naa'
            player_done.append(var)

        if play == 'naa':
            num = random.randint(0,99)
            while num in comp_done:
                num = random.randint(0,99)
            if num in pos1 or num in pos2 or num in pos3 or num in pos4 or num in pos5:
                blocks1[num] = Button(screen, bg='red', height=2, width=4).grid(row=(num // 10) * 50 + 40,column=((num) % 10) * 50 + 640, rowspan=50,columnspan=50)
                play = 'yes'
                count_game_comp+=1
            else:
                blocks1[num] = Button(screen, bg='white', height=2, width=4).grid(row=(num // 10) * 50 + 40,column=((num) % 10) * 50 + 640, rowspan=50,columnspan=50)
                play = 'yes'
            comp_done.append(num)

        if count_game_player == 17:
            over_label = Label(screen, text='GAME OVER --> PLAYER WINS').grid(row=0, column=0, columnspan=1200, rowspan = 600)
            restart = Button(screen, text='Rematch???', command = start).grid(row=0, column=600, rowspan=600, columnspan=600)

        elif count_game_comp == 17:
            over_label=Label(screen, text='GAME OVER --> COMPUTER WINS').grid(row = 0 , column = 0, columnspan =1200, rowspan = 600)
            restart = Button(screen, text='Rematch???', command = start).grid(row = 0, column = 0, rowspan = 600, columnspan =600)
        
def comp_ships():
        global cship_pos1, cship_pos2, cship_pos3,cship_pos4, cship_pos5, play, count1, count2, count4, count3, count5
        if count1==5 and count2==4 and count3==3 and count4==3 and count5==2:
            for i in range(5):
                dir=random.randint(1,2) #1->Down , 2->Side
                if i==0 and dir==1:
                    Iblock=random.randint(1,60)
                    for j in range(5):
                        cship_pos1.append(Iblock)
                        Iblock+=10
                if i==0 and dir==2:
                    Iblock1=random.randint(1,6)
                    Iblock2=random.randint(0,9)
                    for j in range(5):
                        cship_pos1.append(Iblock2*10+Iblock1)
                        Iblock1+=1
                if i==1 and dir==1:
                    Iblock=random.randint(1,70)
                    while Iblock in cship_pos1 or Iblock+10 in cship_pos1 or Iblock+20 in cship_pos1 or Iblock+30 in cship_pos1:
                        Iblock=random.randint(1,70)
                    for j in range(4):
                        cship_pos2.append(Iblock)
                        Iblock+=10
                if i==1 and dir==2:
                    Iblock1=random.randint(1,7)
                    Iblock2=random.randint(0,9)
                    while Iblock2*10+Iblock1 in cship_pos1 or Iblock2*10+Iblock1+1 in cship_pos1 or Iblock2*10+Iblock1+2 in cship_pos1 or Iblock2*10+Iblock1+3 in cship_pos1:
                        Iblock1 = random.randint(1, 7)
                        Iblock2 = random.randint(0, 9)
                    for j in range(4):
                        cship_pos2.append(Iblock2*10+Iblock1)
                        Iblock1+=1
                if i==2 and dir==1:
                    Iblock=random.randint(1,80)
                    while Iblock in cship_pos1 or Iblock+10 in cship_pos1 or Iblock+20 in cship_pos1 :
                        Iblock=random.randint(1,80)
                    while Iblock in cship_pos2 or Iblock+10 in cship_pos2 or Iblock+20 in cship_pos2 :
                        Iblock=random.randint(1,80)
                    for j in range(3):
                        cship_pos3.append(Iblock)
                        Iblock+=10
                if i==2 and dir==2:
                    Iblock1=random.randint(1,8)
                    Iblock2=random.randint(0,9)
                    while Iblock2*10+Iblock1 in cship_pos1 or Iblock2*10+Iblock1+1 in cship_pos1 or Iblock2*10+Iblock1+2 in cship_pos1:
                        Iblock1 = random.randint(1, 8)
                        Iblock2 = random.randint(0, 9)
                    while Iblock2*10+Iblock1 in cship_pos2 or Iblock2*10+Iblock1+1 in cship_pos2 or Iblock2*10+Iblock1+2 in cship_pos2:
                        Iblock1 = random.randint(1, 8)
                        Iblock2 = random.randint(0, 9)
                    for j in range(3):
                        cship_pos3.append(Iblock2*10+Iblock1)
                        Iblock1+=1
                if i==3 and dir==1:
                    Iblock=random.randint(1,80)
                    while Iblock in cship_pos1 or Iblock+10 in cship_pos1 or Iblock+20 in cship_pos1 :
                        Iblock=random.randint(1,80)
                    while Iblock in cship_pos2 or Iblock+10 in cship_pos2 or Iblock+20 in cship_pos2 :
                        Iblock=random.randint(1,80)
                    while Iblock in cship_pos3 or Iblock+10 in cship_pos3 or Iblock+20 in cship_pos3 :
                        Iblock=random.randint(1,80)
                    for j in range(3):
                        cship_pos4.append(Iblock)
                        Iblock+=10
                if i==3 and dir==2:
                    Iblock1=random.randint(1,8)
                    Iblock2=random.randint(0,9)
                    while Iblock2*10+Iblock1 in cship_pos1 or Iblock2*10+Iblock1+1 in cship_pos1 or Iblock2*10+Iblock1+2 in cship_pos1:
                        Iblock1 = random.randint(1, 8)
                        Iblock2 = random.randint(0, 9)
                    while Iblock2*10+Iblock1 in cship_pos2 or Iblock2*10+Iblock1+1 in cship_pos2 or Iblock2*10+Iblock1+2 in cship_pos2:
                        Iblock1 = random.randint(1, 8)
                        Iblock2 = random.randint(0, 9)
                    while Iblock2*10+Iblock1 in cship_pos3 or Iblock2*10+Iblock1+1 in cship_pos3 or Iblock2*10+Iblock1+2 in cship_pos3:
                        Iblock1 = random.randint(1, 8)
                        Iblock2 = random.randint(0, 9)
                    for j in range(3):
                        cship_pos4.append(Iblock2*10+Iblock1)
                        Iblock1+=1
                if i==4 and dir==1:
                    Iblock=random.randint(1,90)
                    while Iblock in cship_pos1 or Iblock+10 in cship_pos1 :
                        Iblock=random.randint(1,90)
                    while Iblock in cship_pos2 or Iblock+10 in cship_pos2 :
                        Iblock=random.randint(1,90)
                    while Iblock in cship_pos3 or Iblock+10 in cship_pos3 :
                        Iblock=random.randint(1,90)
                    while Iblock in cship_pos4 or Iblock+10 in cship_pos4 :
                        Iblock=random.randint(1,90)
                    for j in range(2):
                        cship_pos5.append(Iblock)
                        Iblock+=10
                if i==4 and dir==2:
                    Iblock1=random.randint(1,9)
                    Iblock2=random.randint(0,9)
                    while Iblock2*10+Iblock1 in cship_pos1 or Iblock2*10+Iblock1+1 in cship_pos1:
                        Iblock1 = random.randint(1, 9)
                        Iblock2 = random.randint(0, 9)
                    while Iblock2*10+Iblock1 in cship_pos2 or Iblock2*10+Iblock1+1 in cship_pos2:
                        Iblock1 = random.randint(1, 9)
                        Iblock2 = random.randint(0, 9)
                    while Iblock2*10+Iblock1 in cship_pos3 or Iblock2*10+Iblock1+1 in cship_pos3:
                        Iblock1 = random.randint(1, 9)
                        Iblock2 = random.randint(0, 9)
                    while Iblock2*10+Iblock1 in cship_pos4 or Iblock2*10+Iblock1+1 in cship_pos4:
                        Iblock1 = random.randint(1, 9)
                        Iblock2 = random.randint(0, 9)
                    for j in range(2):
                        cship_pos5.append(Iblock2*10+Iblock1)
                        Iblock1+=1
            play = 'yes'


def ships(var):
        global blocks1, rt, rb1, rb2, rb3, rb4, rb5, count2, count3, count4, count5,count1, pos1, pos2,pos3,pos4,pos5
        if rt.get()==1 and count1<5 and var not in pos1 and var not in pos2 and var not in pos3 and var not in pos4 and var not in pos5:
            if len(pos1)==0:
                blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50,columnspan=50)
                pos1.append(var)
                count1+=1
            elif len(pos1)==1:
                if var==pos1[0]+1 or var==pos1[0]-1 or var==pos1[0]+10 or var==pos1[0]-10:
                    blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50, columnspan=50)
                    pos1.append(var)
                    count1 += 1
            elif len(pos1)==2:
                if pos1[0]==pos1[1]+1 or pos1[0]==pos1[1]-1:
                    if var==pos1[0]-1 or var==pos1[0]+1 or var==pos1[1]-1 or var==pos1[1]+1:
                        blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos1.append(var)
                        count1 += 1
                elif pos1[0]==pos1[1]+10 or pos1[0]==pos1[1]-10:
                    if var == pos1[0] - 10 or var == pos1[0] + 10 or var == pos1[1] - 10 or var == pos1[1] + 10:
                        blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos1.append(var)
                        count1 += 1
            elif len(pos1)==3:
                if pos1[0]==pos1[1]+1 or pos1[0]==pos1[1]-1:
                    if var==pos1[0]-1 or var==pos1[0]+1 or var==pos1[1]-1 or var==pos1[1]+1 or var==pos1[2]+1 or var==pos1[2]-1:
                        blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos1.append(var)
                        count1 += 1
                elif pos1[0]==pos1[1]+10 or pos1[0]==pos1[1]-10:
                    if var == pos1[0] - 10 or var == pos1[0] + 10 or var == pos1[1] - 10 or var == pos1[1] + 10 or var==pos1[2]+10 or var==pos1[2]-10:
                        blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos1.append(var)
                        count1 += 1
            elif len(pos1)==4:
                if pos1[0]==pos1[1]+1 or pos1[0]==pos1[1]-1:
                    if var==pos1[0]-1 or var==pos1[0]+1 or var==pos1[1]-1 or var==pos1[1]+1 or var==pos1[2]+1 or var==pos1[2]-1 or var==pos1[3]+1 or var==pos1[3]-1:
                        blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos1.append(var)
                        count1 += 1
                elif pos1[0]==pos1[1]+10 or pos1[0]==pos1[1]-10:
                    if var == pos1[0] - 10 or var == pos1[0] + 10 or var == pos1[1] - 10 or var == pos1[1] + 10 or var==pos1[2]+10 or var==pos1[2]-10 or var==pos1[3]+10 or var==pos1[3]-10:
                        blocks1[var] = Button(screen, bg='blue', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos1.append(var)
                        count1 += 1

        if rt.get()==2 and count2<4 and var not in pos1 and var not in pos2 and var not in pos3 and var not in pos4 and var not in pos5:
            if len(pos2)==0:
                blocks1[var] = Button(screen, bg='brown', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50,columnspan=50)
                pos2.append(var)
                count2+=1
            elif len(pos2)==1:
                if var==pos2[0]+1 or var==pos2[0]-1 or var==pos2[0]+10 or var==pos2[0]-10:
                    blocks1[var] = Button(screen, bg='brown', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50, columnspan=50)
                    pos2.append(var)
                    count2 += 1
            elif len(pos2)==2:
                if pos2[0]==pos2[1]+1 or pos2[0]==pos2[1]-1:
                    if var==pos2[0]-1 or var==pos2[0]+1 or var==pos2[1]-1 or var==pos2[1]+1:
                        blocks1[var] = Button(screen, bg='brown', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos2.append(var)
                        count2 += 1
                elif pos2[0]==pos2[1]+10 or pos2[0]==pos2[1]-10:
                    if var == pos2[0] - 10 or var == pos2[0] + 10 or var == pos2[1] - 10 or var == pos2[1] + 10:
                        blocks1[var] = Button(screen, bg='brown', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos2.append(var)
                        count2 += 1
            elif len(pos2)==3:
                if pos2[0]==pos2[1]+1 or pos2[0]==pos2[1]-1:
                    if var==pos2[0]-1 or var==pos2[0]+1 or var==pos2[1]-1 or var==pos2[1]+1 or var==pos2[2]+1 or var==pos2[2]-1:
                        blocks1[var] = Button(screen, bg='brown', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos2.append(var)
                        count2 += 1
                elif pos2[0]==pos2[1]+10 or pos2[0]==pos2[1]-10:
                    if var == pos2[0] - 10 or var == pos2[0] + 10 or var == pos2[1] - 10 or var == pos2[1] + 10 or var==pos2[2]+10 or var==pos2[2]-10:
                        blocks1[var] = Button(screen, bg='brown', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos2.append(var)
                        count2 += 1
        if rt.get()==3 and count3<3 and var not in pos1 and var not in pos2 and var not in pos3 and var not in pos4 and var not in pos5:
            if len(pos3)==0:
                blocks1[var] = Button(screen, bg='yellow', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50,columnspan=50)
                pos3.append(var)
                count3+=1
            elif len(pos3)==1:
                if var==pos3[0]+1 or var==pos3[0]-1 or var==pos3[0]+10 or var==pos3[0]-10:
                    blocks1[var] = Button(screen, bg='yellow', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50, columnspan=50)
                    pos3.append(var)
                    count3 += 1
            elif len(pos3)==2:
                if pos3[0]==pos3[1]+1 or pos3[0]==pos3[1]-1:
                    if var==pos3[0]-1 or var==pos3[0]+1 or var==pos3[1]-1 or var==pos3[1]+1:
                        blocks1[var] = Button(screen, bg='yellow', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos3.append(var)
                        count3 += 1
                elif pos3[0]==pos3[1]+10 or pos3[0]==pos3[1]-10:
                    if var == pos3[0] - 10 or var == pos3[0] + 10 or var == pos3[1] - 10 or var == pos3[1] + 10:
                        blocks1[var] = Button(screen, bg='yellow', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos3.append(var)
                        count3 += 1
        if rt.get()==4 and count4<3 and var not in pos1 and var not in pos2 and var not in pos3 and var not in pos4 and var not in pos5:
            if len(pos4)==0:
                blocks1[var] = Button(screen, bg='green', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50,columnspan=50)
                pos4.append(var)
                count4+=1
            elif len(pos4)==1:
                if var==pos4[0]+1 or var==pos4[0]-1 or var==pos4[0]+10 or var==pos4[0]-10:
                    blocks1[var] = Button(screen, bg='green', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50, columnspan=50)
                    pos4.append(var)
                    count4 += 1
            elif len(pos4)==2:
                if pos4[0]==pos4[1]+1 or pos4[0]==pos4[1]-1:
                    if var==pos4[0]-1 or var==pos4[0]+1 or var==pos4[1]-1 or var==pos4[1]+1:
                        blocks1[var] = Button(screen, bg='green', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos4.append(var)
                        count4 += 1
                elif pos4[0]==pos4[1]+10 or pos4[0]==pos4[1]-10:
                    if var == pos4[0] - 10 or var == pos4[0] + 10 or var == pos4[1] - 10 or var == pos4[1] + 10:
                        blocks1[var] = Button(screen, bg='green', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640,rowspan=50, columnspan=50)
                        pos4.append(var)
                        count4 += 1
        if rt.get()==5 and count5<2 and var not in pos1 and var not in pos2 and var not in pos3 and var not in pos4 and var not in pos5:
            if len(pos5)==0:
                blocks1[var] = Button(screen, bg='violet', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50,columnspan=50)
                pos5.append(var)
                count5+=1
            elif len(pos5)==1:
                if var==pos5[0]+1 or var==pos5[0]-1 or var==pos5[0]+10 or var==pos5[0]-10:
                    blocks1[var] = Button(screen, bg='violet', height=2, width=4).grid(row=(var // 10) * 50 + 40,column=((var) % 10) * 50 + 640, rowspan=50, columnspan=50)
                    pos5.append(var)
                    count5 += 1

def start_battleship():
    global screen, bkrd, back_img,label_back
    screen = Toplevel()
    screen.title('Battle Ship')
    bkrd = ImageTk.PhotoImage(Image.open(('img/Checkers_bs.png')))
    back_img = ImageTk.PhotoImage(Image.open(('img/Back.png')))
    s_img = ImageTk.PhotoImage(Image.open(('img/img2.jpeg')))
    label_back = Label(screen, image = back_img).grid(row = 0, column = 0, columnspan = 600, rowspan = 600)
    game_lab = Label(screen, text = 'img/Battle Ship').grid(row = 0, column = 0, columnspan = 600, rowspan = 200)
    Start_button = Button(screen, image = s_img, command = start)
    Start_button.grid(row = 0, column = 0, columnspan = 600, rowspan = 600)

    screen.mainloop()

def start():
        global blocks, blocks1, rt, rb1, rb2, rb3, rb4, rb5,head_1, head_2
        var_assign()
        label_back1 = Label(screen, image=back_img)
        label_back1.grid(row=0, column=0, columnspan=600, rowspan=600)
        label_back2 = Label(screen, image=back_img)
        label_back2.grid(row=0, column=600, columnspan=600, rowspan=600)
        head_1 = Label(screen, text='PLAYER').grid(row=30, column = 0, columnspan = 600)
        head_2 = Label(screen, text='COMPUTER').grid(row=30, column=600, columnspan = 600)

        bkrd_label = Label(screen, image = bkrd)
        bkrd_label.grid(row = 40, column = 10, rowspan = 551, columnspan = 550)
        blocks = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10',
                'B1','B2','B3','B4','B5','B6','B7','B8','B9','B10',
                'C1','C2','C3','C4','C5','C6','C7','C8','C9','C10',
                'D1','D2','D3','D4','D5','D6','D7','D8','D9','D10',
                'E1','E2','E3','E4','E5','E6','E7','E8','E9','E10',
                'F1','F2','F3','F4','F5','F6','F7','F8','F9','F10',
                'G1','G2','G3','G4','G5','G6','G7','G8','G9','G10',
                'H1','H2','H3','H4','H5','H6','H7','H8','H9','H10',
                'I1','I2','I3','I4','I5','I6','I7','I8','I9','I10',
                'J1','J2','J3','J4','J5','J6','J7','J8','J9','J10']

        for i in range(0,100):
            blocks[i] = Button(screen, height = 2, width = 4, bg = 'light pink')
            blocks[i].grid(row = (i//10)*50+40, column = ((i)%10)*50+10, rowspan = 50, columnspan = 50)
            blocks[i].configure(command = lambda  b=i: change(b))

        bkrd_label1 = Label(screen, image=bkrd)
        bkrd_label1.grid(row=40, column=640, rowspan=551, columnspan=550)
        blocks1 = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10',
                'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
                'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10',
                'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10',
                'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 'E10',
                'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10',
                'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
                'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10',
                'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10',
                'J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7', 'J8', 'J9', 'J10']

        for i in range(0, 100):
            blocks1[i] = Button(screen, height=2, width=4, bg='light pink')
            blocks1[i].grid(row=(i // 10) * 50 + 40, column=((i) % 10) * 50 + 640, rowspan=50, columnspan=50)
            blocks1[i].configure(command=lambda b=i: ships(b))

        rt = IntVar()
        rt.set(0)
        rb1 = Radiobutton(screen, text='5 unit',variable =rt, value = 1)
        rb2 = Radiobutton(screen, text='4 unit', variable=rt, value=2)
        rb3 = Radiobutton(screen, text='3 unit I', variable=rt, value=3)
        rb4 = Radiobutton(screen, text='3 unit II', variable=rt, value=4)
        rb5 = Radiobutton(screen, text='2 unit', variable=rt, value=5)
        rb1.grid(row=190, column=555, columnspan=90, rowspan=50)
        rb2.grid(row=240, column=555, columnspan=90, rowspan=50)
        rb3.grid(row=290, column=555, columnspan=90, rowspan=50)
        rb4.grid(row=340, column=555, columnspan=90, rowspan=50)
        rb5.grid(row=390, column=555, columnspan=90, rowspan=50)
        on_btn=Button(screen, text='START GAME', command = comp_ships)
        on_btn.grid(row = 0, column = 0, rowspan= 40, columnspan =1200)
   