# TODO: Write a file comment.

from artist import Artist
from album import Album
from song import Song

class Library:
    artists = {}

    def __init__(self):
        pass

    def add_track(self, id, attributes):
        artist_name = attributes.get('Artist')
        album_name = attributes.get('Album')
        album_year = attributes.get('Year')
        song_name = attributes.get('Name')
        song_number = attributes.get('Track Number')

        # TODO: Stuff.
