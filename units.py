step = 30

class Unit:
    """Класс персонажей.
       unit_type - какой персонаж, строка
       health - здоровье
       force - сила
       image - картинка"""
    unit_type = ""
    health = 0
    force = 0
    image = None
    x = 0
    y = 0

    def __init__(self, unit_type, x, y):
        """Присваивает переданные значения полям экземпляра self,
           force, health и image получает по unit_type (FIXME вписать в unittypes.py
           нужные функции"""
        pass

    def move(self, way):
        """Движение на step в направлении way (way = "left" or "right")"""
        pass


def fight(unit1, unit2):
    """Битва персонажей.
       Из health каждого персоножа вычитается force второго.
       Если health перс. стало <0, он проиграл.
       Возвращает список проигравших персонажей, если таких нет,
       вызывается рекурсивно"""
    loosers = [unit2]
    return loosers
