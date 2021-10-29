from kivymd.app import MDApp
from kivy.lang import Builder
from kivy import properties as p

from manager.navigation import NavigationManager


class MainSreenManager(NavigationManager):
    pass


with open('main.kv', encoding='utf-8') as f:
    Builder.load_string(f.read())


class Kvtemplate5App(MDApp):
    manager = p.ObjectProperty(None)

    def build(self):
        self.manager = MainSreenManager()
        return self.manager

    def on_start(self):
        pass

if __name__ == '__main__':
    Kvtemplate5App().run()
