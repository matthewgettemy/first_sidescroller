
import logging

from kivy.uix.widget import Widget
from kivy.core.window import Window

log = logging.getLogger('{}'.format(__name__))

class Feature(Widget):
    def __init__(self):
        super(Feature, self).__init__()

    def update(self):
        pass

class Pipe(Feature):
    def __init__(self):
        super(Pipe, self).__init__()

    def update(self):
        pass


class Button(Feature):
    def __init__(self):
        super(Button, self).__init__()

    def update(self):
        pass


class Pole(Feature):
    def __init__(self):
        super(Pole, self).__init__()

    def update(self):
        pass
