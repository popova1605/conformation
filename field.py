from mathematical_parametrs import Game, Player
from units import*

fight_distanse = 0

class Buttle_field:
    """Игровое поле.
       roads - список дорожек, тип Road
       canvas - виджет Canvas
       money1_im, money2_im, mana1_im, mana2_im - объекты соотв. надписей на canvas
    """
    canvas = None
    money1_im = None
    money2_im = None
    mana1_im = None
    mana2_im = None

    def __init__(self, canvas, h, w):
        """Создаёт всё вышеописанное"""
        roads = [Road(]
        pass

    def move_roads(self):
        """Вызов move_units для всех дорожек"""
        pass

    def set_parametrs(self, game):
        """Изменяет значения text в money1_im, money2_im, mana1_im, mana2_im
           на значения, содержащиеся в game (экз. Game)"""
        pass

    def set_players_money_parametrs(self, player):
        """Изменяет значения text в money1_im, mana1_im, или mana2_im, money2_im
           на значения, содержащиеся в player (экз. Player)"""

        pass

class Road:
    """Дорожка.
       Содеджит списки персонажей еа ней, рисунок последней положеной карты,
       координату y середины и ширину """
    left_unit_list = []
    right_unit_list = []
    last_card_im = None
    y = 0
    width = 0
    le

    def __init__(self, y, length):
        pass

    def move_units(self):
        """Вызов move для всех персонажей на дорожке.
           Проверка встречи вражеских персонажей.
           Вызов для этих персонажей fight и удаление проигравшего(их) с дорожки"""
        pass

    def catch_card(self, card):
        """Добавление новой карты.
           Смена last_card_im. Создание unit"""
        pass

    
    
    

    
