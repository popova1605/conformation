from tkinter import*

def die(c, im):
    c.delete(im)

def un(canvas, x, y):
    return canvas.create_oval(x - 30, y - 30, x + 30, y + 30, fill="blue")

def move_un(canv, image, x, y):
    canv.coords(image, x - 30, y - 30, x + 30, y + 30)

def ca(canvas, x, y):
    return canvas.create_rectangle(x, y, x+40, y+60, fill = "red")

def move_c(canvas, image, x, y):
    canvas.coords(image, x, y, x+40, y+60)

def w(canvas, image):
    canvas.itemconfig(image, fill = "red")
