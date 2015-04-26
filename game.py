from tkinter import *
import sys
import time

x1, y1, x2, y2 = 510, 510, 530, 530
move = []
lenn = 0
count = 0

def inscription(event):
    global line
    exec(text1.get(str('5.0'), END))      
    

def RunRight(n):
    global move, lenn
    move += [['Right', n]]
    lenn += 1

def RunLeft(n):
    global move, lenn
    move += [['Left', n]]   
    lenn += 1

def RunDown(n):
    global move, lenn
    move += [['Down', n]]   
    lenn += 1

def RunUp(n):
    global move, lenn
    move += [['Up', n]]   
    lenn += 1     
        
root = Tk()
root.title('CONSOLE')
text1 = Text(root, height=15, width=75, font = 'Arial 14', wrap=WORD, bg ='mint cream', fg='red')
text1.insert('1.0', 'Here is your console\n')
text1.insert('2.0', 'You should use python commands\n')
text1.insert('3.0', 'And you must use commands:\n')
text1.insert('4.0', 'RunUp(), RunDown(), RunLeft(), RunRight()\n')
ready = Button(root, text = 'READY', bg = 'orange', font = 'arial 36')
c = 0
text1.pack()
ready.pack(fill = 'both')
ready.bind('<Button-1>', inscription)

def new_ball():
    global x1, y1, x2, y2, count, lenn
    can.create_oval(x1, y1, x2, y2, fill = "red", width=3)
    if count < lenn:
        if move[count][1] != 0:
            if move[count][0] == 'Right':
                x1, x2 = x1 + 5, x2 + 5
            elif move[count][0] == 'Left':
                x1, x2 = x1 - 5, x2 - 5
            elif move[count][0] == 'Down':
                y1, y2 = y1 + 5, y2 + 5
            elif move[count][0] == 'Up':
                y1, y2 = y1 - 5, y2 - 5
            move[count][1] -= 1
        else:
            count += 1
    root.after(50, new_ball)         

root = Tk()
root.title("Game")
root.wm_geometry("+%d+%d" % (0, 0))

can = Canvas(root, width = root.winfo_screenwidth() - 18, height = root.winfo_screenheight())
can.pack()

root.after(100, new_ball) 

root.mainloop()
