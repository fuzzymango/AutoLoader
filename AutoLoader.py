import nuke
import typing
from pathlib import Path
'''
TODO:
- expand program to run with scripts
'''

class AutoLoader():
    VALID_GIZMO_FILE_TYPES = ['.gizmo', '.nk']
    VALID_ICON_FILE_TYPES = ['.jpg', '.jpeg', '.png']

    def __init__(self, directory: str, toolbar: object) -> None:
        '''
        Constructor to initialize the object

        Parameters
        ----------
        directory: str
            The file path to load gizmos from
        toolbar: Nuke Toolbar
            The in-software Nuke toolbar to load the gizmos to
        '''
        self.directory = directory
        self.toolbar = toolbar

    def retrieve_relative_path(self, file: Path, relative_to: str = '.nuke') -> str:
        '''
        Takes in a file path and returns everything after the 'relative_to' param
        as a string representation of the file path. If the input paths to a
        file (not folder) the file extention is removed from the relative path.

        Parameters
        ---------
        file: Path
            A full-length file path

        relative_to: str
            An optional input to define a different relative path other than .nuke
        Returns
        -------
        relative_path: str
            The file path relative to the cut off point. If it's a file (not folder)
            the extension is removed when returned.
        '''
        relative_path_start = file.parts.index('.nuke') + 1
        relative_path_parts = file.parts[relative_path_start:]
        relative_path = ""
        for index, part in enumerate(relative_path_parts):
            if index == 0:
                relative_path = f"{part}"
            elif index == len(relative_path_parts) - 1:
                relative_path = f"{relative_path}/{file.stem}"
            else:
                relative_path = f"{relative_path}/{part}"
        return relative_path

    def fetch_icons(self, folder: Path) -> dict:
        '''
        Creates a dictionary of all files in the specified directory containing
        an extension defined in VALID_ICON_FILE_TYPES

        Parameters
        ---------
        folder: Path
            A full-length file path

        Returns
        -------
        icons: dict
            A dictionary containing the stem of the image file (no extension) for
            the keys and the name of the image file (with extension) for the
            values.
        '''
        icons = {}
        for file in folder.glob('*.*'):
            if file.suffix in self.VALID_ICON_FILE_TYPES:
                icons.update({file.stem: file.name})
        return icons

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
        nuke.pluginAddPath(self.directory, False)
        p = Path(self.directory)
        for folder in p.glob('**/'):
            if folder.name != p.name:
                nuke.pluginAddPath(self.retrieve_relative_path(folder))
            icons = self.fetch_icons(folder)
            for file in folder.glob('*.*'):
                if file.suffix in self.VALID_GIZMO_FILE_TYPES:
                    shelf_name = self.retrieve_relative_path(file)
                    create_node = f"nuke.createNode('{file.stem}')"
                    if file.stem in icons:
                        icon_tile = icons[file.stem]
                    else:
                        icon_tile = ""
                    self.toolbar.addCommand(shelf_name, create_node, icon=icon_tile)
