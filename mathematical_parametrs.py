class Player:
    """Класс, содержащий численные параметры игрока
       number - номер, 1 или 2;
       mana - кол-во маны у игрока в данный момент
       money - кол-во денег у игрока в данный момент"""
    number = 0
    mana = 0
    money = 0
    
    def __init__(self, number, mana, money):
        """Инициализация полей экземпляра класса
           соответствующими полученными значениями"""
        pass

    def pay(cost):
        """Вычитает cost из money"""
        pass


# константы игры
start_money = 1  # деньги в начале игры у каждого игрока
start_mana = 1   # мана в начале игры у каждого игрока
additional_mana = 1  # добавка маны после хода

class Game:
    """Класс, содержащий численные параметры текущей игры
       turn - чей ход, 1 или 2,
       players - список игроков(экземпляров Player)
       max_money - кол-во денег у каждого игрока в начале хода
       add_mana - мана, вщифвляемая игроку перед ходом"""
    turn = 1
    players = []
    max_money = 0
    add_mana = 0
    
    def __init__(self):
        """Инициализация игры:
           ход 1-ого,
           создаёт и записывает в players двух игроков
           с номерами 1 и 2, маной start_mana, деньгами start_money,
           записывает в поле add_mana значение additional_mana,
           в поле max_money значение start_money
           """
        pass
    
    def end_turn(self, event):
        """Конец хода.
           Если self.turn == 2, то увеличивает self.max_money на 1,
           записывает self.max_money в поля money обоих элементов players,
           увеличивает поля mana обоих элементов players на self.add_mana.
           Меняет значение self.turn с 1 на 2 и наоборот """
        pass
    
