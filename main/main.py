from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import math
import importlib

#importlib.import_module('utils.py')

janela = Window(608, 600)

janela.set_title("Placeholder Adventure")
janela.set_background_color((0,0,0))

fundo = Sprite("imgs/pugfundo.jpg")
fundo.set_position(0,0)

pug1 = Sprite("imgs/pug.jpg")
pug1.set_position(0,200)


pug2 = Sprite("imgs/pug.jpg")
pug2.set_position(548,200)
x = 548
y = 200
speed = 300
speed_original = 300
speed_bola = [speed_original, 100]

tec = Window.get_keyboard()

bola = Sprite("imgs/bola.png")
bola.set_position((janela.width - bola.width)/2, (janela.height - bola.height)/2)
bola.col = 0

def incrementVelocity(limit_x, limit_y):

    if math.fabs(speed_bola[0]) < limit_x:
       speed_bola[0] += math.copysign(0.05 * speed_original,speed_bola[0])
       print("X : "+ str(speed_bola[0]))
    if  math.fabs(speed_bola[1]) < limit_y:
        speed_bola[1] += math.copysign(0.05 * speed_original, speed_bola[1])
        print("Y : "+ str(speed_bola[1]))


def player_update():
    if (tec.key_pressed("UP") and (pug2.y > 0)):
        pug2.move_y(-speed * janela.delta_time())
    if (tec.key_pressed("DOWN") and (pug2.y < janela.height - pug2.height)):
        pug2.move_y(speed * janela.delta_time())
    if (tec.key_pressed("W") and (pug1.y > 0)):
        pug1.move_y(-speed * janela.delta_time())
    if (tec.key_pressed("S") and (pug1.y < janela.height - pug1.height)):
        pug1.move_y(speed * janela.delta_time())

def bola_update():
    bola.move_x(speed_bola[0]*janela.delta_time())
    bola.move_y(speed_bola[1]*janela.delta_time())

    if(bola.y > janela.height - bola.height or bola.y < 0):
        speed_bola[1] *= -1
        bola.move_y(speed_bola[1]*janela.delta_time()*1.2)

    if(bola.x > janela.width - bola.width or bola.x < 0):
        speed_bola[0] *= -1
        bola.move_x(speed_bola[0]*janela.delta_time()*1.2)

    if(bola.collided(pug1) or bola.collided(pug2)):
        speed_bola[0] *= -1
        bola.move_y(speed_bola[1] * janela.delta_time() * 1.2)
        bola.col += 1

    if (bola.col == 2):
        incrementVelocity(janela.width, janela.height)
        bola.col = 0


while(True):
    fundo.draw()
    player_update()
    bola_update()
    bola.draw()
    pug2.draw()
    pug1.draw()
    janela.update()


janela.update()











