from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from scrren_manager import screen_helper
from kivy.core.window import Window

Window.size = (350, 580)

class ConvertorApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

    def Navigate_t0_homepage(self):
        self.root.current = 'home'

    def snackbar_tanks(self):
        self.snackbar = Snackbar(
            text="[color=#000000] Thanks for your feedback ",
            bg_color=(1, 1, 1, 1),
            snackbar_animation_dir="Top",
            font_size='16sp',
        )
        self.snackbar.open()

        toast('Feedback Sent Succesfully')
        pass

ConvertorApp().run()

