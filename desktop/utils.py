"""
Utilitários para formatação e helpers
"""
from typing import Optional


def format_currency(value: float) -> str:
    """Formata valor como moeda brasileira"""
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def format_percentage(value: float) -> str:
    """Formata valor como porcentagem"""
    sign = "+" if value >= 0 else ""
    return f"{sign}{value:.2f}%"


def get_color_for_value(value: float) -> tuple:
    """Retorna cor RGB baseada no valor (verde para positivo, vermelho para negativo)"""
    if value >= 0:
        return (0.2, 0.8, 0.4)  # Verde (emerald)
    else:
        return (0.9, 0.3, 0.3)  # Vermelho


def get_status_color(status: str) -> tuple:
    """Retorna cor baseada no status"""
    colors = {
        'OPEN': (1.0, 0.7, 0.0),      # Amarelo/Amber
        'CLOSED': (0.5, 0.5, 0.5),    # Cinza/Slate
        'PENDING': (0.3, 0.6, 0.9),   # Azul
    }
    return colors.get(status, (0.5, 0.5, 0.5))


def get_type_color(trade_type: str) -> tuple:
    """Retorna cor baseada no tipo de trade"""
    if trade_type == 'BUY':
        return (0.2, 0.8, 0.4)  # Verde
    else:
        return (0.9, 0.3, 0.3)  # Vermelho

