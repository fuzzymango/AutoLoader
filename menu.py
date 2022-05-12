'''
ENABLE THE AUTO LOADER

If the below statements are confusing or if your gizmos are stored all
around your .nuke folder, use loader = AutoLoader()

AutoLoader takes two optional arguments. 1) a file path to your gizmos and 2) a
nuke toolbar to load them on to.

EXAMPLE:
# this loads all the gizmos from the .nuke\gizmos folder into a toolbar called MyGizmos
myToolbar = nuke.menu('Nodes').addMenu('MyGizmos')
loader = AutoLoader(toolbar = myToolbar, directory = r"C:\Users\isaac.spiegel\.nuke\gizmos")
'''
from AutoLoader import AutoLoader
loader = AutoLoader()
loader.populate_toolbar()
