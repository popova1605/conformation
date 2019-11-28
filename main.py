from mathematical_parametrs import*
from decks_and_cards import*
from field import*
import tkinter

def main():
    global root, canvas
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root)
    canvas.pack()
    start_button = tkinter.Button(root, text="Start")
    start_button.pack()
    start_button.bind("<Button-1>", new_game)
    root.mainloop()

def new_game(event):
    global root, canvas, game, bf
    bf = Buttle_field(canvas)
    game = Game()
    d1 = Deck(bf, 1)
    d2 = Deck(bf, 2)
    turn_button = tkinter.Button(root, text="End turn")
    turn_button.pack()
    turn_button.bind("<Button-1>", new_turn)

def new_turn(event):
    game.end_turn()
    activate_decks(game.players[game.turn-1])

main()
