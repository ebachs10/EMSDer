from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "emsder.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import emsder.users.signals  # noqa F401
        except ImportError:
            pass
