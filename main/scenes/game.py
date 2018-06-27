from PPlay.sprite import *
from main.objects.player import Player
from main.objects.box import Box

class Game(object):
    def __init__(self, janela, mouse, keyboard):
        self.window = janela
        self.mouse = mouse
        self.change = 0
        self.player = []
        self.boxes = []
        self.door = []
        self.pressPlate = []
        self.platforms = []
        self.background = []
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
            self.boxes.append(Box("imgs/box.png", 300, 2, 1))
            self.boxes[len(self.boxes)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "platform":
            self.platforms.append(Sprite("imgs/platform.png"))
            self.platforms[len(self.platforms)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "door":
            if object_settings[3] == "0":
                self.door.append(Sprite("imgs/door.png"))
            else:
                self.door.append(Sprite("imgs/door.png"))
            self.door[len(self.door)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "pressureplate":
            self.pressPlate.append(PressurePlate("imgs/pressureplate.png"))
            self.pressPlate[len(self.pressPlate)-1].set_position(int(object_settings[1]), int(object_settings[2]))
        if object_settings[0] == "background":
            self.background.append(Sprite("imgs/background.png"))
            self.background[len(self.background)-1].set_position(int(object_settings[1]), int(object_settings[2]))

    def start(self):
        self.load_level()

    def getLefBoxColliding(self, player):
        boxes = []
        for box in self.boxes:
            coliderRightPlayer = [player.x + player.width - 15, player.y, player.x + player.width,
                                  player.height + player.y - 5]
            coliderLeftBox = [box.x, box.y, box.x + 15, box.height + box.y]

            if self.mycol(coliderLeftBox, coliderRightPlayer):
                boxes.append(box)
        return boxes

    def getRightBoxColliding(self, player):
        boxes = []
        for box in self.boxes:
            coliderLeftPlayer = [player.x, player.y, player.x + 15, player.height + player.y - 5]
            coliderRightBox = [box.x + box.width - 15, box.y, box.x + box.width, box.height + box.y]
            if self.mycol(coliderRightBox, coliderLeftPlayer):
                boxes.append(box)
        return boxes

    def ctrl_player(self):
        for player in self.player:
            player.move_key_x(player.speed * self.window.delta_time())

            leftBoxes = self.getLefBoxColliding(player)
            righBoxes = self.getRightBoxColliding(player)

            if len(righBoxes) > 0 or len(leftBoxes) > 0:
                player.speed = 50
                for box in righBoxes:
                    if self.keyboard.key_pressed("LEFT"):
                        box.move_x(-50 * self.window.delta_time())

                for box in leftBoxes:
                    if self.keyboard.key_pressed("RIGHT"):
                        box.move_x(50 * self.window.delta_time())

            else:
                player.speed = 100

            for door in self.door:
                if door.collided(player) and self.canGo():
                    self.changeLevel()

            if player.x <= 0:
                player.set_position(0, player.y)
            if player.x + player.width >= self.window.width:
                player.set_position(self.window.width - player.width, player.y)

            if self.keyboard.key_pressed("SPACE") and player.groundCol:
                player.jump = -1.5
                player.move_y(player.grav * self.window.delta_time() * player.jump)

    def physics(self, obj):
        if obj.y + obj.height >= self.window.height:
            obj.grav = 300
            obj.jump = 1
            obj.groundCol = True
            obj.set_position(obj.x, self.window.height - obj.height)
        else:
            obj.groundCol = False
        for box in self.boxes:
            if obj != box:
                coliderObj = [obj.x, obj.y + obj.height - 10, obj.x + obj.width, obj.y + obj.height]
                coliderBox = [box.x, box.y, box.x + box.width, box.y + 10]
                if self.mycol(coliderObj, coliderBox):
                    obj.grav = 300
                    obj.jump = 1
                    obj.groundCol = True
                    obj.set_position(obj.x, box.y - obj.height)
                    break

        for plat in self.platforms:
            if obj.groundCol:
                break
            coliderUnderObj = [obj.x, obj.y + obj.height - 25, obj.x + obj.width, obj.y + obj.height]
            coliderOnPlat = [plat.x, plat.y, plat.x + plat.width, plat.y + 25]
            if self.mycol(coliderUnderObj, coliderOnPlat):
                obj.grav = 300
                obj.jump = 1
                obj.groundCol = True
                obj.set_position(obj.x, plat.y - obj.height)
                break
        if not obj.groundCol:
            obj.move_y(obj.grav * self.window.delta_time() * obj.jump)
            if obj.jump < 1:
                obj.jump += obj.grav_acc * self.window.delta_time()

    def mycol(self, A, B):
        if (A[0] < B[2]) and (A[2] > B[0]) and (A[1] < B[3]) and (A[3] > B[1]):
            return True
        return False

    def pressCol(self, p):
        for player in self.player:
            if p.collided(player):
                return True
        for box in self.boxes:
            if p.collided(box):
                return True
        return False

    def canGo(self):
        for p in self.pressPlate:
            p.col = self.pressCol(p)
            if not p.col:
                return p.col
        return True

    def changeLevel(self):
        self.player = []
        self.boxes = []
        self.pressPlate = []
        self.door = []
        self.platforms = []
        self.level += 1
        try:
            self.load_level()
        except:
            self.change = 1
    def change_update(self):
        if self.keyboard.key_pressed("ESC"):
            return 1
        return 0

    def update(self):
        self.change = self.change_update()
        self.ctrl_player()
        for p in self.player:
            self.physics(p)
        for box in self.boxes:
            self.physics(box)

    def draw(self):
        self.window.set_background_color((255, 255, 255))
        for back in self.background:
            back.draw()
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
        self.col = False
