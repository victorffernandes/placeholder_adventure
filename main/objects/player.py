from PPlay.sprite import Sprite


class Player(Sprite):
    def __init__(self, image_file, speed, grav, grav_acc, jump, frames=1):
        Sprite.__init__(self, image_file, frames)
        self.speed = speed
        self.grav = grav
        self.grav_acc = grav_acc
        self.jump = jump
        #self.footCollider = [Sprite.x, Sprite.y + (9*Sprite.height)/10, Sprite.width, Sprite.y + Sprite.height]