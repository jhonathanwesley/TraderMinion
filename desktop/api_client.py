"""
API Client para comunicação com o backend Django
"""
import requests
import json
from typing import Optional, List, Dict, Any
from pathlib import Path


class APIClient:
    """Cliente para comunicação com a API Django"""
    
    def __init__(self, base_url: str = "http://localhost:8000/api"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
        })
    
    def get_dashboard_stats(self) -> Dict[str, Any]:
        """Obtém estatísticas do dashboard"""
        try:
            response = self.session.get(f"{self.base_url}/dashboard/stats/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao obter estatísticas: {str(e)}")
    
    def get_trades(self) -> List[Dict[str, Any]]:
        """Lista todas as operações"""
        try:
            response = self.session.get(f"{self.base_url}/trades/")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao listar operações: {str(e)}")
    
    def create_trade(self, trade_data: Dict[str, Any], screenshot_path: Optional[str] = None) -> Dict[str, Any]:
        """Cria uma nova operação"""
        try:
            files = {}
            data = {}
            
            # Prepara dados do formulário
            for key, value in trade_data.items():
                if value is not None and value != '':
                    data[key] = str(value)
            
            # Adiciona screenshot se fornecido
            if screenshot_path and Path(screenshot_path).exists():
                files['screenshot'] = open(screenshot_path, 'rb')
            
            # Remove Content-Type para permitir multipart/form-data
            headers = {}
            if not files:
                headers['Content-Type'] = 'application/json'
                response = self.session.post(
                    f"{self.base_url}/trades/",
                    json=data,
                    headers=headers
                )
            else:
                response = self.session.post(
                    f"{self.base_url}/trades/",
                    data=data,
                    files=files,
                    headers=headers
                )
                files['screenshot'].close()
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao criar operação: {str(e)}")
    
    def update_trade(self, trade_id: str, trade_data: Dict[str, Any]) -> Dict[str, Any]:
        """Atualiza uma operação"""
        try:
            response = self.session.patch(
                f"{self.base_url}/trades/{trade_id}/",
                json=trade_data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao atualizar operação: {str(e)}")
    
    def delete_trade(self, trade_id: str) -> None:
        """Deleta uma operação"""
        try:
            response = self.session.delete(f"{self.base_url}/trades/{trade_id}/")
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erro ao deletar operação: {str(e)}")

