from tkinter import*
import unittypes as u
from units import Unit
import testgr
# Размеры карты
deck_height = 60
deck_width = 40


class Deck:
    """Колода.
        ones - СТАТИЧЕСКАЯ переменная
        (x,y) - coords of card's upper left point"""
    unit_type = ""
    owner = 0
    field = None
    player = None
    ones = []
    x = 0
    y = 0
    im = None
    card = None

    def __init__(self, field, unit_type, owner, x, y):
        self.unit_type = unit_type
        self.field = field
        Deck.field = field
        self.owner = owner
        self.x = x
        self.y = y
        self.im = testgr.ca(field.canvas, x, y) #TEST
        Deck.ones.append(self)

    def is_clicked(self, event):
        """Проверяет, попала ли мышь по колоде"""
        if((event.x <= self.x + deck_width) and (event.x >= self.x) and (event.y <= self.y + deck_height)
                and (event.y >= self.y)):
            return True
        else:
            return False
    
    def create_card(self):
        """Создание данной колодой карты, привязывание её move к <Motion>
                   и find_road к отпусканию кнопки мыши"""
        Deck.card = Card(self)
        self.field.canvas.bind('<Motion>', Deck.card.move)
        self.field.canvas.bind('<ButtonRelease-1>', Deck.card.find_road)


class Card:
    unit_type = ""
    field = None
    player = None
    image = None
    x = 0
    y = 0

    def __init__(self, deck):
        """Переменные карты совпадают с соотв. перем. колоды deck"""
        self.unit_type = deck.unit_type
        self.field = deck.field
        self.x = deck.x
        self.y = deck.y
        self.player = deck.player
        self.image = testgr.ca(self.field.canvas, self.x, self.y) #TEST

    def move(self, event):
        """Следить за тем, чтобы карта не выходила за пределы экрана и на чужую половину"""
        if self.player.number == 1:
            if (event.x >= 0) and (event.x <= self.field.h_size/2 - deck_width):
                self.x = event.x
            if (event.y >= 0) and (event.y <= self.field.v_size - deck_height):
                self.y = event.y
        else:
            if (event.x >= self.field.h_size/2) and (event.x <= self.field.h_size - deck_width):
                self.x = event.x
            if (event.y >= 0) and (event.y <= self.field.v_size - deck_height):
                self.y = event.y
        testgr.move_c(self.field.canvas, self.image, self.x, self.y)

    def find_road(self, event):
        """Перебирает дорожки, проверяя на какой находится центр карты,
                   вызывает для неё catch_card(self), отвязывает мышь
                   и карта умирает, если дорожки не нашлось"""
        self.field.canvas.bind('<Motion>', "")
        self.field.canvas.bind('<ButtonRelease-1>', "")
        b = False
        for i in self.field.roads:
            if ((i.y + i.width/2 >= event.y)
                    and (i.y - i.width/2 < event.y)):
                i.catch_card(self)
                b = True
        self.hide()

    def hide(self):
        self.field.canvas.delete(self.image)
    

def find_clicked_deck(event):
    for deck in Deck.ones:
        if deck.is_clicked(event) and deck.owner == deck.player.number and u.cost(deck.unit_type) <= deck.player.money:
            deck.create_card()


def activate_decks(player):
    Deck.field.canvas.bind("<Button-1>", find_clicked_deck)
    for deck in Deck.ones:
        deck.player = player

