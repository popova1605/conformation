
def save_game(game, buttle_field):
    ''' Сохраняет текущее состояние игры в файл last_game.txt
       предполагаемый формат
       turn
       money1
       money2
       max_money
       mana1
       mana2
       health1
       health2
       buttle_field.roads[].left_unit_list[].unit_type для всех дорожек
       buttle_field.roads[].left_unit_list[].health для всех дорожек...
       buttle_field.roads[].left_unit_list[].y
       buttle_field.roads[].left_unit_list[].x
       buttle_field.roads[].right_unit_list[].health....
       buttle_field.roads[].right_unit_list[].unit_type
       buttle_field.roads[].right_unit_list[].y
       buttle_field.roads[].right_unit_list[].x
       '''
    f = open('last_game.txt', 'w')
    f.write(str(game.turn) + '\n' + str(game.players[0].money) + '\n' + game.players[1].money + '\n' + game.max_money + '\n'
            + game.players[0].mana + '\n' + game.players[1].mana + '\n' + game.players[0].health + '\n'
            + game.players[1].health)
    for i in buttle_field.roads:
        for j in i.left_unit_list:
            f.write(str(j.unit_type))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.left_unit_list:
            f.write(str(j.health))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.left_unit_list:
            f.write(str(j.x))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.left_unit_list:
            f.write(str(j.y))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.right_unit_list:
            f.write(str(j.unit_type))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.right_unit_list:
            f.write(str(j.health))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.right_unit_list:
            f.write(str(j.x))
    f.write(' ')
    for i in buttle_field.roads:
        for j in i.right_unit_list:
            f.write(str(j.y))
    f.close()


def read_game(game, buttle_field):
    """Заполняет поля классов значениями из файла last_game"""
    f = open('last_game.txt', 'r')
    game.turn = f.readline()
    game.players[0].money = f.readline()
    game.players[1].money = f.readline()
    game.max_money = f.readline()
    game.players[0].mana = f.readline()
    game.players[1].mana = f.readline()
    game.players[0].health = f.readline()
    game.players[1].health = f.readline()
    game.set_parametres(game)
    k = 0
    while f.readline() != ' ':
        buttle_field.left_unit_list[k].unit_type = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.left_unit_list[k].health = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.left_unit_list[k].x = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.left_unit_list[k].y = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.right_unit_list[k].unit_type = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.right_unit_list[k].health = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.right_unit_list[k].x = f.readline()
        k += 1
    k = 0
    while f.readline() != ' ':
        buttle_field.right_unit_list[k].y = f.readline()
        k += 1
    f.close()
