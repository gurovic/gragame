#coding:utf-8
from tkinter import *
import sys
import time

x1, y1 = 20,  20
x2, y2 = 20,  460
x3, y3 = 460, 20
x4, y4 = 460, 460
x5, y5 = 20,  240
x6, y6 = 240, 460
x7, y7 = 240, 20
x8, y8 = 460, 240
rule = 'лол взвзвзвзв-'
rule2 = 'Эта игра была сделана учениками 9 класса В:\n Чернышев Вадим \n Александр Кучеренко \n Пархоменко Егор \nОтдельное спасибо нашим спонсорам : \n . . . \nТакже благодарим сценариста нашего проекта:\n Гуровица Владимира Михайловича'

def border(x, y):
    if 20 < x <= 460 and y == 20:
        x -= 5
    if 20 <= x < 460 and y == 460:
        x += 5
    if 20 < y <= 460 and x == 460:
        y -= 5
    if 20 <= y < 460 and x == 20:
        y += 5
    return x, y

def new_ball():
    global x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8
    can.delete(ALL)
    x1, y1 = border(x1, y1)
    x2, y2 = border(x2, y2)
    x3, y3 = border(x3, y3)
    x4, y4 = border(x4, y4)
    x5, y5 = border(x5, y5)
    x6, y6 = border(x6, y6)
    x7, y7 = border(x7, y7)
    x8, y8 = border(x8, y8)    
    can.create_rectangle(0,  0,  500, 500, fill="red")
    can.create_rectangle(20, 20, 480, 480, fill="orange")
    can.create_rectangle(90, 40, 410, 460, fill="red")
    can.create_oval(x1, y1, x1 + 20, y1 + 20, fill = "red",    width=3)
    can.create_oval(x2, y2, x2 + 20, y2 + 20, fill = "yellow", width=3)
    can.create_oval(x3, y3, x3 + 20, y3 + 20, fill = "purple", width=3)
    can.create_oval(x4, y4, x4 + 20, y4 + 20, fill = "orange",   width=3)
    can.create_oval(x5, y5, x5 + 20, y5 + 20, fill = "aqua", width=3)
    can.create_oval(x6, y6, x6 + 20, y6 + 20, fill = "green",  width=3)
    can.create_oval(x7, y7, x7 + 20, y7 + 20, fill = "white",  width=3)
    can.create_oval(x8, y8, x8 + 20, y8 + 20, fill = "blue",   width=3) 
    root.after(50, new_ball)    

def play(event):
    root.destroy()
    os.system('game.py')

def rules(event):
    root2 = Tk()
    text1 = Label(root2, text=rule, font='Arial 14')
    text1.pack(side='top')
    root2.mainloop()

def creators(event):
    root3 = Tk()
    text2 = Label(root3, text=rule2, font='Arial 14')
    text2.pack(side='top')
    root3.mainloop()

def exit_from_a_game(event):
    sys.exit()

root = Tk()
l, h = root.winfo_screenwidth() / 3.5, root.winfo_screenheight() / 7
root.wm_geometry("+%d+%d" % (l, h))
can = Canvas(root, width = 500 , height = 500)
but1 = Button(root, text = 'PLAY',     bg = 'orange', font = 'arial 36')
but2 = Button(root, text = 'RULES',    bg = 'orange', font = 'arial 36')
but3 = Button(root, text = 'CREATORS', bg = 'orange', font = 'arial 36')
but4 = Button(root, text = 'EXIT',     bg = 'orange', font = 'arial 36')

but1.place(relx = 0.2, rely = 0.1, width = 300)
but2.place(relx = 0.2, rely = 0.3, width = 300)
but3.place(relx = 0.2, rely = 0.5, width = 300)
but4.place(relx = 0.2, rely = 0.7, width = 300)
can.pack()

but1.bind('<Button-1>', play)
but2.bind('<Button-1>', rules)
but3.bind('<Button-1>', creators)
but4.bind('<Button-1>', exit_from_a_game)

root.after(100, new_ball) 

root.mainloop()
