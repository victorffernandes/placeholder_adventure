from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
#import
import importlib

#importlib.import_module('utils.py')

janela = Window(900, 650)

janela.set_title("Placeholder Adventure")
janela.set_background_color((0,0,255))

img = Sprite("imgs/pug.jpg")
img.set_position(450,325)

while(True):
    img.draw()
    janela.update()


janela.update()











