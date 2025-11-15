from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count, Q, Avg, Max, Min, F
from django.utils import timezone
from .models import Trade
from .serializers import TradeSerializer


class TradeViewSet(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer

    @action(detail=False, methods=['get'])
    def stats(self, request):
        """Get dashboard statistics"""
        trades = Trade.objects.all()
        closed_trades = trades.filter(status='CLOSED')
        open_trades = trades.filter(status='OPEN')

        closed_trades_list = list(closed_trades)
        winning_trades = [
            t for t in closed_trades_list
            if t.profit_loss and t.profit_loss > 0
        ]
        losing_trades = [
            t for t in closed_trades_list
            if t.profit_loss and t.profit_loss < 0
        ]

        total_profit_loss = sum(
            float(trade.profit_loss or 0) for trade in closed_trades_list
        )

        stats = {
            'total_trades': trades.count(),
            'open_trades': open_trades.count(),
            'closed_trades': closed_trades.count(),
            'total_profit_loss': total_profit_loss,
            'win_rate': (
                len(winning_trades) / len(closed_trades_list) * 100
                if closed_trades_list
                else 0
            ),
            'average_profit': (
                sum(t.profit_loss for t in winning_trades) / len(winning_trades)
                if winning_trades
                else 0
            ),
            'average_loss': (
                sum(t.profit_loss for t in losing_trades) / len(losing_trades)
                if losing_trades
                else 0
            ),
            'best_trade': (
                max(t.profit_loss for t in closed_trades_list)
                if closed_trades_list
                else 0
            ),
            'worst_trade': (
                min(t.profit_loss for t in closed_trades_list)
                if closed_trades_list
                else 0
            ),
            'total_volume': sum(
                float(t.quantity * t.entry_price) for t in trades
            ),
        }

        return Response(stats)
