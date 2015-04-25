from tkinter import *

def inscription(event):
    global line
    exec(text1.get(str('5.0'), END))      
    

def RunRight():
    pass


def RunLeft():
    pass


def RunDown():
    pass


def RunUp():
    pass
        
        
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
root.mainloop()
