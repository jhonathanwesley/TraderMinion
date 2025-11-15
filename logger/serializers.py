from rest_framework import serializers
from .models import Trade


class TradeSerializer(serializers.ModelSerializer):
    profit_loss = serializers.SerializerMethodField()
    profit_loss_percentage = serializers.SerializerMethodField()
    screenshot = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Trade
        fields = [
            'id',
            'asset',
            'type',
            'category',
            'quantity',
            'entry_price',
            'exit_price',
            'stop_loss',
            'take_profit',
            'status',
            'opened_at',
            'closed_at',
            'notes',
            'screenshot',
            'profit_loss',
            'profit_loss_percentage',
        ]
        read_only_fields = ['id', 'opened_at', 'profit_loss', 'profit_loss_percentage']

    def get_profit_loss(self, obj):
        return obj.profit_loss

    def get_profit_loss_percentage(self, obj):
        return obj.profit_loss_percentage
    
    def to_representation(self, instance):
        """Override to return full URL for screenshot"""
        representation = super().to_representation(instance)
        if instance.screenshot:
            request = self.context.get('request')
            if request:
                representation['screenshot'] = request.build_absolute_uri(instance.screenshot.url)
            else:
                representation['screenshot'] = instance.screenshot.url
        return representation
