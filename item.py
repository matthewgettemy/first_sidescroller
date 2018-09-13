from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.atlas import Atlas
from kivy.graphics import Rectangle

import os
import logging

log = logging.getLogger('mario.{}'.format(__name__))
ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
BLOCK_SIZE = Window.width/18


class Item(Widget):
    def __init__(self, pos, size, type):
        self.pos = pos
        self.size = size
        self.type = type
        super(Item, self).__init__()
        self.atlas = Atlas(os.path.join(ROOT_FOLDER, 'textures', 'items.atlas'))
        self.texture = self.atlas[self.type]
        with self.canvas:
            self.platform = Rectangle(pos=self.pos, size=self.size,
                                      texture=self.texture)


    def update(self):
        log.info('Item update.')


class Feather(Item):
    def __init__(self, pos, size, type):
        self.pos = pos
        self.size = size
        self.type = type
        super(Feather, self).__init__(self.pos, self.size, self.type)

    def update(self):
        pass


class Mushroom(Item):
    def __init__(self):
        super(Mushroom, self).__init__()

    def update(self):
        pass


class Star(Item):
    def __init__(self):
        super(Star, self).__init__()

    def update(self):
        pass


class FireFlower(Item):
    def __init__(self):
        super(FireFlower, self).__init__()

    def update(self):
        pass


class ItemManager(Widget):

    def __init__(self):
        super(ItemManager, self).__init__()
        self.feathers = []
        self.mushrooms = []
        self.stars = []
        self.fireflowers = []
        self.all_items = []

    def add_feather(self, **kwargs):
        feather = Feather(**kwargs)
        self.add_widget(feather)
        self.feathers.append(feather)
        self.all_items.append(feather)

    def add_mushroom(self, **kwargs):
        fp = Mushroom(**kwargs)
        self.add_widget(fp)
        self.mushrooms.append(fp)
        self.all_items.append(fp)

    def add_star(self, **kwargs):
        hb = Star(**kwargs)
        self.add_widget(hb)
        self.stars.append(hb)
        self.all_items.append(hb)

    def add_fireflower(self):
        hb = Star(**kwargs)
        self.add_widget(hb)
        self.fireflowers.append(hb)
        self.all_items.append(hb)

    def update(self):
        for item in self.all_items:
            item.update()