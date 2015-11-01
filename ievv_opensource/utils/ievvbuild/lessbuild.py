import sh
from ievv_opensource.utils.ievvbuild import pluginbase
from ievv_opensource.utils.ievvbuild.installers.npm import NpmInstaller


class Plugin(pluginbase.Plugin):
    name = 'lessbuild'

    def __init__(self, sourcefolder=None, destinationfolder=None):
        self.sourcefolder = sourcefolder
        self.destinationfolder = destinationfolder

    def install(self):
        self.app.get_installer(NpmInstaller).install('lessc')

    def run(self):
        lessc = sh.Command(self.app.get_installer(NpmInstaller).find_executable('lessc'))
        lessc()


# class BowerInstall(PluginBase):
#     pass
#
#
# class NpmInstall(PluginBase):
#     pass
#
#
# class CoffeeBuild(PluginBase):
#     pass
