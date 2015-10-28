class App(object):
    def __init__(self, appname, *plugins):
        self.apps = None
        self.appname = appname
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
