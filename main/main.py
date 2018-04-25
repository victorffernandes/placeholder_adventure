from PPlay.window import *
from PPlay.sprite import *
import math
import random

janela = Window(608, 600)

janela.set_title("Placeholder Adventure")
janela.set_background_color((0,0,0))

fundo = Sprite("imgs/pugfundo.jpg")
fundo.set_position(0,0)

pug1 = Sprite("imgs/pug.jpg")
pug1.set_position(0,(janela.height/2) - pug1.height)

pug2 = Sprite("imgs/pug.jpg")
pug2.set_position(janela.width - pug2.width,  (janela.height/2) - pug2.height)
x = 548
y = 200
speed = 300
speed_original = 300
speed_bola = [speed_original, speed_original/3]
offset = janela.width /4

frame_show = 0
frame_rate = 0
frames = 0

tec = Window.get_keyboard()
mouse = Window.get_mouse()

bola = Sprite("imgs/bola.png")
bola.set_position((janela.width - bola.width)/2, (janela.height - bola.height)/2)
bola.col = 0

player_point = [0,0]

def incrementVelocity(limit_x, limit_y):

    if math.fabs(speed_bola[0]) < limit_x:
       speed_bola[0] += math.copysign(0.05 * speed_original,speed_bola[0])
       print("X : "+ str(speed_bola[0]))
    if math.fabs(speed_bola[1]) < limit_y:
        speed_bola[1] += math.copysign(0.05 * speed_original, speed_bola[1])
        print("Y : "+ str(speed_bola[1]))

def text_draw():
    global offset
    janela.draw_text(str(player_point[0]),
                     offset, 0, 50, (255, 255, 255), "Calibri")
    janela.draw_text(str(player_point[1]),
                            janela.width - offset, 0, 50, (255, 255, 255), "Calibri")


def player_update():
    global mouse
    if (mouse.get_position()[1]  < pug2.y + pug2.height/2 and (pug2.y > 0)):
        pug2.move_y(-speed * janela.delta_time())
    if (mouse.get_position()[1] > pug2.y + pug2.height/2 and (pug2.y < janela.height - pug2.height)):
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

    if(bola.x < 0):
        player_point[0] += 1
        bola.set_position((janela.width - bola.width) / 2, (janela.height - bola.height) / 2)
        r = -1 if random.randint(0,1) == 0 else 1
        speed_bola[0] = speed_original * r
        speed_bola[1] = -r * speed_original / 3

    if(bola.x > janela.width - bola.width):
        player_point[1] += 1
        bola.set_position((janela.width - bola.width) / 2, (janela.height - bola.height) / 2)
        r = -1 if random.randint(0,1) == 0 else 1
        speed_bola[0] = speed_original * r
        speed_bola[1] =  -r *speed_original / 3

    if(bola.collided(pug1) or bola.collided(pug2)):
        speed_bola[0] *= -1
        bola.move_y(speed_bola[1] * janela.delta_time() * 1.2)
        bola.col += 1

    if (bola.col == 2):
        incrementVelocity(janela.width, janela.height)
        bola.col = 0

def frame_update():
    global frame_rate, frames, frame_show
    frame_rate += janela.delta_time()
    frames += 1
    if(frame_rate >= 1):
        frame_show = frames #1/janela.delta_time()
        frames = 0
        frame_rate = 0
    janela.draw_text(str(int(frame_show)),
                     (janela.width / 2) - 50, 0, 50, (255, 255, 255), "Calibri")


while(True):
    fundo.draw()
    player_update()
    bola_update()
    bola.draw()
    pug2.draw()
    pug1.draw()
    text_draw()
    frame_update()
    janela.update()