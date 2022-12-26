from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import rgba
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("test-a35ab-firebase-adminsdk-6es2b-4348e672df.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://test-a35ab-default-rtdb.firebaseio.com/'
})

ref = db.reference('')
'''ref.push({
    'Employee':
        {
            'emp1': {
                'name': 'MISHA',
                'pass': '1234'
            }
        }
})'''
ref = db.reference('Employee')
'''ref.push({
    'name': 'MISHA2',
    'pass': '1234'
})'''
print(ref.get())


class RootScreen(MDScreen):
    pass


class FirstWindow(Screen):
    pass


class SecondWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MainApp(MDApp):

    def sent_data(self, login, password):
        data = {
            'Email': login,
            'Password': password
        }
        asd = ref.get()
        for i in asd:
            if asd[i]['name'] == login:
                if asd[i]['pass'] == password:
                    print(login +" вход успешен!")
                    return True
                else:
                    print("пароль неправильный")
            else:
                print("invalid user")



    def build(self):
        return Builder.load_file('ZXCHouse.kv')


Window.size = (324, 720)
MainApp().run()
