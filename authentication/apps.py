from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'

    # Using signals in our app
    def ready(self):
        import authentication.signals
