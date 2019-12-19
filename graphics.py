# Вся графика - здесь!!!
from tkinter import*
import unittypes

def amount(imagelist):
    i = 0
    giflist = animation(imagelist)
    for gif in giflist:
        i = i+1
    return i


def Height(imagelist):
        photo = PhotoImage(file=imagelist[0])
        height = photo.height()
        return(height)


def Width(imagelist):
    photo = PhotoImage(file=imagelist[0])
    width = photo.width()
    return(width)


def canvas(x, y, imagelist):
    # Если это лист картинок, то все они должны быть одного размера
    photo = PhotoImage(file=imagelist[0])
    width = photo.width()
    height = photo.height()
    canv = Canvas(x, y, width=width, height=height)
    canv.pack()
    return canv


def animation(imagelist):
    # создает лист объектов (картинок)
    giflist = []
    for imagefile in imagelist:
        photo = PhotoImage(file=imagefile)
        giflist.append(photo)
    return giflist


def init_sprite(x, y, canvas, gif):
    sprite = canvas.create_image(x, y, image=gif)
    canvas.pack()
    return sprite


def move_sprite(x, y, canvas, image, imagefile):
    canvas.coords(image, x, y)
    canvas.itemconfig(image, image=imagefile)


def make_card():
    pass



