#!/usr/bin/env python
"""
Script de teste para validar a API Django
"""
import requests
import json
from datetime import datetime
import time

API_URL = "http://localhost:8000/api"

def test_api():
    print("=" * 60)
    print("Testando API Django - TraderMinion")
    print("=" * 60)
    
    # Test 1: GET trades (deve estar vazio no início)
    print("\n[TEST 1] GET /api/trades/")
    try:
        response = requests.get(f"{API_URL}/trades/")
        print(f"Status: {response.status_code}")
        trades = response.json()
        print(f"Trades: {json.dumps(trades, indent=2)}")
    except Exception as e:
        print(f"Erro: {e}")
    
    # Test 2: POST create trade
    print("\n[TEST 2] POST /api/trades/")
    trade_data = {
        "asset": "BTC/USD",
        "type": "BUY",
        "category": "CRYPTO",
        "quantity": "0.5",
        "entry_price": "45000.00",
        "exit_price": "46000.00",
        "stop_loss": "44000.00",
        "take_profit": "47000.00",
        "status": "CLOSED",
        "notes": "Trade de teste - Compra de Bitcoin"
    }
    try:
        response = requests.post(f"{API_URL}/trades/", json=trade_data)
        print(f"Status: {response.status_code}")
        trade = response.json()
        print(f"Resposta: {json.dumps(trade, indent=2)}")
        trade_id = trade.get('id')
    except Exception as e:
        print(f"Erro: {e}")
        trade_id = None
    
    # Test 3: GET dashboard stats
    print("\n[TEST 3] GET /api/dashboard/stats/ (antes do segundo trade)")
    try:
        response = requests.get(f"{API_URL}/trades/stats/")
        print(f"Status: {response.status_code}")
        stats = response.json()
        print(f"Stats: {json.dumps(stats, indent=2)}")
    except Exception as e:
        print(f"Erro: {e}")
    
    # Test 4: Create another trade with loss
    print("\n[TEST 4] POST /api/trades/ (trade com loss)")
    trade_data2 = {
        "asset": "ETH/USD",
        "type": "BUY",
        "category": "CRYPTO",
        "quantity": "1.0",
        "entry_price": "2500.00",
        "exit_price": "2400.00",
        "status": "CLOSED",
        "notes": "Trade de teste - Compra de Ethereum com loss"
    }
    try:
        response = requests.post(f"{API_URL}/trades/", json=trade_data2)
        print(f"Status: {response.status_code}")
        trade2 = response.json()
        print(f"Resposta: {json.dumps(trade2, indent=2)}")
    except Exception as e:
        print(f"Erro: {e}")
    
    # Test 5: GET dashboard stats (após criar trades)
    print("\n[TEST 5] GET /api/dashboard/stats/ (após criar trades)")
    try:
        response = requests.get(f"{API_URL}/trades/stats/")
        print(f"Status: {response.status_code}")
        stats = response.json()
        print(f"Stats: {json.dumps(stats, indent=2)}")
    except Exception as e:
        print(f"Erro: {e}")
    
    # Test 6: GET all trades
    print("\n[TEST 6] GET /api/trades/ (listar todos)")
    try:
        response = requests.get(f"{API_URL}/trades/")
        print(f"Status: {response.status_code}")
        trades = response.json()
        print(f"Total de trades: {len(trades)}")
        for trade in trades:
            print(f"  - {trade['asset']} ({trade['type']}) - Status: {trade['status']}")
    except Exception as e:
        print(f"Erro: {e}")
    
    # Test 7: PATCH/Update trade
    if trade_id:
        print(f"\n[TEST 7] PATCH /api/trades/{trade_id}/")
        update_data = {
            "notes": "Trade atualizado com novo comentário"
        }
        try:
            response = requests.patch(f"{API_URL}/trades/{trade_id}/", json=update_data)
            print(f"Status: {response.status_code}")
            updated_trade = response.json()
            print(f"Trade atualizado: {json.dumps(updated_trade, indent=2)}")
        except Exception as e:
            print(f"Erro: {e}")
    
    # Test 8: DELETE trade
    if trade_id:
        print(f"\n[TEST 8] DELETE /api/trades/{trade_id}/")
        try:
            response = requests.delete(f"{API_URL}/trades/{trade_id}/")
            print(f"Status: {response.status_code}")
            print("Trade deletado com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")
    
    print("\n" + "=" * 60)
    print("Testes concluídos!")
    print("=" * 60)

if __name__ == "__main__":
    try:
        test_api()
    except KeyboardInterrupt:
        print("\nTeste interrompido!")
