from PPlay.sprite import Sprite

class Box (Sprite):
    def __init__(self, image_file, grav, grav_acc, jump, frames = 1):
        Sprite.__init__(self, image_file, frames)
        self.grav = grav
        self.grav_acc = grav_acc
        self.jump = jump
        self.groundCol = False
        self.speed = 0