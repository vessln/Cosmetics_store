from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cosmetics_store.orders'

    def ready(self):
        import cosmetics_store.orders.signals
