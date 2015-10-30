import sh
from ievv_opensource.utils.ievvbuild import pluginbase


class Plugin(pluginbase.Plugin):
    def __init__(self, sourcefolder=None, destinationfolder=None):
        self.sourcefolder = sourcefolder
        self.destinationfolder = destinationfolder

    def run(self):
        lessc = sh.Command('lessc')
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
