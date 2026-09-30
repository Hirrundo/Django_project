from django.apps import AppConfig


class CartsConfig(AppConfig):
    name = 'apps.carts'

    def ready(self):
        import apps.carts.signals
