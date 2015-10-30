import os
from django.apps import apps


class App(object):
    def __init__(self, appname, *plugins, sourcefolder='staticsources'):
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
        self.appname = appname
        self.sourcefolder = sourcefolder
        self.plugins = []
        for plugin in plugins:
            self.add_plugin(plugin)

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def run(self):
        for plugin in self.plugins:
            try:
                plugin.run()
            except NotImplementedError:
                pass

    def get_app_config(self):
        """
        Get the AppConfig for the Django app.
        """
        if not hasattr(self, '_app_config'):
            self._app_config = apps.get_app_config('admin')
        return self._app_config

    def get_appfolder(self):
        """
        Get the absolute path to the Django app root folder.
        """
        return self.get_app_config().path

    def build_app_path(self, apprelative_path):
        """
        Returns the path to the directory joined with the
        given ``apprelative_path``.
        """
        return os.path.join(self.get_appfolder(), apprelative_path)

    def build_source_path(self, sourcefolder_relative_path):
        """
        Returns a path built by joining the Django app root directory
        with the ``sourcefolder`` provided to ``__init__``, the
        """

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


class Apps(object):
    def __init__(self, *apps):
        self.apps = []
        for app in apps:
            self.add_app(app)

    def add_app(self, app):
        app.apps = app
        self.apps[app.name] = app

    def run(self):
        for app in self.apps:
            app.run()

    def watch(self):
        for app in self.apps:
            app.watch()
