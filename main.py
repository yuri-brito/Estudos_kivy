from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.utils import get_color_from_hex
from kivymd.app import MDApp
from kivymd.uix.datatables.datatables import MDDataTable
from kivy.lang import Builder
import pandas as pd
from kivy.metrics import  dp
from kivymd.uix.screen import MDScreen

'''class StackLayoutEx(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        for x in range(100):
            size='100dp'
            b=Button(text=str(x+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)
    pass'''

'''class MyLayout(BoxLayout):
    pass'''

'''    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation='vertical'
        b1=Button(text='Yuri')
        b2=Button(text='Aline')
        self.add_widget(b1)
        self.add_widget(b2)
'''
class MyMDTable(MDDataTable):
    pass


'''class MainWidget(Widget):
    pass'''

class Lab3App(MDApp):
    def build(self):
        screen=MDScreen()
        df=pd.read_csv('titanic.csv')
        lista_col=[]
        for col in df.columns.to_list():
            sum=0
            for x in df[col]:
                sum+=len(str(x))
            media=sum/(len(df[col]))
            if len(col)>media:
                prop=len(col)
            else:
                prop=media
            if col == 'Name':
                tupla=(f'[size=14][color=#063970]{col}[/color][/size]',dp(3*prop),self.filter_on_name)
                lista_col.append(tupla)
            else:
                tupla=(f'[size=14][color=#063970]{col}[/color][/size]',dp(3*prop))
                lista_col.append(tupla)

        lista_row=[]

        for x in range(len(df)):
            temp_list=[]
            for y in range(len(df.columns.to_list())):
                temp_list.append(f'[size=12]{df.iloc[x,y]}[/size]')
            lista_row.append(tuple(temp_list))
        table=MDDataTable(sorted_on="Age",
                          sorted_order="ASC",
                          elevation=30,
                          pos_hint={'center_x':0.5,'center_y':0.5},
                          size_hint=(0.95,0.8),
                          check=True,
                          use_pagination=True,
                          pagination_menu_pos="auto",
                          pagination_menu_height=dp(240),
                          background_color=[0.5,0.5,0.5,1],
                          background_color_header=get_color_from_hex('#abdbe3'),
                          background_color_cell=get_color_from_hex('#eeeee4'),
                          background_color_selected_cell =get_color_from_hex('#62c8df'),
                          rows_num=891,
                          theme_cls='Dark',
                          column_data=lista_col,row_data=lista_row)

        screen.add_widget(table)
        #return Builder.load_file('Lab2.kv')
        return screen
    def filter_on_name(self,data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

Lab3App().run()
