
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
       buttle_field.money1_im
       buttle_field.money2_im
       buttle_field.mana1_im
       buttle_field.mana2_im
       buttle_field.health1_im
       buttle_field.health2_im
       buttle_field.roads

       """
    f = open('last_game.txt', 'w')
    f.write(game.turn + '\n' + game.players[0].money + '\n' + game.players[1].money + '\n' + game.max_money + '\n'
            + game.players[0].mana + '\n' + game.players[1].mana + '\n' + game.players[0].health + '\n'
            + game.players[1].health)
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
