import nuke
import typing
from pathlib import Path
'''
TODO:
folders aren't adding in correct order
add icon loading functionality
'''

class GizmoAutoLoader():
    VALID_GIZMO_FILE_TYPES = ['.gizmo', '.nk']
    VALID_ICON_FILE_TYPES = ['.jpg', '.jpeg', '.png']

    def __init__(self, directory: str, toolbar) -> None:
        '''
        Constructor to initilize the object

        Parameters
        ----------
        directory: str
            The file path to load gizmos from
        toolbar: Nuke Toolbar
            The in-software Nuke toolbar to load the gizmos to
        '''
        self.directory = directory
        self.toolbar = toolbar
        self.populate_toolbar()

    def populate_toolbar(self) -> None:
        '''
        Loads all .gizmo and .nk files from ``directory`` to the ``toolbar``

        Parameters
        ----------
        directory: str
            The file path to load the gizmos from

        Returns
        -------
        None
        '''
        icons = {}
        nuke.pluginAddPath(self.directory, False)
        p = Path(self.directory)
        relative_path = f"{p.name}"
        for folder in p.glob('**/'):
            if folder.name != p.name:
                relative_path = f"{relative_path}/{folder.name}"
                nuke.pluginAddPath(relative_path, False)
            for file in folder.glob('*.*'):
                if file.suffix in self.VALID_ICON_FILE_TYPES:
                    icon_name = file.stem
                    icon_relative_path = f"{relative_path}/{file.name}"
                    icons.update({icon_name: icon_relative_path})
                if file.suffix in self.VALID_GIZMO_FILE_TYPES:
                    shelf_name = f"{relative_path}/{file.stem}"
                    create_node = f"nuke.createNode('{file.stem}')"
                    if file.stem in icons:
                        icon = icons[file.stem]
                    else:
                        icon = ""
                    self.toolbar.addCommand(shelf_name, create_node, icon)
