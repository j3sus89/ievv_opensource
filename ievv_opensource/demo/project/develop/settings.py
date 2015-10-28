from ievv_opensource.demo.project.default.settings import *  # noqa
from ievv_opensource.utils import ievvbuild

THIS_DIR = os.path.dirname(__file__)

IEVVTASKS_DUMPDATA_DIRECTORY = os.path.join(THIS_DIR, 'dumps')


# IEVVTASKS_BUILD_APPS = ievvbuild.config.Apps(
#     ievvbuild.config.App(
#         'superapp',
#         NpmInstall(),
#         BowerInstall(),
#         ievvbuild.lessbuild.Plugin(sourcedirectory='less/themes/default'),
#         ievvbuild.lessbuild.Plugin(sourcedirectory='less/themes/dark'),
#         ievvbuild.lessbuild.Plugin(sourcedirectory='less/themes/red'),
#         CoffeeBuild(sourcedirectory='scripts'),
#         CopyMedia(validate_structure=True,
#                   sourcedirectory='media'),
#     ),
#     ievvbuild.config.App(
#         'themeapp',
#         NpmInstall(),
#         BowerInstall(),
#         LessBuild()
#     ),
# )
