from django.contrib import admin
from .api.v1.models import Quote

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        'from_currency_code', 
        'to_currency_code',
        'exchange_rate',
        'last_refreshed',
        'time_zone'
    )
admin.site.register(Quote, QuoteAdmin)