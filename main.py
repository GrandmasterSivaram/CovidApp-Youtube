from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import requests
from kivy.properties import ObjectProperty,NumericProperty,StringProperty
from kivymd.uix.snackbar import Snackbar


class WorldCases(FloatLayout):
    confirmed = NumericProperty()
    deaths = NumericProperty()
    recovered = NumericProperty()
    date = StringProperty()

    def search_world(self):
        api_url = 'https://covid2019-api.herokuapp.com/total'
        result = requests.get(url=api_url).json()
        self.confirmed = result['confirmed']
        self.deaths = result['deaths']
        self.recovered = result['recovered']
        self.date = result['dt']



class LiveCases(FloatLayout):
    search_input = ObjectProperty()
    location = StringProperty()
    confirmed = NumericProperty()
    deaths = NumericProperty()
    recovered = NumericProperty()

    def search(self):
        try:
            api_url = 'https://covid2019-api.herokuapp.com/v2/country/{}'
            result = requests.get(url=api_url.format(self.search_input.text)).json()
            self.location = result['data']['location']
            self.confirmed = result['data']['confirmed']
            self.deaths = result['data']['deaths']
            self.recovered = result['data']['recovered']
        except:
            Snackbar(text='No such country! Try again',font_size=20).show()





class MainApp(MDApp):
    def __init__(self,**kwargs):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette = 'Blue'
        self.theme_cls.theme_style = 'Dark'
        Window.size = (400,600)
        super().__init__(**kwargs)

MainApp().run()
