from PPlay.sprite import Sprite

class Box (Sprite):
    def __init__(self, image_file, frames):
        Sprite.__init__(self, image_file, frames)

    def up_Collision(self, collider):
        return 0