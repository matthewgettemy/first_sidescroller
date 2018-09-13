
import os
import logging

from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.atlas import Atlas
from kivy.core.image import Image as CoreImage

log = logging.getLogger('mario.{}'.format(__name__))
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
BLOCK_SIZE = Window.width/18



class Platform(Widget):
    def __init__(self, pos, size, texture, repeat=False, uvsize=None):
        self.pos = pos
        self.size = size
        self.texture = texture
        super(Platform, self).__init__()
        if repeat:
            self.repeat = repeat
            self.uvsize = uvsize
            self.texture = self.texture
            self.texture.wrap = 'repeat'
            self.texture.uvsize = self.uvsize
        with self.canvas:
            self.platform = Rectangle(pos=self.pos, size=self.size,
                                      texture=self.texture)

    def update(self):
        pass


class GroundPlatform(Platform):
    def __init__(self, pos, size, num_blocks, block_type):
        self.pos = pos
        self.size = size
        self.num_blocks = num_blocks
        self.block_type = block_type
        self.texture = CoreImage('./textures/stone.png').texture
        super(GroundPlatform, self).__init__(self.pos, self.size, self.texture, repeat=True, uvsize=(self.num_blocks, 1))

    def update(self):
        pass


class FloatingPlatform(Platform):
    def __init__(self, pos, size, uvsize, block_type):
        self.pos = pos
        self.size = size
        self.uvsize = uvsize
        self.block_type = block_type
        self.texture = CoreImage('./textures/stone.png').texture
        super(FloatingPlatform, self).__init__(self.pos, self.size, self.texture, repeat=True, uvsize=self.uvsize)

    def update(self):
        pass


class HitBlock(Platform):
    def __init__(self, pos, size, block_type):
        self.pos = pos
        self.size = size
        self.block_type = block_type
        self.atlas = Atlas(os.path.join(ROOT_FOLDER, 'textures', 'special_blocks.atlas'))
        self.texture = self.atlas[self.block_type]

        super(HitBlock, self).__init__(self.pos, self.size, self.texture)
    def __repr__(self):
        return 'HitBlock(pos={}, type={})'.format(self.pos, self.block_type)

    def update(self):
        pass


class PlatformManager(Widget):

    def __init__(self):
        super(PlatformManager, self).__init__()
        self.ground_platforms = []
        self.floating_platforms = []
        self.hit_blocks = []
        self.all_platforms = []

    def add_ground_platform(self, **kwargs):
        gp = GroundPlatform(**kwargs)
        self.add_widget(gp)
        self.ground_platforms.append(gp)
        self.all_platforms.append(gp)

    def add_floating_platform(self, **kwargs):
        fp = FloatingPlatform(**kwargs)
        self.add_widget(fp)
        self.floating_platforms.append(fp)
        self.all_platforms.append(fp)

    def add_hit_block(self, **kwargs):
        hb = HitBlock(**kwargs)
        self.add_widget(hb)
        self.hit_blocks.append(hb)
        self.all_platforms.append(hb)

    def update(self):
        for platform in self.all_platforms:
            platform.update()