class Plugin(object):
    def __init__(self):
        self.app = None
        self.is_executing = False

    def run(self):
        raise NotImplementedError()

    def get_watch_file_patterns(self):
        return r'.*'
