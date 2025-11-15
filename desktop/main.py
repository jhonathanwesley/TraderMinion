"""
Aplicação principal TraderMinion Desktop
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.metrics import dp

from desktop.api_client import APIClient
from desktop.sidebar import Sidebar
from desktop.screens.dashboard import DashboardScreen
from desktop.screens.trade_registration import TradeRegistrationScreen


class TraderMinionApp(App):
    """Aplicação principal"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.api_client = APIClient()
        self.current_screen = None
        self.sidebar = None
        self.screen_container = None
    
    def build(self):
        """Constrói a interface"""
        # Configura janela
        Window.size = (1400, 900)
        Window.minimum_width = 1200
        Window.minimum_height = 700
        Window.clearcolor = (0.95, 0.95, 0.95, 1)  # slate-50
        
        # Aplica restrições de tamanho mínimo
        if Window.width < Window.minimum_width:
            Window.width = Window.minimum_width
        if Window.height < Window.minimum_height:
            Window.height = Window.minimum_height
        
        # Layout principal
        main_layout = BoxLayout(orientation='horizontal', spacing=0)
        
        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.on_screen_change = self.change_screen
        main_layout.add_widget(self.sidebar)
        
        # Container de telas
        self.screen_container = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.screen_container)
        
        # Carrega tela inicial
        self.change_screen('dashboard')
        
        return main_layout
    
    def change_screen(self, screen_id):
        """Muda a tela atual"""
        self.screen_container.clear_widgets()
        
        if screen_id == 'dashboard':
            self.current_screen = DashboardScreen(self.api_client)
        elif screen_id == 'register':
            self.current_screen = TradeRegistrationScreen(self.api_client)
        else:
            return
        
        self.screen_container.add_widget(self.current_screen)


if __name__ == '__main__':
    TraderMinionApp().run()

