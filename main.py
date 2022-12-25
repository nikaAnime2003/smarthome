from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import rgba
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen


class RootScreen(MDScreen):
    pass


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):
    def build(self):
        return Builder.load_file('ZXCHouse.kv')


Window.size = (324, 720)
MainApp().run()
