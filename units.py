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
    step = 50
    test_image = None
    first_image = None
    x = 0
    y = 0
    canv = None

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

    def move(self, way):
        giflist = graphics.animation(unittypes.walk(self.unit_type))
        if way == 'right':
            self.x += self.step
            self.ex_animation()

        else:
            self.x -= self.step
            self.ex_animation()

    def ex_animation():
        global iter
        st = step / len(photolist)
        photo = photolist[iter]
        # canvas.itemconfig(image, image=photo)
        canvas.move(image, st, 0)
        iter += 1
        if iter != len(photolist):
            root.after(200, ex_animation)
        else:
            canvas.itemconfig(image, image=photolist[0])
            iter = 0

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

