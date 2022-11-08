screen_helper="""
ScreenManager:
    MDScreen:
        name: 'home'
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
                            on_press: root.current ='currency'
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
                            on_press: root.current ='distance'
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
                            on_press: root.current ='mass'
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
                                halign:"center" 
                                color: "blue"

                        MDCard:
                            md_bg_color: 190/255, 190/255,190/255, 1
                            size_hint_y:None
                            padding:dp(10)
                            radius:dp(25)
                            height:dp(175)
                            orientation:"vertical"
                            on_press: root.current ='time'
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
                            on_press: root.current ='temprature'
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
                            on_press: root.current ='energy'
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
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'About Us'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

            BoxLayout:
                ScrollView:
                    GridLayout:
                        padding: '10dp'
                        spacing: '10dp'
                        cols: 1
                        size_hint: 1, None
                        height: self.minimum_size[1]
                        MDCard:
                            orientation: 'vertical'
                            size_hint: 0.6, None
                            height: self.minimum_size[1]
                            radius: [50, ]
                            spacing: '5dp'
                            padding: '10dp'
                            Image:
                                source: 'gidi.jpg'
                                size_hint: 0.5, None
                                height: self.texture_size[1]
                                pos_hint: {'center_x':0.5}
                            MDLabel:
                                text: 'Gideon Kirui'
                                color: 'red'
                                font_style: 'H6'
                                size_hint_y: None
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}
                                

                            MDLabel:
                                text: 'University of Embu'
                                color: 'gray'
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}

                            MDLabel:
                                text: '0712345678'
                                color: 'gray'
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}

                            MDLabel: 
                                text: 'BSc. Information Tech'
                                color: 'gray'
                                font_style: 'Caption'
                                size_hint_y: None
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}        
                
    MDScreen:
        name: 'currency'
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

                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: "Curency Convertor"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                            pos_hint: {'center_x':0.5}

    MDScreen:
        name: 'distance'
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

                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: "Distance Convertor"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                            pos_hint: {'center_x':0.5}



    MDScreen:
        name: 'mass'
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
                    
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: "Mass Convertor"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                            pos_hint: {'center_x':0.5}

    MDScreen:
        name: 'time'
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
                    
                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: "Time Convertor"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                            pos_hint: {'center_x':0.5}


    MDScreen:
        name: 'temprature'
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

                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: "Temprature Convertor"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                            pos_hint: {'center_x':0.5}

    MDScreen:
        name: 'energy'
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

                    MDBoxLayout:
                        orientation: 'vertical'
                        MDLabel:
                            text: "Energy Convertor"
                            halign: "center"
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                            pos_hint: {'center_x':0.5}

    MDScreen:
        name: 'feedback'
        MDBoxLayout:
            orientation: "vertical"
            MDBoxLayout:
                size_hint_y:.25
                padding:dp(25)
                BoxLayout:
                    orientation: 'vertical'
                    MDTopAppBar:
                        title: 'Give Feedback'
                        left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                    MDBoxLayout:
                        Button:
                            text: "Send"
                            halign: "center"
                            size_hint_y: .1
                            height: self.texture_size[1]
                            size_hint_x: 0.2
                            pos_hint: {'center_x':0.5, 'center_y':0.8}
                            on_release:app.snackbar_tanks()

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