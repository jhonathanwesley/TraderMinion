"""
Tela de Registro de Operações
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
from kivy.uix.image import Image as KivyImage

from desktop.api_client import APIClient
from desktop.widgets import StyledTextInput, StyledSpinner
from desktop.utils import format_currency
import os


class FileChooserPopup(Popup):
    """Popup para escolher arquivo de screenshot"""
    file_path = StringProperty("")
    
    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.title = "Selecionar Screenshot"
        self.size_hint = (0.8, 0.8)
        self.callback = callback
        
        content = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(10))
        
        filechooser = FileChooserIconView(
            filters=['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']
        )
        content.add_widget(filechooser)
        
        btn_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(50), spacing=dp(10))
        select_btn = Button(text='Selecionar', size_hint_x=0.5, background_color=(0.2, 0.8, 0.4, 1))
        select_btn.bind(on_press=lambda x: self.select_file(filechooser))
        cancel_btn = Button(text='Cancelar', size_hint_x=0.5, background_color=(0.7, 0.7, 0.7, 1))
        cancel_btn.bind(on_press=self.dismiss)
        btn_box.add_widget(select_btn)
        btn_box.add_widget(cancel_btn)
        content.add_widget(btn_box)
        
        self.content = content
    
    def select_file(self, filechooser):
        if filechooser.selection:
            self.file_path = filechooser.selection[0]
            self.callback(self.file_path)
            self.dismiss()


class TradeRegistrationScreen(BoxLayout):
    """Tela de registro de operações"""
    api_client = ObjectProperty(None)
    screenshot_path = StringProperty("")
    
    def __init__(self, api_client: APIClient, **kwargs):
        super().__init__(**kwargs)
        self.api_client = api_client
        self.orientation = 'vertical'
        self.padding = dp(30)
        self.spacing = dp(20)
        
        # Container com scroll
        scroll = ScrollView(do_scroll_x=False)
        content = BoxLayout(orientation='vertical', spacing=dp(20), size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        # Título
        title_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(80))
        title = Label(
            text='Nova Operação',
            size_hint_y=None,
            height=dp(40),
            font_size=dp(32),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='left'
        )
        title.bind(texture_size=title.setter('size'))
        subtitle = Label(
            text='Registre uma nova operação de trading',
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
        
        # Formulário
        form_card = BoxLayout(orientation='vertical', padding=dp(30), spacing=dp(20))
        form_card.size_hint_y = None
        form_card.height = dp(1000)
        
        with form_card.canvas.before:
            Color(1, 1, 1, 1)
            form_card.rect = RoundedRectangle(pos=form_card.pos, size=form_card.size, radius=[dp(12)])
        
        def update_form_card_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size
        form_card.bind(pos=update_form_card_rect, size=update_form_card_rect)
        
        # Grid de campos
        grid = GridLayout(cols=2, spacing=dp(20), size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        # Ativo
        grid.add_widget(self._create_label('Ativo *'))
        self.asset_input = StyledTextInput(hint_text='Ex: BTCUSDT, AAPL, EURUSD')
        grid.add_widget(self.asset_input)
        
        # Tipo
        grid.add_widget(self._create_label('Tipo *'))
        self.type_spinner = StyledSpinner(
            text='BUY',
            values=('BUY', 'SELL')
        )
        grid.add_widget(self.type_spinner)
        
        # Categoria
        grid.add_widget(self._create_label('Categoria *'))
        self.category_spinner = StyledSpinner(
            text='CRYPTO',
            values=('CRYPTO', 'STOCKS', 'FOREX', 'DERIVATIVES')
        )
        grid.add_widget(self.category_spinner)
        
        # Status
        grid.add_widget(self._create_label('Status *'))
        self.status_spinner = StyledSpinner(
            text='OPEN',
            values=('OPEN', 'CLOSED', 'PENDING')
        )
        grid.add_widget(self.status_spinner)
        
        # Quantidade
        grid.add_widget(self._create_label('Quantidade *'))
        self.quantity_input = StyledTextInput(hint_text='0.00', input_filter='float')
        grid.add_widget(self.quantity_input)
        
        # Preço de Entrada
        grid.add_widget(self._create_label('Preço de Entrada *'))
        self.entry_price_input = StyledTextInput(hint_text='0.00', input_filter='float')
        grid.add_widget(self.entry_price_input)
        
        # Preço de Saída
        grid.add_widget(self._create_label('Preço de Saída'))
        self.exit_price_input = StyledTextInput(hint_text='0.00', input_filter='float')
        grid.add_widget(self.exit_price_input)
        
        # Stop Loss
        grid.add_widget(self._create_label('Stop Loss'))
        self.stop_loss_input = StyledTextInput(hint_text='0.00', input_filter='float')
        grid.add_widget(self.stop_loss_input)
        
        # Take Profit
        grid.add_widget(self._create_label('Take Profit'))
        self.take_profit_input = StyledTextInput(hint_text='0.00', input_filter='float')
        grid.add_widget(self.take_profit_input)
        
        form_card.add_widget(grid)
        
        # Observações
        notes_label = self._create_label('Observações')
        form_card.add_widget(notes_label)
        self.notes_input = StyledTextInput(multiline=True, size_hint_y=None, height=dp(100))
        form_card.add_widget(self.notes_input)
        
        # Screenshot
        screenshot_label = self._create_label('Screenshot da Operação')
        form_card.add_widget(screenshot_label)
        
        self.screenshot_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(200), spacing=dp(10))
        self.screenshot_preview = None
        self._update_screenshot_display()
        form_card.add_widget(self.screenshot_box)
        
        content.add_widget(form_card)
        scroll.add_widget(content)
        self.add_widget(scroll)
        
        # Botões
        btn_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(60), spacing=dp(15))
        
        submit_btn = Button(
            text='Registrar Operação',
            size_hint_x=0.7,
            background_color=(0.2, 0.8, 0.4, 1),
            color=(1, 1, 1, 1),
            font_size=dp(16),
            bold=True
        )
        submit_btn.bind(on_press=self.submit_form)
        
        clear_btn = Button(
            text='Limpar',
            size_hint_x=0.3,
            background_color=(0.9, 0.9, 0.9, 1),
            color=(0.2, 0.2, 0.2, 1),
            font_size=dp(16)
        )
        clear_btn.bind(on_press=self.clear_form)
        
        btn_box.add_widget(submit_btn)
        btn_box.add_widget(clear_btn)
        self.add_widget(btn_box)
        
        # Labels de feedback
        self.success_label = None
        self.error_label = None
    
    def _create_label(self, text):
        """Cria label estilizado"""
        label = Label(
            text=text,
            size_hint_y=None,
            height=dp(25),
            font_size=dp(14),
            bold=True,
            color=(0.2, 0.2, 0.2, 1),
            halign='left'
        )
        label.bind(texture_size=label.setter('size'))
        return label
    
    def _update_screenshot_display(self):
        """Atualiza display do screenshot"""
        self.screenshot_box.clear_widgets()
        
        if self.screenshot_path and os.path.exists(self.screenshot_path):
            # Mostra preview
            preview_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(180))
            
            img = KivyImage(
                source=self.screenshot_path,
                size_hint_y=None,
                height=dp(150),
                allow_stretch=True,
                keep_ratio=True
            )
            preview_box.add_widget(img)
            
            btn_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(30), spacing=dp(10))
            remove_btn = Button(
                text='Remover',
                size_hint_x=0.5,
                background_color=(0.9, 0.3, 0.3, 1),
                color=(1, 1, 1, 1),
                font_size=dp(12)
            )
            remove_btn.bind(on_press=lambda x: self.remove_screenshot())
            btn_box.add_widget(remove_btn)
            preview_box.add_widget(btn_box)
            
            self.screenshot_box.add_widget(preview_box)
        else:
            # Mostra área de upload
            upload_box = BoxLayout(orientation='vertical', spacing=dp(10), padding=dp(20))
            upload_box.size_hint_y = None
            upload_box.height = dp(180)
            
            with upload_box.canvas.before:
                Color(0.95, 0.95, 0.95, 1)
                upload_box.rect = RoundedRectangle(pos=upload_box.pos, size=upload_box.size, radius=[dp(8)])
            
            def update_upload_rect(instance, value):
                instance.rect.pos = instance.pos
                instance.rect.size = instance.size
            upload_box.bind(pos=update_upload_rect, size=update_upload_rect)
            
            info_label = Label(
                text='Clique para selecionar uma imagem\nou arraste uma imagem aqui',
                text_size=(None, None),
                halign='center',
                valign='middle',
                color=(0.5, 0.5, 0.5, 1),
                font_size=dp(14)
            )
            upload_box.add_widget(info_label)
            
            select_btn = Button(
                text='Selecionar Arquivo',
                size_hint_y=None,
                height=dp(40),
                background_color=(0.9, 0.9, 0.9, 1),
                color=(0.2, 0.2, 0.2, 1),
                font_size=dp(14)
            )
            select_btn.bind(on_press=self.select_screenshot)
            upload_box.add_widget(select_btn)
            
            self.screenshot_box.add_widget(upload_box)
    
    def select_screenshot(self, *args):
        """Abre seletor de arquivo"""
        popup = FileChooserPopup(callback=self.on_screenshot_selected)
        popup.open()
    
    def on_screenshot_selected(self, file_path):
        """Callback quando screenshot é selecionado"""
        self.screenshot_path = file_path
        self._update_screenshot_display()
    
    def remove_screenshot(self):
        """Remove screenshot selecionado"""
        self.screenshot_path = ""
        self._update_screenshot_display()
    
    def clear_form(self, *args):
        """Limpa formulário"""
        self.asset_input.text = ""
        self.type_spinner.text = 'BUY'
        self.category_spinner.text = 'CRYPTO'
        self.status_spinner.text = 'OPEN'
        self.quantity_input.text = ""
        self.entry_price_input.text = ""
        self.exit_price_input.text = ""
        self.stop_loss_input.text = ""
        self.take_profit_input.text = ""
        self.notes_input.text = ""
        self.remove_screenshot()
        self.hide_feedback()
    
    def show_success(self, message):
        """Mostra mensagem de sucesso"""
        self.hide_feedback()
        self.success_label = Label(
            text=message,
            size_hint_y=None,
            height=dp(50),
            color=(0.1, 0.6, 0.2, 1),
            font_size=dp(14),
            bold=True
        )
        self.add_widget(self.success_label, index=1)
        Clock.schedule_once(lambda dt: self.hide_feedback(), 3)
    
    def show_error(self, message):
        """Mostra mensagem de erro"""
        self.hide_feedback()
        self.error_label = Label(
            text=message,
            size_hint_y=None,
            height=dp(50),
            color=(0.9, 0.3, 0.3, 1),
            font_size=dp(14),
            bold=True
        )
        self.add_widget(self.error_label, index=1)
    
    def hide_feedback(self):
        """Esconde mensagens de feedback"""
        if self.success_label and self.success_label.parent:
            self.remove_widget(self.success_label)
            self.success_label = None
        if self.error_label and self.error_label.parent:
            self.remove_widget(self.error_label)
            self.error_label = None
    
    def submit_form(self, *args):
        """Submete formulário"""
        # Validação
        if not self.asset_input.text.strip():
            self.show_error("Ativo é obrigatório")
            return
        if not self.quantity_input.text.strip():
            self.show_error("Quantidade é obrigatória")
            return
        if not self.entry_price_input.text.strip():
            self.show_error("Preço de entrada é obrigatório")
            return
        
        # Prepara dados
        trade_data = {
            'asset': self.asset_input.text.strip(),
            'type': self.type_spinner.text,
            'category': self.category_spinner.text,
            'status': self.status_spinner.text,
            'quantity': self.quantity_input.text.strip(),
            'entry_price': self.entry_price_input.text.strip(),
        }
        
        if self.exit_price_input.text.strip():
            trade_data['exit_price'] = self.exit_price_input.text.strip()
        if self.stop_loss_input.text.strip():
            trade_data['stop_loss'] = self.stop_loss_input.text.strip()
        if self.take_profit_input.text.strip():
            trade_data['take_profit'] = self.take_profit_input.text.strip()
        if self.notes_input.text.strip():
            trade_data['notes'] = self.notes_input.text.strip()
        
        # Envia para API
        try:
            self.api_client.create_trade(trade_data, self.screenshot_path if self.screenshot_path else None)
            self.show_success("Operação registrada com sucesso!")
            self.clear_form()
        except Exception as e:
            self.show_error(f"Erro ao registrar operação: {str(e)}")

