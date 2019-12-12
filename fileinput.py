
def save_game(game, buttle_field):
    """Сохраняет текущее состояние игры в файл last_game.txt
       предполагаемый формат
       turn
       money1
       money2
       max_money
       mana1
       mana2
       health1
       health2

       
       """
    f = open('last_game.txt', 'w')
    f.write(game.turn + '\n' + game.money1 + '\n' + game.money2 + '\n' + game.max_money + '\n' + game.mana1
            + '\n' + game.mana2 + '\n' + game.health1 + '\n' + game.health2)
    f.close()


def read_game(game, buttle_field):
    """Заполняет поля классов значениями из файла last_game"""
    f = open('last_game.txt', 'r')
    game.turn = f.readline()
    game.money1 = f.readline()
    game.money2 = f.readline()
    game.max_money = f.readline()
    game.mana1 = f.readline()
    game.mana2 = f.readline()
    game.health1 = f.readline()
    game.health2 = f.readline()
    f.close()
