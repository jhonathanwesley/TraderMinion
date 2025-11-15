from django.contrib import admin
from .models import Trade


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('asset', 'type', 'status', 'quantity', 'entry_price', 'exit_price', 'opened_at')
    list_filter = ('status', 'type', 'category', 'opened_at')
    search_fields = ('asset', 'notes')
    readonly_fields = ('opened_at', 'profit_loss', 'profit_loss_percentage')
    
    fieldsets = (
        ('Basic Info', {
            'fields': ('asset', 'type', 'category', 'status')
        }),
        ('Trade Details', {
            'fields': ('quantity', 'entry_price', 'exit_price', 'stop_loss', 'take_profit')
        }),
        ('Time & Notes', {
            'fields': ('opened_at', 'closed_at', 'notes', 'screenshot')
        }),
        ('Calculated Fields', {
            'fields': ('profit_loss', 'profit_loss_percentage'),
            'classes': ('collapse',)
        }),
    )
