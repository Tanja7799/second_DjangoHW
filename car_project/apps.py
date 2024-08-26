from django.apps import AppConfig


class CarProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'car_project'

    def ready(self):
        import car_project.signals
