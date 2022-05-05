from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget

class StackLayoutEx(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for x in range(100):
            size='100dp'
            b=Button(text=str(x+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)


class MyLayout(BoxLayout):
    pass

'''    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        b1=Button(text='Yuri')
        b2=Button(text='Aline')
        self.add_widget(b1)
        self.add_widget(b2)
'''

class MainWidget(Widget):
    pass

class LabApp(App):
    pass

LabApp().run()
