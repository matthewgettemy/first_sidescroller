
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.atlas import Atlas
from kivy.graphics import Rectangle

import os
import logging
from itertools import cycle

log = logging.getLogger('mario.{}'.format(__name__))
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
BLOCK_SIZE = Window.width/18

class Hero(Widget):
    def __init__(self, pos, size):
        self.x = pos[0]
        self.y = pos[1]
        self.pos = pos
        self.size = size
        super(Hero, self).__init__()
        self.atlas = Atlas(os.path.join(ROOT_FOLDER, 'textures', 'trump.atlas'))
        self.texture = self.atlas['stand']
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size,
                                  texture=self.texture)

        self.run_frames = ['run1', 'run2', 'run3', 'run4',
                           'run5', 'run6', 'run7', 'run8']
        self.run_frame_cycle = cycle(self.run_frames)




    def update(self):
        pass
        #current_frame = next(self.run_frame_cycle)
        #self.texture = self.atlas[current_frame]
        #self.rect.texture = self.texture
