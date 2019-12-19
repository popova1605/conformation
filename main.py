from mathematical_parametrs import*
from decks_and_cards import*
from field import*
import tkinter as tk
import fileinput


def main():
    global root, canvas, frame, start_button, photo
    root = tk.Tk()
    root.geometry('800x600')
    photo = PhotoImage(file='bcg.png')
    canvas = tk.Canvas(root)
    canvas.pack(fill=tk.BOTH, expand=1)
    frame = tk.Frame(root)
    frame.pack(side=tk.BOTTOM)
    start_button = tk.Button(frame, text="новая игра")
    start_button.pack()
    start_button.bind("<Button-1>", new_game)
    root.mainloop()


def new_game(event):
    global root, canvas, game, bf, turn_button1, turn_button2, decks, background
    canvas.delete(ALL)
    background = canvas.create_image(400, 300, image = photo)
    frame.pack_forget()
    bf = Buttle_field(root, canvas, 600, 800)
    game = Game()
    decks = []
    decks.append(Deck(bf, "Rogue", 1, 40, 500))
    decks.append(Deck(bf, "Knight", 1, 100, 500))
    decks.append(Deck(bf, "Mage", 1, 161, 500))
    decks.append(Deck(bf, "Necromancer", 2, 660, 500))
    decks.append(Deck(bf, "Overseer", 2, 600, 500))
    decks.append(Deck(bf, "Elemental", 2, 540, 500))
    turn_button1 = tk.Button(root, text="Закончить ход")
    turn_button2 = tk.Button(root, text="Закончить ход")
    turn_button1.pack(side = tk.LEFT)
    turn_button1.bind("<Button-1>", new_turn)
    activate_decks(game.players[0])
    bf.set_parametrs(game)


def new_turn(event):
    global turn_button1, button2
    game.end_turn()
    bf.move_roads(game)
    bf.set_parametrs(game)
    fail = game.check_fail()
    if fail:
        finish_game()
    else:
        if game.turn == 1:
            activate_decks(game.players[0])
            turn_button1.pack(side = tk.LEFT)
            turn_button1.bind("<Button-1>", new_turn)
            turn_button2.pack_forget()
            turn_button2.bind("<Button-1>", "")
        else:
            activate_decks(game.players[1])
            turn_button2.pack(side = tk.RIGHT)
            turn_button2.bind("<Button-1>", new_turn)
            turn_button1.pack_forget()
            turn_button1.bind("<Button-1>", "")


def finish_game():
    global game, bf
    fail = game.check_fail()
    canvas.delete(ALL)
    if fail == 1:
        canvas.create_text(400, 300, text = 'Выиграл игрок 1')
    elif fail == 2:
        canvas.create_text(400, 300, text = "Выиграл игрок 2", font = 10)
    else:
        canvas.create_text(400, 300, text = "Ничья", font = 10)
    frame.pack()
    start_button.pack()
    turn_button1.pack_forget()
    turn_button2.pack_forget()


main()
