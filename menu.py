from AutoLoader import AutoLoader

myToolbar = nuke.menu('Nodes').addMenu('MyGizmos')
loader = AutoLoader(r"C:\Users\isaac.spiegel\.nuke\gizmos", myToolbar)
loader.populate_toolbar()
