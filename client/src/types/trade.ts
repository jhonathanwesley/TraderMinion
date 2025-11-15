export interface Trade {
  id: string;
  asset: string;
  type: 'BUY' | 'SELL';
  category: 'CRYPTO' | 'STOCKS' | 'FOREX' | 'DERIVATIVES';
  quantity: number;
  entry_price: number;
  exit_price?: number;
  stop_loss?: number;
  take_profit?: number;
  status: 'OPEN' | 'CLOSED' | 'PENDING';
  opened_at: string;
  closed_at?: string;
  notes?: string;
  screenshot?: string;
  profit_loss?: number;
  profit_loss_percentage?: number;
}

export interface DashboardStats {
  total_trades: number;
  open_trades: number;
  closed_trades: number;
  total_profit_loss: number;
  win_rate: number;
  average_profit: number;
  average_loss: number;
  best_trade: number;
  worst_trade: number;
  total_volume: number;
}
