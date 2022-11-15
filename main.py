from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.snackbar import Snackbar
from kivymd.toast import toast
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window

Window.size = (330, 580)

screen_helper="""
ScreenManager:
    MDScreen:
        id: 'home'
        name: 'home'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                MDBoxLayout:
                    orientation: "vertical"
                    MDLabel:
                        text: "Unit Convertor"
                        font_style: "H5"
                        color: "white"
                    MDBoxLayout:
                        adaptive_size:True
                        spacing:dp(10)
                        MDLabel:
                            text:"Home"
                            text_size:None,None
                            adaptive_width:True
                            color: "orange"

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
                            md_bg_color: 0.9, 0.9, 0.9, .3
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='currency'
                            
                            MDLabel:
                                text: 'Curency'
                                halign:"center"
                                font_style:"H6" 
                                color: 83/255, 31/255, 147/255, 1

                            MDLabel:
                                text: 'Convert From'
                                halign:"center"
                                font_style:"Body1" 
                                color: 255/255, 255/255, 255/255, 1 

                            MDLabel:
                                text: 'USD to KES'
                                halign:"center" 
                                color: "blue"
                                font_size: 16
                        
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, .3
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='distance'
                            
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
                                font_size: 16

                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, .3
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='mass'
                            
                            MDLabel:
                                text: 'Mass'
                                halign:"center"
                                font_style:"H6"  
                                color: 83/255, 31/255, 147/255, 1

                            MDLabel:
                                text: 'Convert From'
                                halign:"center"
                                font_style:"Body1" 
                                color: 255/255, 255/255, 255/255, 1 

                            MDLabel:
                                text: 'Grams to Kilograms'
                                halign:"center" 
                                color: "blue"
                                font_size: 16

                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, .3
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='time'
                            
                            MDLabel:
                                text: 'Time'
                                halign:"center"
                                font_style:"H6"  
                                color: 83/255, 31/255, 147/255, 1

                            MDLabel:
                                text: 'Convert From'
                                halign:"center"
                                font_style:"Body1" 
                                color: 255/255, 255/255, 255/255, 1 

                            MDLabel:
                                text: 'Seconds to minutes'
                                halign:"center" 
                                color: "blue"
                                font_size: 16

                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, .3
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='temprature'
                            
                            MDLabel:
                                text: 'Temprature'
                                halign:"center"
                                font_style:"H6"  
                                color: 83/255, 31/255, 147/255, 1

                            MDLabel:
                                text: 'Convert From'
                                halign:"center"
                                font_style:"Body1" 
                                color: 255/255, 255/255, 255/255, 1 

                            MDLabel:
                                text: 'Celsius to Kelvin'
                                halign:"center" 
                                color: "blue"
                                font_size: 16

                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, .3
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='energy'
                            
                            MDLabel:
                                text: 'Energy'
                                halign:"center"
                                font_style:"H6"  
                                color: 83/255, 31/255, 147/255, 1

                            MDLabel:
                                text: 'Convert From'
                                halign:"center"
                                font_style:"Body1" 
                                color: 255/255, 255/255, 255/255, 1 

                            MDLabel:
                                text: 'Jouls to Watts'
                                halign:"center" 
                                color: "blue"
                                font_size: 16

        MDNavigationDrawer:
            id: nav_ldrawer
            anchor: 'right'
            size_hint: (0.6, 0.3)
            pos_hint: {'center_y':0.7}
            BoxLayout:
                md_bg_color: 'dark'
                orientation: 'vertical'
                ScrollView:
                MDSwitch:
                    #on_release: app.chdn_back_color()
     
                MDList:
                    OneLineIconListItem:
                        text: 'Feedback'
                        on_press: root.current ='feedback'
                        IconLeftWidget:
                            icon: 'chat'
                    
                    OneLineIconListItem:
                        text: 'About'
                        on_press: root.current ='about'
                        IconLeftWidget:
                            icon: 'information-outline'
               
    MDScreen:
        name: 'about'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                MDBoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'About App'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

            MDBoxLayout:
                ScrollView:
                    MDBoxLayout:
                        orientation: 'vertical'
                        padding:dp(10)
                        Image:
                            source: 'gidi.jpg'
                            
                        MDCard:
                            orientation: 'vertical'
                            md_bg_color: 0.9, 0.9, 0.9, 0.2
                            spacing: '5dp'
                            padding: '10dp'
                            size_hint_y: 0.5
                            MDLabel:
                                text: 'Gideon Kirui'
                                color: 'black'
                                font_style: 'H6'
                                height: self.texture_size[1]
                                halign: 'center'
                            
                            MDLabel:
                                text: 'University of Embu'
                                color: 'white'
                                font_style: 'Caption'
                                height: self.texture_size[1]
                                halign: 'center'
                                
                            MDLabel:
                                text: '0712345678'
                                color: 'white'
                                font_style: 'Caption'
                                height: self.texture_size[1]
                                halign: 'center'
                                
                            MDLabel: 
                                text: 'BSc. Information Tech'
                                color: 'white'
                                font_style: 'Caption'
                                height: self.texture_size[1]
                                halign: 'center'
                                    
                                            
                
    MDScreen:
        name: 'currency'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Currency (USD-KES)'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                    MDGridLayout:
                        cols: 1
                        padding:dp(20)
                        spacing: dp(15)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(5)
                            padding:dp(5)
                            MDGridLayout:
                                cols: 1
                                padding: dp(5)
                                spacing: dp(10)
                                size_hint_y:.5
                                MDLabel:
                                    text: "From"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.3}
                                    on_press: app.menu.open()

                                MDLabel:
                                    id: unit_dis
                                    text: 'USD'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                            MDTextField:
                                id: data1
                                size_hint_x: 0.4
                                halign: 'center'
                                helper_text_mode: "persistent"
                                pos_hint: {'center_x':0.5}
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]

                        MDRectangleFlatIconButton:
                            text: 'Convert'
                            icon: 'autorenew'
                            pos_hint: {'center_x':0.5}
                            color: 'white'
                            size_hint_x: 0.5
                            size_hint_y: None
                            on_release: app.get_data1()
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(10)
                            padding:dp(10)
                            MDGridLayout:
                                cols: 1
                                spacing: dp(5)
                                size_hint_y: .4
                                MDLabel:
                                    text: "To"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    size_hint_x: 0.8
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button_c
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    on_press: app.menu_c.open()

                                MDLabel:
                                    id: unit_dis_c
                                    text: 'KES'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDLabel:
                                    id: output1
                                    size_hint_x: 0.8
                                    size_hint_x: 0.4
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    color: "orange"

    MDScreen:
        name: 'distance'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Distance (M-Km)'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                    MDGridLayout:
                        cols: 1
                        padding:dp(20)
                        spacing: dp(15)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(5)
                            padding:dp(5)
                            MDGridLayout:
                                cols: 1
                                padding: dp(5)
                                spacing: dp(10)
                                size_hint_y:.5
                                MDLabel:
                                    text: "From"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button2
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.3}
                                    on_press: app.menu2.open()

                                MDLabel:
                                    id: unit_dis2
                                    text: 'Meter'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                            MDTextField:
                                id: data2
                                size_hint_x: 0.4
                                halign: 'center'
                                helper_text_mode: "persistent"
                                pos_hint: {'center_x':0.5}
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]

                        MDRectangleFlatIconButton:
                            text: 'Convert'
                            icon: 'autorenew'
                            pos_hint: {'center_x':0.5}
                            color: 'white'
                            size_hint_x: 0.5
                            size_hint_y: None
                            on_release: app.get_data2()
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(10)
                            padding:dp(10)
                            MDGridLayout:
                                cols: 1
                                spacing: dp(5)
                                size_hint_y: .4
                                MDLabel:
                                    text: "To"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    size_hint_x: 0.8
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button_c2
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    on_press: app.menu_c2.open()

                                MDLabel:
                                    id: unit_dis_c2
                                    text: 'Kilometer'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDLabel:
                                    id: output2
                                    size_hint_x: 0.8
                                    size_hint_x: 0.4
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    color: "orange"



    MDScreen:
        name: 'mass'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Mass (gram-kg)'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]
                    
                    MDGridLayout:
                        cols: 1
                        padding:dp(20)
                        spacing: dp(15)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(5)
                            padding:dp(5)
                            MDGridLayout:
                                cols: 1
                                padding: dp(5)
                                spacing: dp(10)
                                size_hint_y:.5
                                MDLabel:
                                    text: "From"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button3
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.3}
                                    on_press: app.menu3.open()

                                MDLabel:
                                    id: unit_dis3
                                    text: 'USD'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                            MDTextField:
                                id: data3
                                size_hint_x: 0.4
                                halign: 'center'
                                helper_text_mode: "persistent"
                                pos_hint: {'center_x':0.5}
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]

                        MDRectangleFlatIconButton:
                            text: 'Convert'
                            icon: 'autorenew'
                            pos_hint: {'center_x':0.5}
                            color: 'white'
                            size_hint_x: 0.5
                            size_hint_y: None
                            on_release: app.get_data3()
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(10)
                            padding:dp(10)
                            MDGridLayout:
                                cols: 1
                                spacing: dp(5)
                                size_hint_y: .4
                                MDLabel:
                                    text: "To"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    size_hint_x: 0.8
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button_c3
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    on_press: app.menu_c3.open()

                                MDLabel:
                                    id: unit_dis_c
                                    text: 'Kilogram'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDLabel:
                                    id: output3
                                    size_hint_x: 0.8
                                    size_hint_x: 0.4
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    color: "orange"

    MDScreen:
        name: 'time'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Time (sec-min)'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]
                    
                    MDGridLayout:
                        cols: 1
                        padding:dp(20)
                        spacing: dp(15)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(5)
                            padding:dp(5)
                            MDGridLayout:
                                cols: 1
                                padding: dp(5)
                                spacing: dp(10)
                                size_hint_y:.5
                                MDLabel:
                                    text: "From"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button4
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.3}
                                    on_press: app.menu4.open()

                                MDLabel:
                                    id: unit_dis4
                                    text: 'Second'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                            MDTextField:
                                id: data4
                                size_hint_x: 0.4
                                halign: 'center'
                                helper_text_mode: "persistent"
                                pos_hint: {'center_x':0.5}
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]

                        MDRectangleFlatIconButton:
                            text: 'Convert'
                            icon: 'autorenew'
                            pos_hint: {'center_x':0.5}
                            color: 'white'
                            size_hint_x: 0.5
                            size_hint_y: None
                            on_release: app.get_data4()
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(10)
                            padding:dp(10)
                            MDGridLayout:
                                cols: 1
                                spacing: dp(5)
                                size_hint_y: .4
                                MDLabel:
                                    text: "To"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    size_hint_x: 0.8
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button_c4
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    on_press: app.menu_c4.open()

                                MDLabel:
                                    id: unit_dis_c4
                                    text: 'Minute'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDLabel:
                                    id: output4
                                    size_hint_x: 0.8
                                    size_hint_x: 0.4
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    color: "orange"
                                


    MDScreen:
        name: 'temprature'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Temprature (c-k)'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                    MDGridLayout:
                        cols: 1
                        padding:dp(20)
                        spacing: dp(15)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(5)
                            padding:dp(5)
                            MDGridLayout:
                                cols: 1
                                padding: dp(5)
                                spacing: dp(10)
                                size_hint_y:.5
                                MDLabel:
                                    text: "From"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button5
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.3}
                                    on_press: app.menu5.open()

                                MDLabel:
                                    id: unit_dis5
                                    text: 'Celsius'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                            MDTextField:
                                id: data5
                                size_hint_x: 0.4
                                halign: 'center'
                                helper_text_mode: "persistent"
                                pos_hint: {'center_x':0.5}
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]

                        MDRectangleFlatIconButton:
                            text: 'Convert'
                            icon: 'autorenew'
                            pos_hint: {'center_x':0.5}
                            color: 'white'
                            size_hint_x: 0.5
                            size_hint_y: None
                            on_release: app.get_data5()
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(10)
                            padding:dp(10)
                            MDGridLayout:
                                cols: 1
                                spacing: dp(5)
                                size_hint_y: .4
                                MDLabel:
                                    text: "To"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    size_hint_x: 0.8
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button_c5
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    on_press: app.menu_c5.open()

                                MDLabel:
                                    id: unit_dis_c5
                                    text: 'Kelvin'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDLabel:
                                    id: output5
                                    size_hint_x: 0.8
                                    size_hint_x: 0.4
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    color: "orange"

    MDScreen:
        name: 'energy'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Energy (Kj-Watt)'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                    MDGridLayout:
                        cols: 1
                        padding:dp(20)
                        spacing: dp(15)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(5)
                            padding:dp(5)
                            MDGridLayout:
                                cols: 1
                                padding: dp(5)
                                spacing: dp(10)
                                size_hint_y:.5
                                MDLabel:
                                    text: "From"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button6
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.3}
                                    on_press: app.menu6.open()

                                MDLabel:
                                    id: unit_dis6
                                    text: 'Juols'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                            MDTextField:
                                id: data6
                                size_hint_x: 0.4
                                halign: 'center'
                                helper_text_mode: "persistent"
                                pos_hint: {'center_x':0.5}
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]

                        MDRectangleFlatIconButton:
                            text: 'Convert'
                            icon: 'autorenew'
                            pos_hint: {'center_x':0.5}
                            color: 'white'
                            size_hint_x: 0.5
                            size_hint_y: None
                            on_release: app.get_data6()
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing:dp(10)
                            padding:dp(10)
                            MDGridLayout:
                                cols: 1
                                spacing: dp(5)
                                size_hint_y: .4
                                MDLabel:
                                    text: "To"
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    size_hint_x: 0.8
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDRaisedButton:
                                    id: button_c6
                                    text: "Change Uint"
                                    size_hint_x: 0.5
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    on_press: app.menu_c6.open()

                                MDLabel:
                                    id: unit_dis_c6
                                    text: 'Kilojuols'
                                    height: self.texture_size[1]
                                    theme_text_color: 'Custom'
                                    size_hint_y: None
                                    halign: 'center'
                                    bold: True
                                    font_size: 24
                                    color: "white"

                                MDLabel:
                                    id: output6
                                    size_hint_x: 0.8
                                    size_hint_x: 0.4
                                    halign: 'center'
                                    pos_hint: {'center_x':0.5}
                                    color: "orange"
    MDScreen:
        name: 'feedback'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            padding:dp(25)
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: 'Feedback'
                    left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                MDGridLayout:
                    cols: 1
                    padding:dp(20)
                    MDCard:
                        md_bg_color: 0.9, 0.9, 0.9, 0.1
                        orientation: 'vertical'
                        height: self.minimum_size[1]
                        radius: [20, ]
                        spacing: dp(5)
                        padding:dp(7)
                        valign: 'center'
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0
                            size_hint: 0.98, None
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'
                            valign: 'center'
                            MDTextField:
                                hint_text: "Your Name"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'account'
                                size_hint_y: None
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]
                                icon_right_color_normal: [1,1,1,1]
                            
                            MDTextField:
                                hint_text: "Your Email"
                                size_hint_x: 0.7
                                pos_hint: {'center_x':0.5}
                                icon_right: 'email'
                                size_hint_y: None
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]
                                icon_right_color_normal: [1,1,1,1]

                        MDBoxLayout:
                            orientation: 'vertical'
                            spacing: dp(30)
                            padding: dp(10)
                            MDTextField:
                                hint_text: "Write Feedback"
                                size_hint_x: 0.98
                                pos_hint: {'center_x':0.5}
                                multiline: True
                                line_color_normal: [1,1,1,1]
                                hint_text_color_normal: [1,1,1,1]
                                line_color_focus: [1,1,1,1]
                                hint_text_color_focus: [1,1,1,1]
                                mode: 'fill'
                                fill_color_normal: [0.9,0.9,0.9, .1]
                                fill_color_focus: [0.9,0.9,0.9, .2]
                                

                            MDRectangleFlatButton:
                                text: 'Submit Feedback'
                                icon: 'message'
                                pos_hint: {'center_x':0.5}
                                color: 'white'
                                on_release: app.snackbar_tanks()
                                size_hint_x: 0.7
                
"""

class ConvertorApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(screen_helper)

        menudata1 = ['USD', 'KES',]
        menudata2 = ['Meter', 'Kilometer']
        menudata3 = ['Kilograms', 'Pounds']
        menudata4 = ['Seconds', 'Minutes']
        menudata5 = ['Celsius', 'Kelvin']
        menudata6 = ['Juols', 'Kilojuols']

################## Currency Sectctor ##################

        menu_items1 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback(x),
        } for i in menudata1
    
        ]
        self.menu = MDDropdownMenu(
        caller=self.screen.ids.button,
        items=menu_items1,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

        menu_items1 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback_c(x),
        } for i in menudata1
    
        ]
        self.menu_c = MDDropdownMenu(
        caller=self.screen.ids.button_c,
        items=menu_items1,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

################## END of Currency Sectctor ##################

################## Distance Sectctor ########################

        menu_items2 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback2(x),
        } for i in menudata2
    
        ]
        self.menu2 = MDDropdownMenu(
        caller=self.screen.ids.button2,
        items=menu_items2,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

        menu_items2 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback_c2(x),
        } for i in menudata2
    
        ]
        self.menu_c2 = MDDropdownMenu(
        caller=self.screen.ids.button_c2,
        items=menu_items2,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

################## Mass Sectctor ########################

        menu_items3 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback3(x),
        } for i in menudata3
    
        ]
        self.menu3 = MDDropdownMenu(
        caller=self.screen.ids.button3,
        items=menu_items3,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

        menu_items3 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback_c3(x),
        } for i in menudata3
    
        ]
        self.menu_c3 = MDDropdownMenu(
        caller=self.screen.ids.button_c3,
        items=menu_items3,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )
####################### End of Mass Sector #################

################## Time Sectctor ########################

        menu_items4 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback4(x),
        } for i in menudata4
    
        ]
        self.menu4 = MDDropdownMenu(
        caller=self.screen.ids.button4,
        items=menu_items4,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

        menu_items4 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback_c4(x),
        } for i in menudata4
    
        ]
        self.menu_c4 = MDDropdownMenu(
        caller=self.screen.ids.button_c4,
        items=menu_items4,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )
####################### End of Time Sector #################

################## Temprature Sectctor ########################

        menu_items5 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback5(x),
        } for i in menudata5
    
        ]
        self.menu5 = MDDropdownMenu(
        caller=self.screen.ids.button5,
        items=menu_items5,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

        menu_items5 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback_c5(x),
        } for i in menudata5
    
        ]
        self.menu_c5 = MDDropdownMenu(
        caller=self.screen.ids.button_c5,
        items=menu_items5,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )
#######################End of Temprature Sector #################

################## Energy Sectctor ########################

        menu_items6 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback6(x),
        } for i in menudata6
    
        ]
        self.menu6 = MDDropdownMenu(
        caller=self.screen.ids.button6,
        items=menu_items6,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )

        menu_items6 = [
        {
        "text": f"{i}",
        "viewclass": "OneLineListItem",
        "on_release": lambda x=f"{i}": self.menu_callback_c6(x),
        } for i in menudata6
    
        ]
        self.menu_c6 = MDDropdownMenu(
        caller=self.screen.ids.button_c6,
        items=menu_items6,
        width_mult=2,
        max_height=112,
        position="center",
        border_margin=50,
        ver_growth="up",
        )
####################### End of Energy Sector #################

################# Changing Texts for Currency ##############

    def menu_callback(self, item):
        self.root.ids.unit_dis.text = item

    def menu_callback_c(self, item):
        self.root.ids.unit_dis_c.text = item

################# END of Changing Texts for Currency ##############

################# Changing Texts for Distance ##############

    def menu_callback2(self, item):
        self.root.ids.unit_dis2.text = item

    def menu_callback_c2(self, item):
        self.root.ids.unit_dis_c2.text = item

################# END of Changing Texts for Distance ##############

################# Changing Texts for Mass ##############

    def menu_callback3(self, item):
        self.root.ids.unit_dis3.text = item

    def menu_callback_c3(self, item):
        self.root.ids.unit_dis_c3.text = item

################# END of Changing Texts for Mass ##############

################# Changing Texts for Time ##############

    def menu_callback4(self, item):
        self.root.ids.unit_dis4.text = item

    def menu_callback_c4(self, item):
        self.root.ids.unit_dis_c4.text = item

################# END of Changing Texts for Time ##############

################# Changing Texts for Temprature ##############

    def menu_callback5(self, item):
        self.root.ids.unit_dis5.text = item

    def menu_callback_c5(self, item):
        self.root.ids.unit_dis_c5.text = item

################# END of Changing Texts for Temprature ##############

################# Changing Texts for Energy ##############

    def menu_callback6(self, item):
        self.root.ids.unit_dis6.text = item

    def menu_callback_c6(self, item):
        self.root.ids.unit_dis_c6.text = item

################# END of Changing Texts for Energy ##############

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

        self.root.current = 'home'
        self.root.ids.nav_ldrawer.set_state("close")
    
################## Currency Sectctor ########################

    def get_data1(self):
        try: 
            value_for_con = int(self.root.ids.data1.text)
            con_sec = int(value_for_con) * 130
            self.root.ids.output1.text =  'KES'+ '  ' +str(con_sec)
            self.root.ids.data1.helper_text = ''
        except ValueError:
            try:
                value_for_con = float(self.root.ids.data1.text)
                con_sec = int(value_for_con) * 130
                self.root.ids.output1.text =  'KES'+ '  ' +str(con_sec)
                self.root.ids.data1.helper_text = ''
            except ValueError:
                self.root.ids.data1.helper_text = 'Enter Number please'
                self.root.ids.output1.text =  ''
                self.root.ids.data1.text = ''

################## Distance Sectctor ########################

    def get_data2(self):
        try: 
            value_for_con = int(self.root.ids.data2.text)
            con_sec = int(value_for_con)/1000
            self.root.ids.output2.text = str(con_sec) + '  ' + 'Kilometers'
            self.root.ids.data2.helper_text = ''
        except ValueError:
            try:
                value_for_con = float(self.root.ids.data2.text)
                con_sec = int(value_for_con)/1000
                self.root.ids.output2.text = str(con_sec) + '  ' + 'Kilometers'
                self.root.ids.data2.helper_text = ''
            except ValueError:
                self.root.ids.data2.helper_text = 'Enter Number please'
                self.root.ids.output2.text =  ''
                self.root.ids.data2.text = ''

################## Mass Sectctor ########################

    def get_data3(self):
        try: 
            value_for_con = int(self.root.ids.data3.text)
            con_sec = int(value_for_con)/1000
            self.root.ids.output3.text = str(con_sec) + '  ' + 'Kilograms'
            self.root.ids.data3.helper_text = ''
        except ValueError:
            try:
                value_for_con = float(self.root.ids.data3.text)
                con_sec = int(value_for_con)/1000
                self.root.ids.output3.text = str(con_sec) + '  ' + 'Kilograms'
                self.root.ids.data3.helper_text = ''
            except ValueError:
                self.root.ids.data3.helper_text = 'Enter Number please'
                self.root.ids.output3.text =  ''
                self.root.ids.data3.text = ''
        
################## Time Sectctor ########################

    def get_data4(self):
        try: 
            value_for_con = int(self.root.ids.data4.text)
            con_sec = int(value_for_con)/60
            self.root.ids.output4.text = str(con_sec) + '  ' + 'Minutes'
            self.root.ids.data4.helper_text = ''
        except ValueError:
            try:
                value_for_con = float(self.root.ids.data4.text)
                con_sec = int(value_for_con)/60
                self.root.ids.output4.text = str(con_sec) + '  ' + 'Minutes'
                self.root.ids.data4.helper_text = ''
            except ValueError:
                self.root.ids.data4.helper_text = 'Enter Number please'
                self.root.ids.output4.text =  ''
                self.root.ids.data4.text = ''

################## Temprature Sectctor ########################

    def get_data5(self):
        try: 
            value_for_con = int(self.root.ids.data5.text)
            con_sec = int(value_for_con) * 274.15
            self.root.ids.output5.text = str(con_sec) + '  ' + 'Kelvin'
            self.root.ids.data5.helper_text = ''
        except ValueError:
            try:
                value_for_con = float(self.root.ids.data5.text)
                con_sec = int(value_for_con) * 274.15
                self.root.ids.output5.text = str(con_sec) + '  ' + 'Kelvin'
                self.root.ids.data5.helper_text = ''
            except ValueError:
                self.root.ids.data5.helper_text = 'Enter Number please'
                self.root.ids.output5.text =  ''
                self.root.ids.data5.text = ''
        
################## Energy Sectctor ########################

    def get_data6(self):
        try: 
            value_for_con = int(self.root.ids.data6.text)
            con_sec = int(value_for_con)*1000
            self.root.ids.output6.text = str(con_sec) + '  ' + 'Kilojuols'
            self.root.ids.data6.helper_text = ''
        except ValueError:
            try:
                value_for_con = float(self.root.ids.data6.text)
                con_sec = int(value_for_con)*1000
                self.root.ids.output6.text = str(con_sec) + '  ' + 'Kilojuols'
                self.root.ids.data6.helper_text = ''
            except ValueError:
                self.root.ids.data6.helper_text = 'Enter Number please'
                self.root.ids.output6.text =  ''
                self.root.ids.data6.text = ''
        

    def chdn_back_color(self):
        self.root.ids.home.md_bg_color = 'white'

    def build(self):
        return self.screen

ConvertorApp().run()

