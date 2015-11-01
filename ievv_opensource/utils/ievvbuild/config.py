import logging
import os
from django.apps import apps


class BuildLoggable(object):
    def get_logger_name(self):
        raise NotImplementedError()

    def get_logger(self):
        return logging.getLogger(self.get_logger_name())


class Installer(BuildLoggable):
    name = None

    def __init__(self, app):
        self.app = app

    def get_logger_name(self):
        return '{}.{}'.format(self.app.get_logger_name(), self.name)


class App(BuildLoggable):
    def __init__(self, appname, version, plugins,
                 sourcefolder='staticsources',
                 destinationfolder='static'):
        """
        Parameters:
            appname: Django app label (I.E.: ``myproject.myapp``).
            plugins: Zero or more :class:`ievv_opensource.utils.ievvbuild.pluginbase.Plugin`
                objects.
            sourcefolder: The folder relative to the app root folder where
                static sources (I.E.: less, coffescript, ... sources) are located.
                Defaults to ``staticsources``.
        """
        self.apps = None
        self.version = version
        self.appname = appname
        self.sourcefolder = sourcefolder
        self.destinationfolder = destinationfolder
        self.installers = {}
        self.plugins = []
        for plugin in plugins:
            self.add_plugin(plugin)

    def add_plugin(self, plugin):
        plugin.app = self
        self.plugins.append(plugin)

    def run(self):
        for plugin in self.plugins:
            plugin.run()

    def install(self):
        for plugin in self.plugins:
            plugin.install()
        for installer in self.installers.values():
            installer.install()

    def get_app_config(self):
        """
        Get the AppConfig for the Django app.
        """
        if not hasattr(self, '_app_config'):
            self._app_config = apps.get_app_config(self.appname)
        return self._app_config

    def get_appfolder(self):
        """
        Get the absolute path to the Django app root folder.
        """
        return self.get_app_config().path

    def get_app_path(self, apprelative_path):
        """
        Returns the path to the directory joined with the
        given ``apprelative_path``.
        """
        return os.path.join(self.get_appfolder(), apprelative_path)

    def get_source_path(self, *sourcefolder_relative_path):
        """
        Returns the absolute path to a folder within the source
        folder.
        """
        sourcefolder = os.path.join(self.get_app_path(self.sourcefolder), self.appname)
        if sourcefolder_relative_path:
            return os.path.join(sourcefolder, *sourcefolder_relative_path)
        else:
            return sourcefolder

    def get_destination_path(self, *sourcefolder_relative_path, new_extension=None):
        """
        Returns the absolute path to a folder within the destination
        folder.
        """
        destinationfolder = os.path.join(
            self.get_app_path(self.destinationfolder), self.appname, self.version)
        if sourcefolder_relative_path:
            path = os.path.join(destinationfolder, *sourcefolder_relative_path)
            if new_extension:
                path, extension = os.path.splitext(path)
                path = path + new_extension
                return path
        else:
            return destinationfolder

    def watch(self):
        """
        Start a watcher thread, and trigger run in all plugins when file change is
        detected. Only trigger run if plugin.get_watch_file_patterns matches the
        changed file.
        """
        # for plugin in self.plugins:
        #     try:
        #         plugin.watch()
        #     except NotImplementedError:
        #         pass

    # def get_buildfolder(self):
    #     return os.path.join(self.apps.buildfolder, self.appname)

    def get_installer(self, installerclass):
        if installerclass.name not in self.installers:
            installer = installerclass(app=self)
            self.installers[installerclass.name] = installer
        return self.installers[installerclass.name]

    def get_logger_name(self):
        return '{}.{}'.format(self.apps.get_logger_name(), self.appname)


class Apps(BuildLoggable):
    def __init__(self, *apps):
        self.apps = []
        for app in apps:
            self.add_app(app)

    def add_app(self, app):
        app.apps = self
        self.apps.append(app)

    def install(self):
        for app in self.apps:
            app.install()

    def run(self):
        for app in self.apps:
            app.run()

    def watch(self):
        for app in self.apps:
            app.watch()

    def get_logger_name(self):
        return 'ievvbuild'

    def configure_logging(self, loglevel=logging.INFO):
        formatter = logging.Formatter('[%(name)s:%(levelname)s] %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.setLevel(loglevel)

        logger = self.get_logger()
        logger.setLevel(loglevel)
        logger.addHandler(handler)
        logger.propagate = False

        shlogger = logging.getLogger('sh.command')
        shlogger.setLevel(loglevel)
        shlogger.addHandler(handler)
        shlogger.propagate = False
