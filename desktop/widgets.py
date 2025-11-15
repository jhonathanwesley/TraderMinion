"""
Widgets customizados para Kivy
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.metrics import dp
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.properties import StringProperty, NumericProperty, ListProperty


class StatCard(BoxLayout):
    """Card de estatística para o dashboard"""
    title = StringProperty("")
    value = StringProperty("")
    color = ListProperty([0.2, 0.8, 0.4])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = dp(20)
        self.spacing = dp(10)
        self.size_hint_y = None
        self.height = dp(150)
        
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(12)]
            )
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        # Título
        title_label = Label(
            text=self.title,
            size_hint_y=None,
            height=dp(20),
            color=(0.4, 0.4, 0.4, 1),
            font_size=dp(12),
            halign='left'
        )
        title_label.bind(texture_size=title_label.setter('size'))
        self.add_widget(title_label)
        
        # Valor
        value_label = Label(
            text=self.value,
            size_hint_y=None,
            height=dp(40),
            color=self.color,
            font_size=dp(24),
            bold=True,
            halign='left'
        )
        value_label.bind(texture_size=value_label.setter('size'))
        self.add_widget(value_label)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class RoundedButton(Button):
    """Botão com bordas arredondadas"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0, 0, 0, 0)
        self.border = [dp(8)]
        
        with self.canvas.before:
            Color(*self.background_color[:3], 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(8)]
            )
        
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class StyledTextInput(TextInput):
    """Input de texto estilizado"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_active = ''
        self.background_color = (0.95, 0.95, 0.95, 1)
        self.padding = [dp(15), dp(12)]
        self.multiline = False
        self.font_size = dp(14)
        self.color = (0.2, 0.2, 0.2, 1)
        
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(8)]
            )
        
        self.bind(pos=self.update_rect, size=self.update_rect, focus=self.on_focus)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def on_focus(self, instance, value):
        if value:
            self.canvas.before.children[0].rgba = (0.2, 0.8, 0.4, 0.3)  # Verde claro quando focado
        else:
            self.canvas.before.children[0].rgba = (0.9, 0.9, 0.9, 1)


class StyledSpinner(Spinner):
    """Spinner estilizado"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ''
        self.background_down = ''
        self.background_color = (0.95, 0.95, 0.95, 1)
        self.font_size = dp(14)
        self.color = (0.2, 0.2, 0.2, 1)
        self.size_hint_y = None
        self.height = dp(45)
        
        with self.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            self.rect = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(8)]
            )
        
        self.bind(pos=self.update_rect, size=self.update_rect)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

