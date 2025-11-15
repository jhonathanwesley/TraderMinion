"""
Sidebar de navegação
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivy.properties import StringProperty, ObjectProperty


class Sidebar(BoxLayout):
    """Barra lateral de navegação"""
    current_screen = StringProperty('dashboard')
    on_screen_change = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_x = None
        self.width = dp(250)
        
        with self.canvas.before:
            Color(0.1, 0.1, 0.1, 1)  # slate-900
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(80), padding=dp(20), spacing=dp(15))
        
        # Logo/Icon
        logo_box = BoxLayout(orientation='vertical', size_hint_x=None, width=dp(40))
        with logo_box.canvas.before:
            Color(0.2, 0.8, 0.4, 1)  # emerald-500
            logo_box.rect = Rectangle(pos=logo_box.pos, size=logo_box.size)
        def update_logo_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        logo_box.bind(pos=update_logo_rect, size=update_logo_rect)
        logo_label = Label(text='📈', font_size=dp(24))
        logo_box.add_widget(logo_label)
        header.add_widget(logo_box)
        
        # Título
        title_box = BoxLayout(orientation='vertical', size_hint_x=1)
        title = Label(
            text='TradeTracker',
            size_hint_y=None,
            height=dp(25),
            font_size=dp(20),
            bold=True,
            color=(1, 1, 1, 1),
            halign='left'
        )
        title.bind(texture_size=title.setter('size'))
        subtitle = Label(
            text='Trading Operations',
            size_hint_y=None,
            height=dp(20),
            font_size=dp(10),
            color=(0.6, 0.6, 0.6, 1),
            halign='left'
        )
        subtitle.bind(texture_size=subtitle.setter('size'))
        title_box.add_widget(title)
        title_box.add_widget(subtitle)
        header.add_widget(title_box)
        
        self.add_widget(header)
        
        # Separador
        separator = BoxLayout(size_hint_y=None, height=dp(1))
        with separator.canvas.before:
            Color(0.2, 0.2, 0.2, 1)
            separator.rect = Rectangle(pos=separator.pos, size=separator.size)
        def update_separator_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        separator.bind(pos=update_separator_rect, size=update_separator_rect)
        self.add_widget(separator)
        
        # Menu items
        menu_box = BoxLayout(orientation='vertical', padding=dp(15), spacing=dp(10))
        
        self.dashboard_btn = self._create_menu_button('Dashboard', 'dashboard')
        self.register_btn = self._create_menu_button('Nova Operação', 'register')
        
        menu_box.add_widget(self.dashboard_btn)
        menu_box.add_widget(self.register_btn)
        
        self.add_widget(menu_box)
        
        # Spacer
        self.add_widget(BoxLayout())
        
        # Footer
        footer = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(50), padding=dp(15))
        footer_label = Label(
            text='v1.0.0 © 2025',
            size_hint_y=None,
            height=dp(20),
            font_size=dp(10),
            color=(0.4, 0.4, 0.4, 1),
            halign='center'
        )
        footer_label.bind(texture_size=footer_label.setter('size'))
        footer.add_widget(footer_label)
        self.add_widget(footer)
    
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def _create_menu_button(self, text, screen_id):
        """Cria botão do menu"""
        btn = Button(
            text=text,
            size_hint_y=None,
            height=dp(50),
            background_color=(0, 0, 0, 0),
            color=(0.8, 0.8, 0.8, 1),
            font_size=dp(16),
            bold=False
        )
        
        with btn.canvas.before:
            btn.bg_color = Color(0.1, 0.1, 0.1, 1)
            btn.bg_rect = Rectangle(pos=btn.pos, size=btn.size)
        
        def update_btn_rect(instance, value):
            instance.bg_rect.pos = instance.pos
            instance.bg_rect.size = instance.size
        
        btn.bind(
            pos=update_btn_rect,
            size=update_btn_rect,
            on_press=lambda x, sid=screen_id: self.set_screen(sid)
        )
        
        return btn
    
    def set_screen(self, screen_id):
        """Muda a tela atual"""
        self.current_screen = screen_id
        
        # Atualiza aparência dos botões
        for btn in [self.dashboard_btn, self.register_btn]:
            btn.color = (0.8, 0.8, 0.8, 1)
            if hasattr(btn, 'bg_color'):
                btn.bg_color.rgba = (0.1, 0.1, 0.1, 1)
        
        active_btn = self.dashboard_btn if screen_id == 'dashboard' else self.register_btn
        active_btn.color = (1, 1, 1, 1)
        if hasattr(active_btn, 'bg_color'):
            active_btn.bg_color.rgba = (0.2, 0.8, 0.4, 1)  # emerald-500
        
        if self.on_screen_change:
            self.on_screen_change(screen_id)

