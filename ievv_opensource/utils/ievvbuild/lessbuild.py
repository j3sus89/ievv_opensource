import os
import sh
from ievv_opensource.utils.ievvbuild import pluginbase
from ievv_opensource.utils.ievvbuild.installers.npm import NpmInstaller


class Plugin(pluginbase.Plugin):
    name = 'lessbuild'

    def __init__(self, sourcefile):
        self.sourcefile = os.path.join('styles', sourcefile)

    def get_sourcefile_path(self):
        return self.app.get_source_path(self.sourcefile)

    def get_destinationfile_path(self):
        return self.app.get_destination_path(
            self.sourcefile, new_extension='.css')

    def install(self):
        self.app.get_installer(NpmInstaller).queue_install('less')

    def run(self):
        lessc = sh.Command(self.app.get_installer(NpmInstaller).find_executable(
            'lessc'))
        output = lessc(self.get_sourcefile_path(), self.get_destinationfile_path())
        self.get_logger().info(output)
