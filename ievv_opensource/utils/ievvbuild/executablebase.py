import sh


class ExecutableMixin(object):
    def execute(self, executable, *args, **kwargs):
        self.get_logger().info('Executing: %s args=%r kwargs=%r',
                               executable, args, kwargs)
        command = sh.Command(executable)
        command(*args, **kwargs)
