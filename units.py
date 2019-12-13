import graphics
import testgr
import unittypes


class Unit:
    """Класс персонажей.
       unit_type - какой персонаж, строка
       health - здоровье
       force - сила
       image - картинка"""
    root = None
    unit_type = ""
    health = 0
    force = 0
    step = 100
    test_image = None
    first_image = None
    x = 0
    y = 0
    canv = None
    it = 0
    photolist = None
    st = 0

    def __init__(self, root, canvas, unit_type, x, y):
        """Присваивает переданные значения полям экземпляра self,
           force, health и image получает по unit_type (FIXME вп0исать в unittypes.py
           нужные функции"""
        self.root = root
        self.unit_type = unit_type
        self.x = x
        self.y = y
        self.canv = canvas
        self.first_image = graphics.animation(unittypes.walk(self.unit_type))[0]
        self.image = graphics.init_sprite(self.x, self.y, self.canv, self.first_image)
        self.it = 0
        self.photolist = None
        self.st = 0
        self.to_die = 0
        self.fin = 1

    def move(self, way):
        self.photolist = graphics.animation(unittypes.walk(self.unit_type))
        self.st = self.step / len(self.photolist)
        if way == 'right':
            self.x += self.step
            self.ex_animation()

        else:
            self.x -= self.step
            self.st *= (-1)
            self.ex_animation()

    def ex_animation(self):
        self.fin = 0
        photo = self.photolist[self.it]
        self.canv.itemconfig(self.image, image=photo)
        self.canv.move(self.image, self.st, 0)
        self.it += 1
        if self.it != len(self.photolist):
            self.root.after(200, self.ex_animation)
        else:
            self.canv.itemconfig(self.image, image=self.photolist[0])
            if self.to_die == 1:
                self.die()
            else: self.fin = 1
            self.it = 0

    def win(self):
        if self.fin:
            self.photolist = graphics.animation(unittypes.attack(self.unit_type))
            self.st = 0
            self.to_die = 1
            self.ex_animation()
        else: self.root.after(10, self.win)
        

    def kill(self):
        if self.fin:
            self.to_due = 1
            self.photolist = graphics.animation(unittypes.death(self.unit_type))
            self.st = 0
            self.ex_animation()
        else: self.root.after(10, self.kill)


    def attak(self):
        if self.fin:
            self.photolist = graphics.animation(unittypes.attack(self.unit_type))
            self.st = 0
            self.ex_animation()
        else: self.root.after(10, self.attak)

    def die(self):
        self.canv.delete(self.image)
        self.fin = 1

    def foo(self):
        1+1



def fight(unit1, unit2):
    loosers = []
    """Битва персонажей.
       Из health каждого персонажа вычитается force второго.
       Если health перс. стало <=0, он проиграл.
       Возвращает список проигравших персонажей, если таких нет,
       вызывается рекурсивно"""

    unit1.attak()
    unit2.attak()
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

