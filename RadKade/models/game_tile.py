import pyglet as pg

class drawable_tile:
    def __init__(self, sprite_file):
        self.drawable_image = pg.image.load(sprite_file)
        self.drawable_sprite= pg.sprite.Sprite(self.drawable_image, x=10, y=10)
        self.drawable_sprite.x = 0
        self.drawable_sprite.y = 0

    def set_sprite(self, sprite_file):
        pass

    def draw_sprite(self):
        self.drawable_sprite.draw()