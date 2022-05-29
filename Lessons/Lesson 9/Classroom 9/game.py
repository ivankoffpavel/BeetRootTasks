import Game.Image.open
from Game.Sound.play import *
from Game.Image import open,change,close
def draw_game():
    open.open()
    change.change()
    close.close()
draw_game()
sound()