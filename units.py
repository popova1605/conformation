import graphics
import time


class Unit:
    """Класс персонажей.
       unit_type - какой персонаж, строка
       health - здоровье
       force - сила
       image - картинка"""
    unit_type = ""
    health = 0
    force = 0
    attack_image = []
    move_image = []
    death_image =[]
    card_image = []
    step = 0
    x = 0
    y = 0

    def __init__(self, unit_type, x, y):

        """Присваивает переданные значения полям экземпляра self,
           force, health и image получает по unit_type (FIXME вп0исать в unittypes.py
           нужные функции"""

    def move(self, way):
        """Движение на step в направлении way (way = "left" or "right")"""
        giflist = graphics.animation(Unit.move_image)
        if way == 'right':
            for gif in giflist:
                canv = graphics.canvas(Unit.x, Unit.y, Unit.move_image)
                canv.create_image(graphics.Height(Unit.move_image)/2, graphics.Width(Unit.move_image)/2, image=gif)
                time.sleep(0.1)
                self.x += Unit.step/graphics.amount(Unit.move_image)
                canv.delete(all)
        if way == 'left':
            for gif in giflist:
                canv = graphics.canvas(Unit.x, Unit.y, Unit.move_image)
                canv.create_image(graphics.Height(Unit.move_image) / 2, graphics.Width(Unit.move_image) / 2, image=gif)
                time.sleep(0.1)
                self.x -= Unit.step/graphics.amount(Unit.move_image)
                canv.delete(all)


def fight(unit1, unit2):
    loosers = []
    """Битва персонажей.
       Из health каждого персонажа вычитается force второго.
       Если health перс. стало <=0, он проиграл.
       Возвращает список проигравших персонажей, если таких нет,
       вызывается рекурсивно"""
    if unit1.health <= unit2.force and unit2.health <= unit1.force:
        loosers.append(unit1)
        loosers.append(unit2)
    elif unit1.health <= unit2.force and unit2.health >= unit1.force:
        loosers.append(unit1)
    elif unit1.health >= unit2.force and unit2.health <= unit1.force:
        loosers.append(unit2)
    elif unit1.health >= unit2.force and unit2.health >= unit1.force:
        unit1.health -= unit2.force
        unit2.health -= unit1.force
        loosers = (fight(unit1, unit2))
    return loosers

