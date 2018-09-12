
import logging

from kivy.uix.widget import Widget
from kivy.core.window import Window

log = logging.getLogger('{}'.format(__name__))


class Hero(Widget):
    def __init__(self):
        super(Hero, self).__init__()

    def update(self):
        pass
