# TODO: Write a file comment.

from song import Song

class Album:
    name = None
    year = None
    songs = {}

    def __init__(self, name, year):
        self.name = name
        self.year = year
