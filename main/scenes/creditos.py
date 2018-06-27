from PPlay.sprite import *

class Creditos(object):
    def __init__(self, janela, mouse,keyboard):
        self.window = janela
        self.background = Sprite("imgs/creditos_background.png")
        self.mouse = mouse
        self.change = 0
        self.wasPressed = True
        self.keyboard = keyboard

    def start(self):
        self.background.set_position(0, 0)

    def change_update(self):
        if not(self.wasPressed):
            if (self.mouse.is_button_pressed(1)):
                return 1
        if self.keyboard.key_pressed("ESC"):
            return 1
        self.wasPressed = self.mouse.is_button_pressed(1)
        return 0

    def update(self):
        self.change = self.change_update()

    def draw(self):
        self.window.set_background_color((255, 0, 0))
        self.background.draw()