from mathematical_parametrs import Game, Player
from units import*
import math

fight_distanse = 0


class Buttle_field:
    """Игровое поле.
       roads - список дорожек, тип Road
       canvas - виджет Canvas
       money1_im, money2_im, mana1_im, mana2_im - объекты соотв. надписей на canvas
    """
    canvas = None
    v_size = 0
    h_size = 0
    money1_im = None
    money2_im = None
    mana1_im = None
    mana2_im = None

    def __init__(self, canvas, h, w):
        """Создаёт всё вышеописанное"""
        self.roads = 0
        self.roads.append(Road(1/9*h, w, h/6))
        self.roads.append(Road(3/9*h, w, h/6))
        self.roads.append(Road(5/9*h, w, h/6))
        self.canvas = canvas
        h_size = w
        v_size = h
        money1_im = canvas.create_text(w/6, h/20, text = "Money: 0")
        money2_im = canvas.create_text(w - w/6, h/20, text = "Money: 0")
        mana1_im = canvas.create_text(w/6, h/10, text = "Mana: 0")
        mana2_im = canvas.create_text(w - w/6, h/10, text = "Mana: 0")
        roads = [Road()]
        pass

    def move_roads(self):
        """Вызов move_units для всех дорожек"""
        for road in self.roads:
            road.move_units()

    def set_parametrs(self, game):
        """Изменяет значения text в money1_im, money2_im, mana1_im, mana2_im
           на значения, содержащиеся в game (экз. Game)"""
        self.itemconfig(self.money1_im, text="Money:" + str(game.players[0].money))
        self.itemconfig(self.money2_im, text="Money:" + str(game.players[1].money))
        self.itemconfig(self.mana1_im, text="Mana:" + str(game.players[0].mana))
        self.itemconfig(self.mana2_im, text="Mana:" + str(game.players[1].mana))

    def set_players_money_parametrs(self, player):
        """Изменяет значения text в money1_im, mana1_im, или mana2_im, money2_im
           на значения, содержащиеся в player (экз. Player)"""

        pass


class Road:
    """Дорожка.
       Содеджит списки персонажей на ней, рисунок последней положеной карты,
       координату y середины и ширину """
    left_unit_list = []
    right_unit_list = []
    last_card_im = None
    y = 0
    width = 0     # полная ширина

    def __init__(self, y, length, width):
        self.y = y
        self.length = length
        self.width = width

    def move_units(self):
        """Вызов move для всех персонажей на дорожке.
           Проверка встречи вражеских персонажей.
           Вызов для этих персонажей fight и удаление проигравшего(их) с дорожки"""
        for i in self.left_unit_list:
            i.move("right")
        for i in self.right_unit_list:
            i.move("left")
        for i in self.left_unit_list:
            for j in self.right_unit_list:
                if math.abs(i.x-j.x) <= math.abs(i.step-j.step):
                    for k in fight(i, j):
                        del k

    def catch_card(self, card):
        """Добавление новой карты.
           Смена last_card_im. Создание unit"""
        #FixME
        self.last_card_im = card.image
        #FixME
