import pyglet as pg
import os

from models import list_builder
from models.list_builder import *
from models.game_tile import *
from models.theme_descriptor import theme_container

#initilize all global variables
current_list = list_builder.generate_list("main_menu")

drawable_tiles = []
theme_configuration = theme_container('C:\img\mameroom.mll')

class radkade_frontend(object):
    def start(self):
        self.window = pg.window.Window(1024, 768, caption='RadKade')
        self.window.set_handlers(self)

        pg.app.run()

    def on_draw(self):
        self.window.clear()

        #draw the tiles
        for number in drawable_tiles:
            number.draw_sprite()

    def on_key_press(self, symbol, modifiers):
        print(symbol)

def entry_point():
    rkfe = radkade_frontend()
    rkfe.start()

if __name__ == '__main__':
    entry_point()
