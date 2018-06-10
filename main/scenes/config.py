from PPlay.sprite import *

class Config(object):
    def __init__(self, janela, mouse, keyboard):
        self.window = janela
        self.buttons = [Sprite("imgs/buttons/dif/0.png"),Sprite("imgs/buttons/dif/1.png"),Sprite("imgs/buttons/dif/2.png")]
        self.change = 0
        self.mouse = mouse
        self.wasPressed = True
        self.keyboard = keyboard
        self.setDif = 0

    def start(self):
        posx = self.window.width/2 - self.buttons[0].width/2
        posy = self.window.height/4
        for i in range(3):
            self.buttons[i].set_position(posx, posy * (i+1))

    def mouse_update(self):
        if not(self.wasPressed):
            for i in range(3):
                if self.mouse.is_over_object(self.buttons[i]) and self.mouse.is_button_pressed(1):
                    self.setDif = i
                    return 1
        self.wasPressed = self.mouse.is_button_pressed(1)
        return 0

    def update(self):
        self.change = self.mouse_update()

    def draw(self):
        self.window.set_background_color((0, 255, 0))
        for i in range(3):
            self.buttons[i].draw()
