from PPlay.sprite import *
from main.objects.player import Player

class Game(object):
    def __init__(self, janela, mouse, keyboard, dif):
        self.window = janela
        self.mouse = mouse
        self.change = 0
        self.player = []
        self.boxes = []
        self.door = []
        self.pressPlate = []
        self.platforms = []
        self.keyboard = keyboard
        self.level = 1

    def load_level(self):
        with open("levels/"+str(self.level) + ".txt", "r") as f:
            for line in f:
                self.load_object(line)

    def load_object(self, l):
        object_settings = l.split("#")
        if object_settings[0] == "player":
            self.player.append(Player("imgs/player.png", 100, 300, 2, 1))
            self.player[len(self.player)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "box":
            self.boxes.append(Sprite("imgs/box.png"))
            self.boxes[len(self.boxes)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "platform":
            self.platforms.append(Sprite("imgs/platform.png"))
            self.platforms[len(self.platforms)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "door":
            self.door.append(Sprite("imgs/door.png"))
            self.door[len(self.door)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "pressureplate":
            self.pressPlate.append(PressurePlate("imgs/pressureplate.png"))
            self.pressPlate[len(self.pressPlate)-1].set_position(int(object_settings[1]), int(object_settings[2]))


    def start(self):
        self.load_level()

    def ctrl_player(self):
        for player in self.player:
            player.move_key_x(player.speed * self.window.delta_time())

            for box in self.boxes:
                if player.collided(box):
                    if player.y + player.height == box.height + box.y:
                        player.speed = 50
                        box.move_key_x(player.speed * self.window.delta_time())
                    if player.y + player.height >= box.y:
                        player.jump = 1
                        player.grav = 300
                        if self.keyboard.key_pressed("SPACE"):
                            player.jump = -1.5
                            player.move_y(player.grav * self.window.delta_time() * player.jump)
                if not(player.collided(box) and player.y + player.height == box.height + box.y):
                    player.speed = 100

                for pressPlate in self.pressPlate:
                    if pressPlate.collided(player):
                        if pressPlate.col != "player":
                            text_1 = ""
                            pressPlate.col = "player"
                       # change_text(text_pressed_player)
                    elif pressPlate.collided(box):
                        if pressPlate.col != "box":
                            text_1 = ""
                            pressPlate.col = "box"
                      #  change_text(text_pressed_box)
                    else:
                        if pressPlate.col != "nothing":
                            text_1 = ""
                            pressPlate.col = "nothing"
                     #   change_text(text_intro)

            if player.x <= 0:
                player.set_position(0, player.y)
            if player.x + player.width >= self.window.width:
                player.set_position(self.window.width - player.width, player.y)

            if player.y + player.height >= self.window.height:
                player.jump = 1
                player.grav = 300
                if player.y + player.height >= self.window.height:
                    player.set_position(player.x, self.window.height - player.height)
                if self.keyboard.key_pressed("SPACE"):
                    player.jump = -1.5
                    player.move_y(player.grav * self.window.delta_time() * player.jump)

            else:
                player.jump += player.grav_acc * self.window.delta_time()
                player.move_y(player.grav * self.window.delta_time() * player.jump)

    def change_update(self):
        if self.keyboard.key_pressed("ESC"):
            return 1
        return 0

    def update(self):
        self.change = self.change_update()
        self.ctrl_player()

    def draw(self):
        self.window.set_background_color((255, 255, 255))
        for p in self.player:
            p.draw()
        for box in self.boxes:
            box.draw()
        for plate in self.pressPlate:
            plate.draw()
        for door in self.door:
            door.draw()
        for platform in self.platforms:
            platform.draw()

class PressurePlate(Sprite):
    def __init__(self, image_file, frames=1):
        Sprite.__init__(self, image_file, frames)
        self.col = "nothing"
