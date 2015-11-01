from ievv_opensource.utils.ievvbuild import config


class NpmInstaller(config.Installer):
    name = 'npminstall'

    def install(self, package, version=None):
        """
        Installs the given npm package in the build
        directory for the app.

        Does nothing if the package is already installed.

        Raises ValueError if the package is already installed,
        but with a different version (this check is not made if
        version is ``None``).
        """
        self.get_logger().info('Installing %s (version=%s)', package, version)

    def find_executable(self, executablename):
        """
        Find an executable named ``executablename``.

        Returns the absolute path to the executable.
        """
