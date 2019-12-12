from mathematical_parametrs import*
from decks_and_cards import*
from field import*
import tkinter as tk
import fileinput

def main():
    global root, canvas, start_button
    root = tk.Tk()
    root.geometry('800x600')
    canvas = tk.Canvas(root, bg='white')
    canvas.pack(fill=tk.BOTH, expand=1)
    start_button = tk.Button(root, text="Start")
    start_button.pack()
    start_button.bind("<Button-1>", new_game)
    root.mainloop()

def new_game(event):
    global root, canvas, game, bf, turn_button
    canvas.delete(ALL)
    start_button.pack_forget()
    bf = Buttle_field(canvas, 600, 800)
    game = Game()
    d1 = Deck(bf, 1, 40, 500)
    d2 = Deck(bf, 2, 760, 500)
    turn_button = tk.Button(root, text="End turn")
    turn_button.pack()
    turn_button.bind("<Button-1>", new_turn)
    activate_decks(game.players[0])
    bf.set_parametrs(game)

def new_turn(event):
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
    start_button.pack()
    canvas.delete(ALL)
    turn_button.pack_forget()
    

main()
