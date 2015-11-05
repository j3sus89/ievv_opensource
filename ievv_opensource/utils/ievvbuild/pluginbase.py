from ievv_opensource.utils.ievvbuild.buildloggable import BuildLoggable


class Plugin(BuildLoggable):
    name = None

    def __init__(self):
        self.app = None
        self.is_executing = False

    def install(self):
        """
        Install any packages required for this plugin.

        Should use :meth:`ievv_opensource.utils.ievvbuild.config.App.get_installer`.

        Examples:

            Install an npm package::

                def install(self):
                    self.app.get_installer(NpmInstaller).install(
                        'somepackage')
                    self.app.get_installer(NpmInstaller).install(
                        'otherpackage', version='~1.0.0')
        """

    def run(self):
        pass

    def get_watch_file_patterns(self):
        return r'.*'

    def get_logger_name(self):
        return '{}.{}'.format(self.app.get_logger_name(), self.name)
