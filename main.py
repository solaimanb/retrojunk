from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class BoxLayoutCanvas(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="Button 1")
    #     b2 = Button(text="Button 2")
    #     self.add_widget(b1)
    #     self.add_widget(b2)

class RetroWidget(Widget):
    pass

class RetroLabApp(App):
    pass

RetroLabApp().run()