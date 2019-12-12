from mathematical_parametrs import Game, Player
from units import*
from unittypes import cost
import math

fight_distanse = 0


class Buttle_field:
    """Игровое поле.
       roads - список дорожек, тип Road
       canvas - виджет Canvas
       money1_im, money2_im, mana1_im, mana2_im - объекты соотв. надписей на canvas
    """
    roads = []
    canvas = None
    v_size = 0
    h_size = 0
    money1_im = None
    money2_im = None
    mana1_im = None
    mana2_im = None
    health1_im = None
    health2_im = None

    def __init__(self, canvas, h, w):
        """Создаёт всё вышеописанное"""
        self.roads = []
        self.roads.append(Road(1/9*h, w, h/6))
        self.roads.append(Road(3/9*h, w, h/6))
        self.roads.append(Road(5/9*h, w, h/6))
        self.canvas = canvas
#-------------------------------------------------------
        canvas.create_line(0,1/9*h+h/12,800,1/9*h+h/12)
        canvas.create_line(0,1/9*h-h/12,800,1/9*h-h/12)
        canvas.create_line(0,3/9*h+h/12,800,3/9*h+h/12)
        canvas.create_line(0,3/9*h-h/12,800,3/9*h-h/12)
        canvas.create_line(0,5/9*h+h/12,800,5/9*h+h/12)
        canvas.create_line(0,5/9*h-h/12,800,5/9*h-h/12)
#--------------------------------------------------------------
        self.h_size = w
        self.v_size = h
        self.money1_im = canvas.create_text(w/6, h/20, text = "Money: 0")
        self.money2_im = canvas.create_text(w - w/6, h/20, text = "Money: 0")
        self.mana1_im = canvas.create_text(w/6, h/10, text = "Mana: 0")
        self.mana2_im = canvas.create_text(w - w/6, h/10, text = "Mana: 0")
        self.health1_im = canvas.create_text(w/6, 3*h/20, text = "Health: 0")
        self.health2_im = canvas.create_text(w - w/6, 3*h/20, text = "Health: 0")

    def move_roads(self, game):
        """Вызов move_units для всех дорожек; проверка на поражение"""
        harm = [0, 0]
        for road in self.roads:
            l = road.move_units()
            harm[0] += l[0]
            harm[1] += l[1]
        game.players[0].health -= harm[0]
        game.players[1].health -= harm[1]

    def set_parametrs(self, game):
        """Изменяет значения text в money1_im, money2_im, mana1_im, mana2_im
           на значения, содержащиеся в game (экз. Game)"""
        self.canvas.itemconfig(self.money1_im, text="Money:" + str(game.players[0].money))
        self.canvas.itemconfig(self.money2_im, text="Money:" + str(game.players[1].money))
        self.canvas.itemconfig(self.mana1_im, text="Mana:" + str(game.players[0].mana))
        self.canvas.itemconfig(self.mana2_im, text="Mana:" + str(game.players[1].mana))
        self.canvas.itemconfig(self.health1_im, text="Health:" + str(game.players[0].health))
        self.canvas.itemconfig(self.health2_im, text="Health:" + str(game.players[1].health))

    def set_players_parametrs(self, player):
        """Изменяет значения text в money1_im, mana1_im, или mana2_im, money2_im
           на значения, содержащиеся в player (экз. Player)"""
        if player.number == 1:
            self.canvas.itemconfig(self.money1_im, text="Money:" + str(player.money))
            self.canvas.itemconfig(self.mana1_im, text="Mana:" + str(player.mana))
            self.canvas.itemconfig(self.health1_im, text="Health:" + str(player.health))
        if player.number == 2:
            self.canvas.itemconfig(self.money2_im, text="Money:" + str(player.money))
            self.canvas.itemconfig(self.mana2_im, text="Mana:" + str(player.mana))
            self.canvas.itemconfig(self.health2_im, text="Health:" + str(player.health))

    


class Road:
    """Дорожка.
       Содержит списки персонажей на ней, рисунок последней положеной карты,
       координату y середины и ширину """
    left_unit_list = []
    right_unit_list = []
    last_card_im = None
    y = 0
    begin = 30
    end = 770
    width = 0     # полная ширина

    def __init__(self, y, length, width):
        self.y = y
        self.length = length
        self.width = width
        self.left_unit_list = []
        self.right_unit_list = []

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
                if abs(i.x-j.x) <= abs(i.step+j.step):
                    for k in fight(i, j):
                        k.kill()
                        if self.left_unit_list.count(k):
                            self.left_unit_list.remove(k)
                        if self.right_unit_list.count(k):
                            self.right_unit_list.remove(k)
        harm = [0,0]
        delist = []
        for i in self.left_unit_list:
            if abs(i.x - self.end) < i.step:
                i.win()
                delist.append(i)
                harm[1]+=1
        for i in delist:
            self.left_unit_list.remove(i)
        delist = []
        for i in self.right_unit_list:
            if abs(i.x - self.begin) < i.step:
                i.win()
                delist.append(i)
                harm[0]+=1
        for i in delist:
            self.right_unit_list.remove(i)
        return harm

    def catch_card(self, card):
        """Добавление новой карты.
           Смена last_card_im. Создание unit"""
        self.last_card_im = card.image
        if card.player.number == 1:
            self.left_unit_list.append(Unit(card.field.canvas, card.unit_type, 
                                            self.begin, self.y))
        if card.player.number == 2:
            self.right_unit_list.append(Unit(card.field.canvas, card.unit_type, 
                                            self.end, self.y))
        card.player.money -= cost(card.unit_type)
        card.field.set_players_parametrs(card.player)
        #card.field.canvas.itemconfig(self.last_card_im, image = card(card.unit_type))
