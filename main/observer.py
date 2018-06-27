from PPlay.window import *
from main.scenes.menu import *
from main.scenes.game import *
from main.scenes.config import *
from main.scenes.creditos import *

janela = Window(1080, 600)
janela.set_background_color((0, 0, 0))
janela.set_title("Placeholder Adventure")
mouse = janela.get_mouse()
keyboard = janela.get_keyboard()

dif = 0
actual_scene = 0

def change_scene(scene):
    global actual_scene,dif
    if scene == 1:
        actual_scene = Menu(janela, mouse, keyboard)
        actual_scene.start()
    elif scene == 2:
        actual_scene = Game(janela, mouse, keyboard)
        actual_scene.start()
    elif scene == 3:
        actual_scene = Config(janela, mouse, keyboard)
        actual_scene.start()
    elif scene == 4:
        actual_scene = Creditos(janela, mouse, keyboard)
        actual_scene.start()
    else:
        quit()

def draw():
    actual_scene.draw()

def update():
    global dif
    janela.update()
    actual_scene.update()
    if actual_scene.change != 0:
        try:
            dif = actual_scene.setDif
        except:
            dif = dif
        change_scene(actual_scene.change)

def loop():
    while (True):
        draw()
        update()

change_scene(1)
loop()