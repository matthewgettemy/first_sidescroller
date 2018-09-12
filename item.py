from kivy.uix.widget import Widget
from kivy.core.window import Window

import logging

log = logging.getLogger('mario.{}'.format(__name__))

class Item(Widget):
    def __init__(self):
        super(Item, self).__init__()

    def update(self):
        log.info('Item update.')


class Feather(Item):
    def __init__(self):
        super(Feather, self).__init__()

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
