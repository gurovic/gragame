from tkinter import *
def inscription(event):
    global line
    a = text1.get(str(line), END)
    analize(a)        
    line += 1.0
    

def analize(a):
    global line
    if a == 'RunRight()\n':
        RunRight()
    elif a == 'RunLeft()\n':
        RunLeft()
    elif a == 'RunUp()\n':
        RunUp()        
    elif a == 'RunDown()\n':
        RunDown()            
    elif a == 'Attack()\n':
        Attack()
    else:
        text1.insert(str(line)[:2] + str(len(a) + 1), ' Wrong Command')
        
root = Tk()
root.title('CONSOLE')
text1 = Text(root, height=10, width=50, font = 'Arial 14', wrap=WORD, bg ='blue', fg='red')
text1.insert('1.0', 'Here is your console\n')
text1.insert('2.0', 'You should use commands:\n')
text1.insert('3.0', 'RunRight(), RunLeft(), RunUp(), RunDown(), Attack()\n')
line = 4.0
text1.pack()
text1.bind('<Return>', inscription)
root.mainloop()
