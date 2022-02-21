from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        from . import signals

default_app_config = 'users.apps.UsersConfig'
