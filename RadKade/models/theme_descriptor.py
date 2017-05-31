import os
import ConfigParser
from ConfigParser import ConfigParser

class theme_container:
    def __init__(self, config_file):
        self.theme_file = config_file
        self.horizontal_bgimage = ''
        self.horizontal_logotop = ''
        self.horizontal_logoleft = ''
        self.horizontal_logoheight= ''
        self.horizontal_logowidth = ''
        self.horizontal_logofontalignment = ''
        self.horizontal_logovisible = ''
        self.horizontal_imagelistalignment = ''fd
        self.horizontal_imagelist

        self.load_theme()

    def load_theme(self):
        theme_ini = ConfigParser()
        theme_ini.read(self.theme_file)

        self.background = theme_ini.get('Horizontal', 'BGImage')
