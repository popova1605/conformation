from mathematical_parametrs import*
from decks_and_cards import*
from field import*
import tkinter as tk
import fileinput


def main():
    global root, canvas, frame, start_button
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    #f = open('last_game.txt', 'r')
    #s = f.readline()
    if True:
        frame = tk.Frame(root)
        frame.pack(side=tk.BOTTOM)
        start_button = tk.Button(frame, text="новая игра")
        saved_button = tk.Button(frame, text="Продолжить сохранённую игру")
        start_button.pack(side=tk.LEFT)
        saved_button.pack(side=tk.RIGHT)
        
        start_button.bind("<Button-1>", new_game)
    root.mainloop()


def new_game(event):
    global root, canvas, game, bf, turn_button
    canvas.delete(ALL)
    frame.pack_forget()
    bf = Buttle_field(root, canvas, 600, 800)
    game = Game()
    dr1 = Deck(bf, "Rogue", 1, 40, 500)
    dk1 = Deck(bf, "Knight", 1, 100, 500)
    dr2 = Deck(bf, "Rogue", 2, 760, 500)
    dk2 = Deck(bf, "Knight", 2, 600, 500)
    turn_button = tk.Button(root, text="End turn")
    turn_button.pack()
    turn_button.bind("<Button-1>", new_turn)
    activate_decks(game.players[0])
    bf.set_parametrs(game)


def new_turn(event):
    global turn_button
    turn_button.bind("<Button-1>", "")
    game.end_turn()
    bf.move_roads(game)
    bf.set_parametrs(game)
    fail = game.check_fail()
    if fail:
        finish_game()
        if fail == 1:
            canvas.create_text(400, 300, text = "Выиграл игрок 1")
        elif fail == 2:
            canvas.create_text(400, 300, text = "Выиграл игрок 2")
        else:
            canvas.create_text(400, 300, text = "Ничья")
    else:
        if game.turn == 1:
            activate_decks(game.players[0])
        else:
            activate_decks(game.players[1])
    turn_button.bind("<Button-1>", new_turn)


def finish_game():
    global game, bf
    frame.pack()
    start_button.pack()
    canvas.delete(ALL)
    turn_button.pack_forget()
    

main()
