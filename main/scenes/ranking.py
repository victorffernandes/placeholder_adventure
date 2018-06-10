from PPlay.sprite import *

class Ranking(object):
    def __init__(self, janela, mouse,keyboard):
        self.window = janela
        self.button_play = Sprite("imgs/buttons/jogar.png")
        self.button_dificuldade = Sprite("imgs/buttons/dificuldade.png")
        self.button_ranking = Sprite("imgs/buttons/ranking.png")
        self.button_sair = Sprite("imgs/buttons/sair.png")
        self.mouse = mouse
        self.change = 0
        self.wasPressed = True
        self.keyboard = keyboard

    def start(self):
        posx = self.window.width/2 - self.button_play.width/2
        posy = self.window.height/8
        self.button_play.set_position(posx, posy*3)
        self.button_dificuldade.set_position(posx, posy*4)
        self.button_ranking.set_position(posx, posy*5)
        self.button_sair.set_position(posx, posy*6)

    def change_update(self):
        if not(self.wasPressed):
            if (self.mouse.is_over_object(self.button_play) and self.mouse.is_button_pressed(1)):
                return 1
            if (self.mouse.is_over_object(self.button_dificuldade) and self.mouse.is_button_pressed(1)):
                return 2
            if (self.mouse.is_over_object(self.button_ranking) and self.mouse.is_button_pressed(1)):
                return 3
            if (self.mouse.is_over_object(self.button_sair) and self.mouse.is_button_pressed(1)):
                return -1
        self.wasPressed = self.mouse.is_button_pressed(1)
        return 0

    def update(self):
        self.change = self.change_update()

    def draw(self):
        self.window.set_background_color((255, 0, 0))
        self.button_play.draw()
        self.button_dificuldade.draw()
        self.button_ranking.draw()
        self.button_sair.draw()