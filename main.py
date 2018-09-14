
import os
import logging

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.config import Config
from kivy.utils import platform
from kivy.core.window import Window


import item
import floor
import enemy
import feature
import hero
import user_input


if platform == 'android':
    Config.set('graphics', 'fullscreen', 1)
    Config.write()
elif platform == 'win':
    Config.set('graphics', 'fullscreen', '0')
    Config.write()
    Window.size = (1200, 720)

BLOCK_SIZE = Window.width/18

class World(Widget):
    def __init__(self, log):
        self.log = log
        self.log.info('Initializing World.')
        super(World, self).__init__()

        self.input_controller = user_input.InputController(platform)
        self.add_widget(self.input_controller)

    def initialize_world(self):
        self.log.info('Adding initial elements to world.')

        self.pfm = floor.PlatformManager()
        self.add_widget(self.pfm)
        self.pfm.add_ground_platform(pos=(0, 0), size=(BLOCK_SIZE*10, BLOCK_SIZE), num_blocks=10, block_type='question_block')
        self.pfm.add_hit_block(pos=(BLOCK_SIZE*9, BLOCK_SIZE*3), size=(BLOCK_SIZE, BLOCK_SIZE), block_type='yellow_block')
        self.pfm.add_floating_platform(pos=(BLOCK_SIZE*10, BLOCK_SIZE*3), size=(BLOCK_SIZE*5, BLOCK_SIZE*2), uvsize=(5,2), block_type='yellow_block')

        self.im = item.ItemManager()
        self.add_widget(self.im)
        self.im.add_feather(pos=(300, 300), size=(BLOCK_SIZE, BLOCK_SIZE), type='feather')
        self.im.add_feather(pos=(600, 500), size=(BLOCK_SIZE, BLOCK_SIZE), type='feather')


        mario = hero.Hero(pos=(BLOCK_SIZE, BLOCK_SIZE), size=(BLOCK_SIZE*2, BLOCK_SIZE*2.5))
        ground = floor.GroundPlatform(pos=(0, 0), size=(BLOCK_SIZE*10, BLOCK_SIZE), num_blocks=10, block_type='question_block')
        hitblock = floor.HitBlock(pos=(BLOCK_SIZE, BLOCK_SIZE), size=(BLOCK_SIZE, BLOCK_SIZE), block_type='yellow_block')
        koopa = enemy.Koopa()
        pipe = feature.Pipe()
        self.add_widget(mario)
        self.add_widget(ground)
        self.add_widget(hitblock)
        self.add_widget(koopa)
        self.add_widget(pipe)
        self.log.info('Done adding initial elements to world.')

        self.input_controller.bring_touchscreen_components_to_front()

    def update(self):
        self.log.debug('World update.')
        for child in self.children:
            self.log.debug('{} update.'.format(child.__class__.__name__))
            child.update()
            #print(repr(child))


class GUI(Widget):
    def __init__(self, root_folder, log):
        self.root_folder = root_folder
        self.log = log
        self.log.info('Initializing GUI.')
        super(GUI, self).__init__()

        self.world = World(self.log)
        self.world.initialize_world()
        self.add_widget(self.world)

    def update(self, dt):
        self.log.debug('GUI update.')
        self.world.update()

class Application(App):

    def build(self):
        root_folder = os.path.dirname(os.path.abspath(__file__))
        log = configure_logger(root_folder)
        log.info('Beginning build process.')
        log.info('ROOT FOLDER: {}'.format(root_folder))
        parent = Widget()
        gui = GUI(root_folder, log)
        log.info('Done initializing GUI.')
        parent.add_widget(gui)
        interval = 1.0/60.0
        log.info('Scheduling update interval for {} seconds.'.format(interval))
        Clock.schedule_interval(gui.update, interval)
        return parent

def configure_logger(root_folder):
    log = logging.getLogger('{}'.format('mario'))
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(name)s: %(message)s')
    sh = logging.StreamHandler()
    fh = logging.FileHandler(os.path.join(root_folder, 'mario.log'), mode='w')
    sh.setFormatter(formatter)
    sh.setLevel(logging.INFO)
    fh.setFormatter(formatter)
    fh.setLevel(logging.DEBUG)
    log.addHandler(sh)
    log.addHandler(fh)

    return log


if __name__ == '__main__' :
    Application().run()