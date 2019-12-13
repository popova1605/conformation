import graphics
from tkinter import *
import time

root = Tk()
root.geometry('800x600')
canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)

imagelist = ['rogue_run_1_0.png', 'rogue_run_1_1.png', 'rogue_run_1_2.png', 'rogue_run_1_3.png']
giflist = graphics.animation(imagelist)
sprite = canvas.create_image(400, 300, image=giflist[0])
i=0

def move():
    global i
    i=(i+1)%4
    image = giflist[i]
    canvas.itemconfig(sprite, image=image)
    root.after(500, move)
    
move()



root.mainloop()
