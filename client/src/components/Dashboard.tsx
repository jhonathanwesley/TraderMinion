import { useEffect, useState } from 'react';
import { TrendingUp, TrendingDown, Activity, DollarSign, Target, BarChart3, AlertCircle } from 'lucide-react';
import { DashboardStats, Trade } from '../types/trade';
import { api } from '../services/api';

export function Dashboard() {
  const [stats, setStats] = useState<DashboardStats | null>(null);
  const [recentTrades, setRecentTrades] = useState<Trade[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadDashboardData();
  }, []);

  const loadDashboardData = async () => {
    try {
      setLoading(true);
      setError(null);
      const [statsData, tradesData] = await Promise.all([
        api.getDashboardStats(),
        api.getTrades(),
      ]);
      setStats(statsData);
      setRecentTrades(tradesData.slice(0, 10));
    } catch (err) {
      setError('Erro ao carregar dados. Verifique a conexão com o backend.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center">
          <Activity className="w-12 h-12 animate-spin text-emerald-500 mx-auto mb-4" />
          <p className="text-slate-600">Carregando dados...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-center max-w-md">
          <AlertCircle className="w-12 h-12 text-amber-500 mx-auto mb-4" />
          <p className="text-slate-700 mb-4">{error}</p>
          <button
            onClick={loadDashboardData}
            className="px-4 py-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600 transition-colors"
          >
            Tentar Novamente
          </button>
        </div>
      </div>
    );
  }

  const formatCurrency = (value: number) => {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL',
    }).format(value);
  };

  const formatPercentage = (value: number) => {
    return `${value > 0 ? '+' : ''}${value.toFixed(2)}%`;
  };

  const statCards = [
    {
      title: 'P&L Total',
      value: formatCurrency(stats?.total_profit_loss || 0),
      icon: DollarSign,
      color: (stats?.total_profit_loss || 0) >= 0 ? 'emerald' : 'red',
      trend: (stats?.total_profit_loss || 0) >= 0 ? 'up' : 'down',
    },
    {
      title: 'Taxa de Acerto',
      value: `${(stats?.win_rate || 0).toFixed(1)}%`,
      icon: Target,
      color: 'blue',
      trend: 'neutral',
    },
    {
      title: 'Total de Operações',
      value: stats?.total_trades || 0,
      icon: BarChart3,
      color: 'slate',
      trend: 'neutral',
    },
    {
      title: 'Operações Abertas',
      value: stats?.open_trades || 0,
      icon: Activity,
      color: 'amber',
      trend: 'neutral',
    },
  ];

  return (
    <div className="p-8">
      <div className="mb-8">
        <h2 className="text-3xl font-bold text-slate-800 mb-2">Dashboard</h2>
        <p className="text-slate-600">Visão geral das suas operações de trading</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {statCards.map((card, index) => {
          const Icon = card.icon;
          const TrendIcon = card.trend === 'up' ? TrendingUp : card.trend === 'down' ? TrendingDown : null;

          return (
            <div
              key={index}
              className="bg-white rounded-xl shadow-sm border border-slate-200 p-6 hover:shadow-md transition-shadow"
            >
              <div className="flex items-start justify-between mb-4">
                <div className={`w-12 h-12 rounded-lg bg-${card.color}-100 flex items-center justify-center`}>
                  <Icon className={`w-6 h-6 text-${card.color}-600`} />
                </div>
                {TrendIcon && (
                  <TrendIcon className={`w-5 h-5 text-${card.color}-500`} />
                )}
              </div>
              <h3 className="text-slate-600 text-sm font-medium mb-1">{card.title}</h3>
              <p className={`text-2xl font-bold text-${card.color}-600`}>{card.value}</p>
            </div>
          );
        })}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8">
        <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Desempenho Detalhado</h3>
          <div className="space-y-4">
            <div className="flex justify-between items-center pb-3 border-b border-slate-100">
              <span className="text-slate-600">Lucro Médio</span>
              <span className="font-semibold text-emerald-600">
                {formatCurrency(stats?.average_profit || 0)}
              </span>
            </div>
            <div className="flex justify-between items-center pb-3 border-b border-slate-100">
              <span className="text-slate-600">Perda Média</span>
              <span className="font-semibold text-red-600">
                {formatCurrency(stats?.average_loss || 0)}
              </span>
            </div>
            <div className="flex justify-between items-center pb-3 border-b border-slate-100">
              <span className="text-slate-600">Melhor Trade</span>
              <span className="font-semibold text-emerald-600">
                {formatCurrency(stats?.best_trade || 0)}
              </span>
            </div>
            <div className="flex justify-between items-center pb-3 border-b border-slate-100">
              <span className="text-slate-600">Pior Trade</span>
              <span className="font-semibold text-red-600">
                {formatCurrency(stats?.worst_trade || 0)}
              </span>
            </div>
            <div className="flex justify-between items-center">
              <span className="text-slate-600">Volume Total</span>
              <span className="font-semibold text-slate-800">
                {formatCurrency(stats?.total_volume || 0)}
              </span>
            </div>
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
          <h3 className="text-lg font-bold text-slate-800 mb-4">Distribuição de Operações</h3>
          <div className="space-y-4">
            <div>
              <div className="flex justify-between mb-2">
                <span className="text-slate-600">Operações Fechadas</span>
                <span className="font-semibold">{stats?.closed_trades || 0}</span>
              </div>
              <div className="w-full bg-slate-100 rounded-full h-2">
                <div
                  className="bg-emerald-500 h-2 rounded-full"
                  style={{
                    width: `${((stats?.closed_trades || 0) / (stats?.total_trades || 1)) * 100}%`,
                  }}
                ></div>
              </div>
            </div>
            <div>
              <div className="flex justify-between mb-2">
                <span className="text-slate-600">Operações Abertas</span>
                <span className="font-semibold">{stats?.open_trades || 0}</span>
              </div>
              <div className="w-full bg-slate-100 rounded-full h-2">
                <div
                  className="bg-amber-500 h-2 rounded-full"
                  style={{
                    width: `${((stats?.open_trades || 0) / (stats?.total_trades || 1)) * 100}%`,
                  }}
                ></div>
              </div>
            </div>
            <div className="pt-4 mt-4 border-t border-slate-100">
              <div className="grid grid-cols-2 gap-4 text-center">
                <div>
                  <p className="text-2xl font-bold text-emerald-600">
                    {Math.round((stats?.win_rate || 0) * (stats?.closed_trades || 0) / 100)}
                  </p>
                  <p className="text-sm text-slate-600">Vitórias</p>
                </div>
                <div>
                  <p className="text-2xl font-bold text-red-600">
                    {(stats?.closed_trades || 0) - Math.round((stats?.win_rate || 0) * (stats?.closed_trades || 0) / 100)}
                  </p>
                  <p className="text-sm text-slate-600">Perdas</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-slate-200 p-6">
        <h3 className="text-lg font-bold text-slate-800 mb-4">Operações Recentes</h3>
        <div className="overflow-x-auto">
          <table className="w-full">
            <thead>
              <tr className="border-b border-slate-200">
                <th className="text-left py-3 px-4 text-sm font-semibold text-slate-600">Ativo</th>
                <th className="text-left py-3 px-4 text-sm font-semibold text-slate-600">Tipo</th>
                <th className="text-left py-3 px-4 text-sm font-semibold text-slate-600">Categoria</th>
                <th className="text-right py-3 px-4 text-sm font-semibold text-slate-600">Quantidade</th>
                <th className="text-right py-3 px-4 text-sm font-semibold text-slate-600">Entrada</th>
                <th className="text-right py-3 px-4 text-sm font-semibold text-slate-600">Saída</th>
                <th className="text-center py-3 px-4 text-sm font-semibold text-slate-600">Status</th>
                <th className="text-right py-3 px-4 text-sm font-semibold text-slate-600">P&L</th>
              </tr>
            </thead>
            <tbody>
              {recentTrades.length === 0 ? (
                <tr>
                  <td colSpan={8} className="text-center py-8 text-slate-500">
                    Nenhuma operação registrada ainda
                  </td>
                </tr>
              ) : (
                recentTrades.map((trade) => (
                  <tr key={trade.id} className="border-b border-slate-100 hover:bg-slate-50">
                    <td className="py-3 px-4 font-medium text-slate-800">{trade.asset}</td>
                    <td className="py-3 px-4">
                      <span
                        className={`inline-flex px-2 py-1 rounded text-xs font-medium ${
                          trade.type === 'BUY'
                            ? 'bg-emerald-100 text-emerald-700'
                            : 'bg-red-100 text-red-700'
                        }`}
                      >
                        {trade.type}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-sm text-slate-600">{trade.category}</td>
                    <td className="py-3 px-4 text-right text-slate-800">{trade.quantity}</td>
                    <td className="py-3 px-4 text-right text-slate-800">
                      {formatCurrency(trade.entry_price)}
                    </td>
                    <td className="py-3 px-4 text-right text-slate-800">
                      {trade.exit_price ? formatCurrency(trade.exit_price) : '-'}
                    </td>
                    <td className="py-3 px-4 text-center">
                      <span
                        className={`inline-flex px-2 py-1 rounded text-xs font-medium ${
                          trade.status === 'OPEN'
                            ? 'bg-amber-100 text-amber-700'
                            : trade.status === 'CLOSED'
                            ? 'bg-slate-100 text-slate-700'
                            : 'bg-blue-100 text-blue-700'
                        }`}
                      >
                        {trade.status}
                      </span>
                    </td>
                    <td className="py-3 px-4 text-right">
                      {trade.profit_loss !== undefined && (
                        <span
                          className={`font-semibold ${
                            trade.profit_loss >= 0 ? 'text-emerald-600' : 'text-red-600'
                          }`}
                        >
                          {formatCurrency(trade.profit_loss)}
                          {trade.profit_loss_percentage !== undefined && (
                            <span className="text-xs ml-1">
                              ({formatPercentage(trade.profit_loss_percentage)})
                            </span>
                          )}
                        </span>
                      )}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
