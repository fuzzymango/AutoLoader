import AutoLoader

myToolbar = nuke.menu('Nodes').addMenu('MyGizmos')
AutoLoader.AutoLoader(r"C:\Users\isaac.spiegel\.nuke\gizmos", myToolbar)
