from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from scrren_manager import screen_helper

class ConvertorApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
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
    
    def get_data1(self):
        value_for_con = self.root.ids.data1.text
        con_sec = int(value_for_con) * 130
        self.root.ids.output1.text =  'KES'+ '  ' +str(con_sec)

    def get_data2(self):
        value_for_con = self.root.ids.data2.text
        con_sec = int(value_for_con)/1000
        self.root.ids.output2.text = str(con_sec) + '  ' + 'Kilometers'

    def get_data3(self):
        value_for_con = self.root.ids.data3.text
        con_sec = int(value_for_con)/1000
        self.root.ids.output3.text = str(con_sec) + '  ' + 'Kilograms'

    def get_data4(self):
        value_for_con = self.root.ids.data4.text
        con_sec = int(value_for_con)/60
        self.root.ids.output4.text = str(con_sec) + '  ' + 'Minutes'

    def get_data5(self):
        value_for_con = self.root.ids.data5.text
        con_sec = int(value_for_con)/100
        self.root.ids.output5.text = str(con_sec) + '  ' + 'Kelvin'

    def get_data6(self):
        value_for_con = self.root.ids.data6.text
        con_sec = int(value_for_con)/1000
        self.root.ids.output6.text = str(con_sec) + '  ' + 'Watts'

ConvertorApp().run()

