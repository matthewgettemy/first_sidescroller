from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse
from kivy.core.window import Window
from kivy.utils import platform
from kivy.config import Config

BLOCK_SIZE = Window.width/18


if platform == 'win':
    Config.set('graphics', 'fullscreen', 1)
    Config.write()
elif platform == 'win':
    Config.set('graphics', 'fullscreen', '0')
    Config.write()
    Window.size = (100, 720)

