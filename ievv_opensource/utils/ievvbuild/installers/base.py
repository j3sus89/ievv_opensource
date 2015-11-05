from ievv_opensource.utils.ievvbuild.buildloggable import BuildLoggable
from ievv_opensource.utils.ievvbuild.executablebase import ExecutableMixin


class AbstractInstaller(BuildLoggable, ExecutableMixin):
    name = None

    def __init__(self, app):
        self.app = app

    def get_logger_name(self):
        return '{}.{}'.format(self.app.get_logger_name(), self.name)
