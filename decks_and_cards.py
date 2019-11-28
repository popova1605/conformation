# Размеры карты
deck_height = 60
deck_width = 40

class Deck:
    """Колода.
       player, ones - СТАТИЧЕСКИЕ переменные"""
    unit_type = ""
    owner = 0
    field = None
    player = None
    ones = []
    def __init__(self, field=None, owner=1, x=0, y=0):
        if field:
            pass
    
    def is_clicked(self, event):
        """Проверяет, попала ли мышь по колоде"""
        return false
    
    def create_card(self):
        """Создание данной колодой карты, привязывание её follow_mouse к <Motion>
           и find_road к отпусканию кнопки мыши"""
        pass

    def set_player(self, player):
        Deck.player = player


class Card:
    unit_type = ""
    owner = 0
    field = None
    player = None
    image = None
    
    def __init__(self, deck):
        """Переменные карты совпадают с соотв. перем. колоды deck"""
        pass

    def follow_mouse(self, event):
        """Движение за мышью"""
        pass

    def find_road(self, event):
        """Перебирает дорожки, проверяя на какой находится центр карты,
           вызывает для неё catch(self), отвязывает мышь"""
        pass
    

def find_clicked_deck():
    for deck in Deck.ones:
        if deck.is_clicked() and deck.owner == Deck.player and cost(deck.unit_type) <= Deck.player.money:
            deck.create_card()

def activate_decks(player):
    Deck.field.bind("<Button-1>", find_clicked_deck)
    goast_deck = Deck()
    goast_deck.set_player(player)



    
    
