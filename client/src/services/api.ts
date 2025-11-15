import { Trade, DashboardStats } from '../types/trade';

const API_BASE_URL = import.meta.env.VITE_DJANGO_API_URL || 'http://localhost:8000/api';

export const api = {
  async getDashboardStats(): Promise<DashboardStats> {
    const response = await fetch(`${API_BASE_URL}/dashboard/stats/`);
    if (!response.ok) throw new Error('Failed to fetch dashboard stats');
    return response.json();
  },

  async getTrades(): Promise<Trade[]> {
    const response = await fetch(`${API_BASE_URL}/trades/`);
    if (!response.ok) throw new Error('Failed to fetch trades');
    return response.json();
  },

  async createTrade(trade: FormData): Promise<Trade> {
    const response = await fetch(`${API_BASE_URL}/trades/`, {
      method: 'POST',
      body: trade,
    });
    if (!response.ok) throw new Error('Failed to create trade');
    return response.json();
  },

  async updateTrade(id: string, trade: Partial<Trade>): Promise<Trade> {
    const response = await fetch(`${API_BASE_URL}/trades/${id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(trade),
    });
    if (!response.ok) throw new Error('Failed to update trade');
    return response.json();
  },

  async deleteTrade(id: string): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/trades/${id}/`, {
      method: 'DELETE',
    });
    if (!response.ok) throw new Error('Failed to delete trade');
  },
};
