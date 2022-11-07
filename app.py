from kivymd.app import MDApp
from kivy.lang.builder import Builder  
from kivy.core.window import Window

Window.size = (350, 580)

screen_helper="""
MDScreen:
    # md_bg_color: 205/255, 205/255,205/255, 1
    MDBoxLayout:
        orientation: "vertical"
        MDBoxLayout:
            size_hint_y:.25
            padding:dp(25)
            MDBoxLayout:
                orientation: "vertical"
                MDLabel:
                    text: "Unit Convertor"
                    font_style: "H4"
                    color: "red"
                MDBoxLayout:
                    adaptive_size:True
                    spacing:dp(10)
                    MDLabel:
                        text:"Home"
                        text_size:None,None
                        adaptive_width:True
                        color: "blue"

            MDIconButton:
                icon: "cog"
                color: "blue"
                on_press: nav_ldrawer.set_state("open")
                    
        MDBoxLayout:
            ScrollView:
                MDGridLayout:
                    padding: '10dp'
                    spacing: '10dp'
                    cols: 2
                    size_hint: 1, None
                    height: self.minimum_size[1]
                    MDCard:
                        md_bg_color: 190/255, 190/255,190/255, 1
                        size_hint_y:None
                        padding:dp(10)
                        radius:dp(25)
                        height:dp(175)
                        orientation:"vertical"
                        Image:
                            radius:.5
                            source: 'gidi.jpg'
                        MDLabel:
                            text: 'Curency'
                            halign:"center"
                            font_style:"H6"  
                            color: 0/255, 100/255, 102/255, 1

                        MDLabel:
                            text: 'Convert From'
                            halign:"center"
                            font_style:"Body1" 
                            color: 255/255, 255/255, 255/255, 1 

                        MDLabel:
                            text: 'USD to KES'
                            halign:"center" 
                            color: "blue"
                    
                    MDCard:
                        md_bg_color: 190/255, 190/255,190/255, 1
                        size_hint_y:None
                        padding:dp(10)
                        radius:dp(25)
                        height:dp(175)
                        orientation:"vertical"
                        Image:
                            radius:.5
                            source: 'gidi.jpg'
                        MDLabel:
                            text: 'Distance'
                            halign:"center"
                            font_style:"H6"  
                            color: 83/255, 31/255, 147/255, 1

                        MDLabel:
                            text: 'Convert From'
                            halign:"center"
                            font_style:"Body1" 
                            color: 255/255, 255/255, 255/255, 1 

                        MDLabel:
                            text: 'Meter to Kilometer'
                            halign:"center" 
                            color: "blue"
                    MDCard:
                        md_bg_color: 190/255, 190/255,190/255, 1
                        size_hint_y:None
                        padding:dp(10)
                        radius:dp(25)
                        height:dp(175)
                        orientation:"vertical"
                        Image:
                            radius:.5
                            source: 'gidi.jpg'
                        MDLabel:
                            text: 'Mass'
                            halign:"center"
                            font_style:"H6"  
                            color: 255/255, 51/255, 153/255, 1

                        MDLabel:
                            text: 'Convert From'
                            halign:"center"
                            font_style:"Body1" 
                            color: 255/255, 255/255, 255/255, 1 

                        MDLabel:
                            text: 'Grams to Kilograms'
                            color: "blue"

                    MDCard:
                        md_bg_color: 190/255, 190/255,190/255, 1
                        size_hint_y:None
                        padding:dp(10)
                        radius:dp(25)
                        height:dp(175)
                        orientation:"vertical"
                        Image:
                            radius:.5
                            source: 'gidi.jpg'
                        MDLabel:
                            text: 'Time'
                            halign:"center"
                            font_style:"H6"  
                            color: 255/255, 153/255, 51/255, 1

                        MDLabel:
                            text: 'Convert From'
                            halign:"center"
                            font_style:"Body1" 
                            color: 255/255, 255/255, 255/255, 1 

                        MDLabel:
                            text: 'Seconds to minutes'
                            halign:"center" 
                            color: "blue"

                    MDCard:
                        md_bg_color: 190/255, 190/255,190/255, 1
                        size_hint_y:None
                        padding:dp(10)
                        radius:dp(25)
                        height:dp(175)
                        orientation:"vertical"
                        Image:
                            radius:.5
                            source: 'gidi.jpg'
                        MDLabel:
                            text: 'Temprature'
                            halign:"center"
                            font_style:"H6"  
                            color: 0/255, 153/255, 0/255, 1

                        MDLabel:
                            text: 'Convert From'
                            halign:"center"
                            font_style:"Body1" 
                            color: 255/255, 255/255, 255/255, 1 

                        MDLabel:
                            text: 'Celsius to Kelvin'
                            halign:"center" 
                            color: "blue"

                    MDCard:
                        md_bg_color: 190/255, 190/255,190/255, 1
                        size_hint_y:None
                        padding:dp(10)
                        radius:dp(25)
                        height:dp(175)
                        orientation:"vertical"
                        Image:
                            radius:.5
                            source: 'gidi.jpg'
                        MDLabel:
                            text: 'Energy'
                            halign:"center"
                            font_style:"H6"  
                            color: 255/255, 102/255, 0/255, 1

                        MDLabel:
                            text: 'Convert From'
                            halign:"center"
                            font_style:"Body1" 
                            color: 255/255, 255/255, 255/255, 1 

                        MDLabel:
                            text: 'Jouls to Watts'
                            halign:"center" 
                            color: "blue"

    MDNavigationDrawer:
        id: nav_ldrawer
        anchor: 'right'
        size_hint: (0.6, 0.3)
        pos_hint: {'center_y':0.7}
        BoxLayout:
            md_bg_color: 'dark'
            orientation: 'vertical'
            ScrollView:
            MDList:
            OneLineIconListItem:
                text: 'togle theme'
                IconLeftWidget:
                    icon: 'cog'
            OneLineIconListItem:
                text: 'Feedback'
                IconLeftWidget:
                    icon: 'chat'
            
            OneLineIconListItem:
                text: 'About'
                IconLeftWidget:
                    icon: 'information-outline'

            


<ElementCard@MDCard>:
    md_bg_color: 190/255, 190/255,190/255, 1
    size_hint_y:None
    padding:dp(2)
    radius:dp(25)
    image:""
    text: ""
    subtext: ""
    height:dp(125)
    orientation:"vertical"
    Image:
        source:'unit.png'
    MDLabel:
        halign:"center"
        font_style:"Subtitle2"
        text:root.subtext

"""

class ConvertorApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen

ConvertorApp().run()

