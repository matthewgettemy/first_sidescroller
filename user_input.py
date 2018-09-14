from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Ellipse
from kivy.core.window import Window
from kivy.config import Config

BLOCK_SIZE = Window.width/18


class InputController(Widget):

    def __init__(self, platform):
        self.platform = platform
        super(InputController, self).__init__()

        if self.platform == 'win':
            self.keyboard = Window.request_keyboard(self._keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.handle_key_down)
            self.keyboard.bind(on_key_up=self.handle_key_up)
            self.initialize_touchscreen_components()
        elif self.platform == 'android':
            pass

    def _keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self._on_keyboard_down)
        self.keyboard = None

    def handle_key_down(self, keyboard, keycode, text, modifiers):
        button = keycode[1]
        print(button)

    def handle_key_up(self, keyboard, keycode):
        button = keycode[1]
        print(button)

    def initialize_touchscreen_components(self):
        #self.jump_button = JumpButton(self.level.hero)
        self.jump_button = JumpButton()
        self.add_widget(self.jump_button)
        self.move_buttons = MoveButtons()
        self.add_widget(self.move_buttons)
        self.bring_touchscreen_components_to_front()

    def bring_touchscreen_components_to_front(self):
        print('bringing them to the front')
        if self.jump_button:
            self.remove_widget(self.jump_button)
            self.add_widget(self.jump_button)
        if self.move_buttons:
            self.move_buttons.bring_to_front()

    def update(self):
        pass

class JumpButton(Widget):

    def __init__(self): # character):
        # self.character = character
        super(JumpButton, self).__init__()
        self.size = (BLOCK_SIZE*2, BLOCK_SIZE*2)
        self.pos = (Window.width-self.size[0]*1.5, self.size[1]/2)

        with self.canvas:
            self.opacity = .25
            self.jump_button = Ellipse(pos=self.pos,
                                       size=self.size)
    def on_touch_down(self, touch):
        if touch.x > (Window.width/2):
            if self.collide_point(touch.x, touch.y):
                print('jump button down.')
                # if self.character.jump and self.character.on_ground:
                #     self.character.vel_y = HERO_JUMP_SPEED
                #     self.character.on_ground = False
                # self.character.jump = False

    def on_touch_up(self, touch):
        if touch.x > (Window.width/2):
            print('jump button up.')
            #self.character.jump = True


class MoveButton(Widget):

    def __init__(self, pos):
        self.pos = pos
        super(MoveButton, self).__init__()
        self.size = (BLOCK_SIZE*2, BLOCK_SIZE)

        with self.canvas:
            self.opacity = .25
            self.rect = Rectangle(pos=self.pos,
                                  size=self.size)


class MoveButtons(Widget):

    def __init__(self):  # , level):
        #self.level = level
        super(MoveButtons, self).__init__()
        self.move_left_button = MoveButton((BLOCK_SIZE, BLOCK_SIZE*1.5))
        self.move_right_button = MoveButton((BLOCK_SIZE * 3, BLOCK_SIZE*1.5))
        self.add_widget(self.move_right_button)
        self.add_widget(self.move_left_button)

    def bring_to_front(self):
        self.remove_widget(self.move_left_button)
        self.remove_widget(self.move_right_button)
        self.add_widget(self.move_left_button)
        self.add_widget(self.move_right_button)

    def on_touch_down(self, touch):
        self.on_touch_move(touch)

    def on_touch_move(self, touch):
        if touch.x < (Window.width / 2):
            if self.move_left_button.collide_point(*touch.pos):
                print('move left')
                # self.level.move_right = False
                # self.level.move_left = True
            elif self.move_right_button.collide_point(*touch.pos):
                print('move right')
                # self.level.move_left = False
                # self.level.move_right = True
            else:
                print('stop moving')
                # self.level.move_right = False
                # self.level.move_left = False

    def on_touch_up(self, touch):
        if touch.x < (Window.width / 2):
            print('stop moving')
            # self.level.move_left = False
            # self.level.move_right = False