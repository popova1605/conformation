import graphics
import time
import testgr
import unittypes


class Unit:
    """Класс персонажей.
       unit_type - какой персонаж, строка
       health - здоровье
       force - сила
       image - картинка"""
    unit_type = ""
    health = unittypes.health(unit_type)
    force = unittypes.force(unit_type)
    attack_image = unittypes.attack(unit_type)
    move_image = unittypes.walk(unit_type)
    death_image = unittypes.death(unit_type)
    card_image = unittypes.card(unit_type)
    step = unittypes.card(unit_type)
    test_image = None
    first_image = []
    x = 0
    y = 0
    canv = None

    def __init__(self, canvas, unit_type, x, y):
        """Присваивает переданные значения полям экземпляра self,
           force, health и image получает по unit_type (FIXME вп0исать в unittypes.py
           нужные функции"""
        self.unit_type = unit_type
        self.x = x
        self.y = y
        self.canv = canvas
        self.first_image = graphics.animation(self.move_image)[0]
        self.image = graphics.init_sprite(self.x, self.y, self.canv, self.first_image)  # TEST

    def move(self, way):
        giflist = graphics.animation(Unit.move_image)
        if way == 'right':
            for gif in giflist:
                image = gif
                self.x += self.step/graphics.amount(Unit.move_image)
                self.canv.coords(self.image, self.x, self.y)
                self.canv.itemconfig(self.image, image=image)
                time.sleep(0.1)

        else:
            self.x -= self.step

        """Движение на step в направлении way (way = "left" or "right")"""
        """giflist = graphics.animation(Unit.move_image)
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
                canv.delete(all)"""
    def win(self):
        testgr.die(self.canv, self.test_image)  # TEST

    def kill(self):
        testgr.die(self.canv, self.test_image) # TEST


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

