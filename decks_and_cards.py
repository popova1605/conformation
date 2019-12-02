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

    def __init__(self, field, owner, x, y):
        self.field = field
        self.owner = owner
        self.x = x
        self.y = y

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
        card = Card(self)
        self.field.canvas.bind('<Motion>', card.move)
        self.field.canvas.bind('<ButtonRelease-1>', card.find_road)


class Card:
    unit_type = ""
    field = None
    player = None
    image = None
    x = 0
    y = 0
    
    def __init__(self, deck):
        """Переменные карты совпадают с соотв. перем. колоды deck"""
        self.field = deck.field
        self.x = deck.x
        self.y = deck.y

    def move(self, event):
        """Следить за тем, чтобы карта не выходила за пределы экрана и на чужую половину"""
        if self.player.number == 1:
            if (event.x >= 0) and (event.x <= self.field.w_size/2 - deck_width):
                self.x = event.x
            if (event.y >= 0) and (event.y <= self.field.h_size/2 - deck_height):
                self.y = event.y
        else:
            if (event.x >= self.field.w_size/2) and (event.x <= self.field.w_size - deck_width):
                self.x = event.x
            if (event.y >= self.field.h_size/2) and (event.y <= self.field.h_size - deck_height):
                self.y = event.y

    def find_road(self, event):
        """Перебирает дорожки, проверяя на какой находится центр карты,
                   вызывает для неё catch_card(self), отвязывает мышь
                   и карта умирает, если дорожки не нашлось"""
        b = False
        for i in self.field.roads:
            if ((self.field.roads[i].y + self.field.roads[i].width >= event.y)
                    and (self.field.roads[i].y - self.field.roads[i].width < event.y)):
                self.field.roads[i].catch_card(self)
                b = True
        if not b:
            del self
    

def find_clicked_deck():
    for deck in Deck.ones:
        if deck.is_clicked() and deck.owner == deck.player.number and cost(deck.unit_type) <= deck.player.money:
            deck.create_card()


def activate_decks(player):
    Deck.field.bind("<Button-1>", find_clicked_deck)
    for deck in Deck.ones:
        deck.player = player

