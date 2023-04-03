from tkinter import *
from tkinter import dialog
from tkinter import font 
from PIL import ImageTk, Image
from main import *
from BattleShip import *
from tictactoe import *
from fruit_ninja import *
from doodle_jump import *

screen = Tk()
screen.title("GAME-X")
background = ImageTk.PhotoImage(Image.open(('img/background.jpg')))
img1 = ImageTk.PhotoImage(Image.open(('img/img1.jpeg')))
img2 = ImageTk.PhotoImage(Image.open(('img/img2.jpeg')))
img3 = ImageTk.PhotoImage(Image.open(('img/img3.jpeg')))
img4 = ImageTk.PhotoImage(Image.open(('img/img4.jpeg')))
img5 = ImageTk.PhotoImage(Image.open(('img/img5.jpeg')))
img6 = ImageTk.PhotoImage(Image.open(('img/img6.jpeg')))
back_label = Label(screen, image = background)
back_label.grid(row = 0, column = 0, rowspan = 1024, columnspan = 576)

def battle():
    start_battleship()

def doodle():
    start_doodlejump()

def flappy():
    start_flappy()

def fruit():
    fruit_ninja()

def tictac():
    start_ttt()

msg_label = Label(screen, image = img1)
msg_label.grid(row = 100, column = 50, columnspan = 576)

bs_button1 = Button(screen , image = img2, command = battle).grid(row = 340, column = 100)
bs_button2 = Button(screen , image = img3, command = doodle).grid(row = 580, column = 190)
bs_button3 = Button(screen , image = img4, command = flappy).grid(row = 340, column = 280)
bs_button4 = Button(screen , image = img5, command = fruit).grid(row = 580, column = 370)
bs_button5 = Button(screen , image = img6, command = tictac).grid(row = 340, column = 460)
screen.mainloop()