from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import rgba
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


def display_user_tokens(self):
    self.root.ids.the_label.text = "local_id: " + self.local_id + "\n user_idToken: " + self.user_idToken


def sign_out(self):
    self.root.ids.firebase_login_screen.log_out()
    self.root.current = 'firebase_login_screen'


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file('main.kv')


Window.size = (324, 720)
MainApp().run()
