
import logging

from kivy.uix.widget import Widget
from kivy.core.window import Window

log = logging.getLogger('{}'.format(__name__))

class Enemy(Widget):
    def __init__(self):
        super(Enemy, self).__init__()


class Koopa(Enemy):
    def __init__(self):
        super(Koopa, self).__init__()

    def update(self):
        pass


class BulletBill(Enemy):
    def __init__(self):
        super(BulletBill, self).__init__()

    def update(self):
        pass


class FireToad(Enemy):
    def __init__(self):
        super(FireToad, self).__init__()

    def update(self):
        pass

