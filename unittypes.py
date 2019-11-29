# функции, возвращающие то, что зависит от персонажа
# Всех новых персонажей предлагается записывать сюда через elif
# FIXME придумайте персонажей!!!!

from tkinter import*

def cost(unit_type):
    """Стоимость"""
    if unit_type == "unknown_type":
        return 0

def card_image(unit_type, canvas, coords):
    """Объект картинки на карте"""
    if unit_type == "unknown_type":
        image = [canvas.create_oval(0, 0, 0, 0)]
    return image
# etc.
