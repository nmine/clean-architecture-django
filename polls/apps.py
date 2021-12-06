from django.apps import AppConfig
from dependency_injector import providers

from cleanarchi import container


class PollsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'polls'

    config = providers.Configuration()

    def ready(self):
        container.wire(modules=[".views"])
