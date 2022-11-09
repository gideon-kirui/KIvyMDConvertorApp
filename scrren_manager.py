screen_helper="""
ScreenManager:
    MDScreen:
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
                        font_style: "H4"
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
                                font_size: 11
                        
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
                                font_size: 11

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
                                font_size: 11

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
                                font_size: 11

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
                                font_size: 11

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
                                font_size: 11

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
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            # md_bg_color: 190/255, 190/255,190/255, 1
                            height:dp(255)
                            spacing: '5dp'
                            padding: '10dp'
                            size_hint_y: 0.7
                            Image:
                                source: 'gidi.jpg'
                                
                            MDBoxLayout:
                                # md_bg_color: "white"
                                orientation: 'vertical'
                                radius: [50, 50]
                                MDLabel:
                                    text: 'Gideon Kirui'
                                    color: 'red'
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
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "From USD"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                hint_text: "Enter USD"
                                size_hint_x: 0.3
                                pos_hint: {'center_x':0.5}

                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding:dp(15)
                            MDLabel:
                                md_bg_color: 0.9, 0.9, 0.9, 0.1
                                text: "Convert"
                                halign: "center"
                                font_style: "H6"
                                color: "red"
                                size_hint_y: 0.3
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "To KES"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.35
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                size_hint_x: 0.3
                                pos_hint: {'center_x':0.5}
                                

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
                        padding:dp(10)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "From Meter"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                hint_text: "Enter Meter"
                                size_hint_x: 0.4
                                pos_hint: {'center_x':0.5}
                                
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding:dp(15)
                            MDLabel:
                                md_bg_color: 0.9, 0.9, 0.9, 0.1
                                text: "Convert"
                                halign: "center"
                                font_style: "H6"
                                color: "red"
                                size_hint_y: 0.3
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "To Kilometer"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.6
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}



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
                        padding:dp(10)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "From Gram"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                hint_text: "Enter Gram"
                                size_hint_x: 0.4
                                pos_hint: {'center_x':0.5}
                                
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding:dp(15)
                            MDLabel:
                                md_bg_color: 0.9, 0.9, 0.9, 0.1
                                text: "Convert"
                                halign: "center"
                                font_style: "H6"
                                color: "red"
                                size_hint_y: 0.3
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "To Kilogram"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.6
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}

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
                        padding:dp(10)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "From Second"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.6
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                hint_text: "Enter Second"
                                size_hint_x: 0.4
                                pos_hint: {'center_x':0.5}
                                
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding:dp(15)
                            MDLabel:
                                md_bg_color: 0.9, 0.9, 0.9, 0.1
                                text: "Convert"
                                halign: "center"
                                font_style: "H6"
                                color: "red"
                                size_hint_y: 0.3
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "To Minute"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.45
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}


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
                        padding:dp(10)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "From Celsius"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.6
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                hint_text: "Enter Celsius"
                                size_hint_x: 0.4
                                pos_hint: {'center_x':0.5}
                                
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding:dp(15)
                            MDLabel:
                                md_bg_color: 0.9, 0.9, 0.9, 0.1
                                text: "Convert"
                                halign: "center"
                                font_style: "H6"
                                color: "red"
                                size_hint_y: 0.3
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "To Kelvin"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.45
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}

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
                        padding:dp(10)
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "From KiloJuol"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.6
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"

                            MDTextField:
                                hint_text: "Enter Kilojuol"
                                size_hint_x: 0.4
                                pos_hint: {'center_x':0.5}
                                
                        MDBoxLayout:
                            orientation: 'vertical'
                            size_hint_y: None
                            padding:dp(15)
                            MDLabel:
                                md_bg_color: 0.9, 0.9, 0.9, 0.1
                                text: "Convert"
                                halign: "center"
                                font_style: "H6"
                                color: "red"
                                size_hint_y: 0.3
                                height: self.texture_size[1]
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                
                        MDCard:
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            size_hint: 0.98, 0.5
                            orientation: 'vertical'
                            height: self.minimum_size[1]
                            radius: [20, ]
                            spacing: '5dp'
                            padding: '10dp'

                            MDLabel:
                                text: "To Watt"
                                height: self.texture_size[1]
                                theme_text_color: 'Custom'
                                size_hint_y: None
                                size_hint_x: 0.45
                                pos_hint: {'center_x':0.5}
                                bold: True
                                font_size: 24
                                color: "white"
                                

                            MDTextField:
                                size_hint_x: 0.5
                                pos_hint: {'center_x':0.5}
                                color: [0, 0, 0, 1]
    MDScreen:
        name: 'feedback'
        md_bg_color: 83/255, 31/255, 147/255, 1
        MDBoxLayout:
            orientation: "vertical"
            padding:dp(25)
            MDBoxLayout:
                orientation: 'vertical'
                MDTopAppBar:
                    title: 'About App'
                    left_action_items: [["arrow-left", lambda x: app.Navigate_t0_homepage()]]

                MDGridLayout:
                    cols: 1
                    padding:dp(20)
                    MDCard:
                        md_bg_color: 'white'
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
                           
                        MDTextField:
                            hint_text: "Your Email"
                            size_hint_x: 0.7
                            pos_hint: {'center_x':0.5}
                            icon_right: 'email'
                            size_hint_y: None
                            
                        MDTextField:
                            hint_text: "Write Feedback"
                            size_hint_x: 0.7
                            pos_hint: {'center_x':0.5}
                            icon_right: 'message'
                            size_hint_y: None
                            
                        Button:
                            text: 'Submit Feedback'
                            pos_hint: {'center_x':0.5}
                            md_bg_color: 0.9, 0.9, 0.9, 0.1
                            color: 'white'
                            on_release: app.snackbar_tanks()
                            size_hint_y: None
                            height: self.texture_size[1]
                            size_hint_x: 0.5
                       

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