# TODO: Write a file comment.

import os.path
import plistlib
from library import Library

class XMLImporter:
    def __init__(self):
        pass

    def import_xml(self, path = None):
        library_path = self.get_library_file_path(path)

        with open(library_path, 'rb') as fp:
            pl = plistlib.load(fp)

        library = Library()

        for id, attributes in pl['Tracks'].items():
            # Only add songs to library. Podcasts and other types can be skipped.
            if attributes.get('Track Type') == 'File':
                library.add_track(id, attributes)

        return library

    def get_library_file_path(self, path):
        default_path = os.path.expanduser('~/Music/iTunes/iTunes Music Library.xml')

        if path is not None and os.path.isfile(path):
            return path
        elif os.path.isfile(default_path):
            return default_path

        raise OSError('No library file found.')
