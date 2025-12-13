from django.apps import AppConfig

class App33Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App33'

    def ready(self):
        import App33.signals
