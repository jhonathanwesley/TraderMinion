"""
Tela de Dashboard
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

from desktop.api_client import APIClient
from desktop.utils import format_currency, format_percentage, get_color_for_value
from desktop.widgets import StatCard


class DashboardScreen(BoxLayout):
    """Tela principal do dashboard"""
    api_client = ObjectProperty(None)
    
    def __init__(self, api_client: APIClient, **kwargs):
        super().__init__(**kwargs)
        self.api_client = api_client
        self.orientation = 'vertical'
        self.padding = dp(30)
        self.spacing = dp(20)
        
        # Container principal com scroll
        scroll = ScrollView(do_scroll_x=False)
        content = BoxLayout(orientation='vertical', spacing=dp(20), size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Título
        title_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        title = Label(
            text='Dashboard',
            size_hint_y=None,
            height=dp(40),
            font_size=dp(32),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='left'
        )
        title.bind(texture_size=title.setter('size'))
        subtitle = Label(
            text='Visão geral das suas operações de trading',
            size_hint_y=None,
            height=dp(30),
            font_size=dp(14),
            color=(0.5, 0.5, 0.5, 1),
            halign='left'
        )
        subtitle.bind(texture_size=subtitle.setter('size'))
        title_box.add_widget(title)
        title_box.add_widget(subtitle)
        content.add_widget(title_box)
        
        # Cards de estatísticas
        self.stats_grid = GridLayout(cols=4, spacing=dp(15), size_hint_y=None)
        self.stats_grid.bind(minimum_height=self.stats_grid.setter('height'))
        content.add_widget(self.stats_grid)
        
        # Seção de desempenho detalhado
        performance_box = BoxLayout(orientation='horizontal', spacing=dp(15), size_hint_y=None, height=dp(300))
        
        # Card de desempenho
        perf_card = self._create_performance_card()
        performance_box.add_widget(perf_card)
        
        # Card de distribuição
        dist_card = self._create_distribution_card()
        performance_box.add_widget(dist_card)
        
        content.add_widget(performance_box)
        
        # Tabela de operações recentes
        trades_card = self._create_trades_table()
        content.add_widget(trades_card)
        
        scroll.add_widget(content)
        self.add_widget(scroll)
        
        # Botão de atualizar
        refresh_btn = Button(
            text='Atualizar',
            size_hint_y=None,
            height=dp(50),
            background_color=(0.2, 0.8, 0.4, 1),
            color=(1, 1, 1, 1),
            font_size=dp(16),
            bold=True
        )
        refresh_btn.bind(on_press=self.load_data)
        self.add_widget(refresh_btn)
        
        # Carrega dados inicialmente
        Clock.schedule_once(lambda dt: self.load_data(), 0.5)
    
    def _create_performance_card(self):
        """Cria card de desempenho detalhado"""
        card = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        card.size_hint_x = 0.5
        card.size_hint_y = None
        card.height = dp(300)
        
        with card.canvas.before:
            Color(1, 1, 1, 1)
            card.rect = RoundedRectangle(pos=card.pos, size=card.size, radius=[dp(12)])
        
        def update_perf_card_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        card.bind(pos=update_perf_card_rect, size=update_perf_card_rect)
        
        title = Label(
            text='Desempenho Detalhado',
            size_hint_y=None,
            height=dp(30),
            font_size=dp(18),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='left'
        )
        title.bind(texture_size=title.setter('size'))
        card.add_widget(title)
        
        self.perf_details = BoxLayout(orientation='vertical', spacing=dp(10))
        card.add_widget(self.perf_details)
        
        return card
    
    def _create_distribution_card(self):
        """Cria card de distribuição"""
        card = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        card.size_hint_x = 0.5
        card.size_hint_y = None
        card.height = dp(300)
        
        with card.canvas.before:
            Color(1, 1, 1, 1)
            card.rect = RoundedRectangle(pos=card.pos, size=card.size, radius=[dp(12)])
        
        def update_dist_card_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        card.bind(pos=update_dist_card_rect, size=update_dist_card_rect)
        
        title = Label(
            text='Distribuição de Operações',
            size_hint_y=None,
            height=dp(30),
            font_size=dp(18),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='left'
        )
        title.bind(texture_size=title.setter('size'))
        card.add_widget(title)
        
        self.dist_details = BoxLayout(orientation='vertical', spacing=dp(10))
        card.add_widget(self.dist_details)
        
        return card
    
    def _create_trades_table(self):
        """Cria tabela de operações recentes"""
        card = BoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        card.size_hint_y = None
        card.height = dp(400)
        
        with card.canvas.before:
            Color(1, 1, 1, 1)
            card.rect = RoundedRectangle(pos=card.pos, size=card.size, radius=[dp(12)])
        
        def update_trades_card_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        card.bind(pos=update_trades_card_rect, size=update_trades_card_rect)
        
        title = Label(
            text='Operações Recentes',
            size_hint_y=None,
            height=dp(30),
            font_size=dp(18),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='left'
        )
        title.bind(texture_size=title.setter('size'))
        card.add_widget(title)
        
        scroll = ScrollView(do_scroll_x=True, do_scroll_y=True)
        self.trades_table = GridLayout(cols=8, spacing=dp(10), size_hint_x=None, size_hint_y=None)
        self.trades_table.bind(minimum_width=self.trades_table.setter('width'),
                               minimum_height=self.trades_table.setter('height'))
        self.trades_table.width = dp(1200)
        
        # Cabeçalho
        headers = ['Ativo', 'Tipo', 'Categoria', 'Quantidade', 'Entrada', 'Saída', 'Status', 'P&L']
        for header in headers:
            lbl = Label(
                text=header,
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                bold=True,
                color=(0.4, 0.4, 0.4, 1)
            )
            self.trades_table.add_widget(lbl)
        
        scroll.add_widget(self.trades_table)
        card.add_widget(scroll)
        
        return card
    
    def load_data(self, *args):
        """Carrega dados do dashboard"""
        try:
            stats = self.api_client.get_dashboard_stats()
            trades = self.api_client.get_trades()
            self.update_dashboard(stats, trades[:10])  # Mostra apenas 10 mais recentes
        except Exception as e:
            self.show_error(str(e))
    
    def update_dashboard(self, stats, trades):
        """Atualiza a interface com os dados"""
        # Limpa cards antigos
        self.stats_grid.clear_widgets()
        self.perf_details.clear_widgets()
        self.dist_details.clear_widgets()
        
        # Remove linhas antigas da tabela (exceto cabeçalho)
        children_to_remove = self.trades_table.children[:]
        for child in children_to_remove[8:]:  # Mantém os 8 cabeçalhos
            self.trades_table.remove_widget(child)
        
        # Cards de estatísticas principais
        pnl_color = get_color_for_value(stats.get('total_profit_loss', 0))
        cards_data = [
            ('P&L Total', format_currency(stats.get('total_profit_loss', 0)), pnl_color),
            ('Taxa de Acerto', f"{stats.get('win_rate', 0):.1f}%", (0.3, 0.6, 0.9, 1)),
            ('Total de Operações', str(stats.get('total_trades', 0)), (0.5, 0.5, 0.5, 1)),
            ('Operações Abertas', str(stats.get('open_trades', 0)), (1.0, 0.7, 0.0, 1)),
        ]
        
        for title, value, color in cards_data:
            card = StatCard(title=title, value=value, color=color)
            self.stats_grid.add_widget(card)
        
        # Desempenho detalhado
        perf_items = [
            ('Lucro Médio', format_currency(stats.get('average_profit', 0)), (0.2, 0.8, 0.4, 1)),
            ('Perda Média', format_currency(stats.get('average_loss', 0)), (0.9, 0.3, 0.3, 1)),
            ('Melhor Trade', format_currency(stats.get('best_trade', 0)), (0.2, 0.8, 0.4, 1)),
            ('Pior Trade', format_currency(stats.get('worst_trade', 0)), (0.9, 0.3, 0.3, 1)),
            ('Volume Total', format_currency(stats.get('total_volume', 0)), (0.2, 0.2, 0.2, 1)),
        ]
        
        for label, value, color in perf_items:
            box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(30))
            lbl = Label(text=label, size_hint_x=0.6, color=(0.5, 0.5, 0.5, 1), font_size=dp(14))
            val = Label(text=value, size_hint_x=0.4, color=color, font_size=dp(14), bold=True, halign='right')
            val.bind(texture_size=val.setter('size'))
            box.add_widget(lbl)
            box.add_widget(val)
            self.perf_details.add_widget(box)
        
        # Distribuição
        total = stats.get('total_trades', 1)
        closed = stats.get('closed_trades', 0)
        open_trades = stats.get('open_trades', 0)
        wins = int((stats.get('win_rate', 0) / 100) * closed) if closed > 0 else 0
        losses = closed - wins
        
        dist_items = [
            ('Operações Fechadas', closed, total, (0.2, 0.8, 0.4, 1)),
            ('Operações Abertas', open_trades, total, (1.0, 0.7, 0.0, 1)),
        ]
        
        for label, value, max_val, color in dist_items:
            box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(50), spacing=dp(5))
            header = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(20))
            lbl = Label(text=label, size_hint_x=0.7, color=(0.5, 0.5, 0.5, 1), font_size=dp(14))
            val = Label(text=str(value), size_hint_x=0.3, color=(0.2, 0.2, 0.2, 1), font_size=dp(14), bold=True, halign='right')
            header.add_widget(lbl)
            header.add_widget(val)
            box.add_widget(header)
            
            # Barra de progresso
            progress_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(8))
            with progress_box.canvas.before:
                Color(0.9, 0.9, 0.9, 1)
                progress_box.bg_rect = RoundedRectangle(pos=progress_box.pos, size=progress_box.size, radius=[dp(4)])
            def update_progress_rect(instance, value):
                instance.bg_rect.pos = instance.pos
                instance.bg_rect.size = instance.size
            progress_box.bind(pos=update_progress_rect, size=update_progress_rect)
            
            if max_val > 0:
                progress_width = (value / max_val) * progress_box.width if progress_box.width > 0 else 0
                with progress_box.canvas:
                    Color(*color[:3])
                    progress_box.prog_rect = RoundedRectangle(
                        pos=progress_box.pos,
                        size=(progress_width, progress_box.height),
                        radius=[dp(4)]
                    )
            
            box.add_widget(progress_box)
            self.dist_details.add_widget(box)
        
        # Vitórias e perdas
        wins_losses = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(20))
        wins_box = BoxLayout(orientation='vertical', size_hint_x=0.5)
        wins_val = Label(text=str(wins), font_size=dp(24), bold=True, color=(0.2, 0.8, 0.4, 1))
        wins_lbl = Label(text='Vitórias', font_size=dp(12), color=(0.5, 0.5, 0.5, 1))
        wins_box.add_widget(wins_val)
        wins_box.add_widget(wins_lbl)
        
        losses_box = BoxLayout(orientation='vertical', size_hint_x=0.5)
        losses_val = Label(text=str(losses), font_size=dp(24), bold=True, color=(0.9, 0.3, 0.3, 1))
        losses_lbl = Label(text='Perdas', font_size=dp(12), color=(0.5, 0.5, 0.5, 1))
        losses_box.add_widget(losses_val)
        losses_box.add_widget(losses_lbl)
        
        wins_losses.add_widget(wins_box)
        wins_losses.add_widget(losses_box)
        self.dist_details.add_widget(wins_losses)
        
        # Tabela de trades
        from desktop.utils import get_status_color, get_type_color
        for trade in trades:
            # Ativo
            self.trades_table.add_widget(Label(
                text=trade.get('asset', ''),
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=(0.2, 0.2, 0.2, 1)
            ))
            # Tipo
            type_color = get_type_color(trade.get('type', 'BUY'))
            type_lbl = Label(
                text=trade.get('type', ''),
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=type_color
            )
            self.trades_table.add_widget(type_lbl)
            # Categoria
            self.trades_table.add_widget(Label(
                text=trade.get('category', ''),
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=(0.5, 0.5, 0.5, 1)
            ))
            # Quantidade
            self.trades_table.add_widget(Label(
                text=str(trade.get('quantity', '')),
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=(0.2, 0.2, 0.2, 1),
                halign='right'
            ))
            # Entrada
            self.trades_table.add_widget(Label(
                text=format_currency(trade.get('entry_price', 0)),
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=(0.2, 0.2, 0.2, 1),
                halign='right'
            ))
            # Saída
            exit_price = trade.get('exit_price')
            self.trades_table.add_widget(Label(
                text=format_currency(exit_price) if exit_price else '-',
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=(0.2, 0.2, 0.2, 1),
                halign='right'
            ))
            # Status
            status_color = get_status_color(trade.get('status', 'PENDING'))
            status_lbl = Label(
                text=trade.get('status', ''),
                size_hint_x=None,
                width=dp(150),
                font_size=dp(12),
                color=status_color,
                halign='center'
            )
            self.trades_table.add_widget(status_lbl)
            # P&L
            pl = trade.get('profit_loss')
            if pl is not None:
                pl_color = get_color_for_value(pl)
                pl_text = format_currency(pl)
                pl_perc = trade.get('profit_loss_percentage')
                if pl_perc is not None:
                    pl_text += f" ({format_percentage(pl_perc)})"
                pl_lbl = Label(
                    text=pl_text,
                    size_hint_x=None,
                    width=dp(150),
                    font_size=dp(12),
                    color=pl_color,
                    bold=True,
                    halign='right'
                )
            else:
                pl_lbl = Label(
                    text='-',
                    size_hint_x=None,
                    width=dp(150),
                    font_size=dp(12),
                    color=(0.5, 0.5, 0.5, 1),
                    halign='right'
                )
            self.trades_table.add_widget(pl_lbl)
        
        # Ajusta altura da tabela
        self.trades_table.height = dp(40) + (len(trades) * dp(35))
    
    def show_error(self, message):
        """Mostra popup de erro"""
        popup = Popup(
            title='Erro',
            content=Label(text=message, text_size=(dp(400), None)),
            size_hint=(0.6, 0.4)
        )
        popup.open()

