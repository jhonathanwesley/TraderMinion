#!/usr/bin/env python
"""Quick test of API endpoints"""
import requests
import json

BASE_URL = 'http://localhost:8000/api'

# Test 1: Criar trade
print('=== CRIANDO TRADE ===')
trade_data = {
    'asset': 'BTC/USD',
    'type': 'BUY',
    'category': 'CRYPTO',
    'quantity': '1.5',
    'entry_price': '43000.00',
    'exit_price': '45000.00',
    'status': 'CLOSED',
    'notes': 'Compra de Bitcoin'
}
resp = requests.post(f'{BASE_URL}/trades/', json=trade_data)
print(f'Status: {resp.status_code}')
if resp.status_code == 201:
    print('✓ Trade criado com sucesso!')
    trade = resp.json()
    print(f'ID: {trade["id"]}')
    print(f'Profit/Loss: {trade["profit_loss"]}')
else:
    print(f'Erro: {resp.text}')

# Test 2: Listar trades
print('\n=== LISTANDO TRADES ===')
resp = requests.get(f'{BASE_URL}/trades/')
print(f'Status: {resp.status_code}')
if resp.status_code == 200:
    trades = resp.json()
    print(f'✓ {len(trades)} trade(s) encontrado(s)')
    for t in trades:
        print(f'  - {t["asset"]} ({t["type"]}) - {t["status"]}: P/L = {t["profit_loss"]}')

# Test 3: Stats
print('\n=== DASHBOARD STATS ===')
resp = requests.get(f'{BASE_URL}/trades/stats/')
print(f'Status: {resp.status_code}')
if resp.status_code == 200:
    stats = resp.json()
    print('✓ Estatísticas obtidas:')
    print(f'  Total de trades: {stats["total_trades"]}')
    print(f'  Trades fechados: {stats["closed_trades"]}')
    print(f'  Profit/Loss total: {stats["total_profit_loss"]}')
    print(f'  Win rate: {stats["win_rate"]:.2f}%')
