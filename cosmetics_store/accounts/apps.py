from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cosmetics_store.accounts'

    def ready(self):
        import cosmetics_store.accounts.signals

