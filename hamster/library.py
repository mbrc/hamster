# TODO: Write a file comment.

import db
from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker, exc

class Library:
    artists = {}
    session = None

    def __init__(self):
        engine = db.get_engine()
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def __del__(self):
        self.session.close()

    def add_song(self, attributes):
        artist_name = attributes.get('Artist')
        album_name = attributes.get('Album')
        album_year = attributes.get('Year')
        song_name = attributes.get('Name')

        album_artist = self.get_artist(artist_name)
        song_album = self.get_album(album_name, album_year, album_artist)
        song = db.Song(name=song_name, album=song_album)

        self.session.add(song)
        self.session.commit()

    def add_album(self, album_name, album_year, album_artist):
        album = db.Album(name=album_name, year=album_year, artist=album_artist)
        self.session.add(album)
        self.session.commit()

        return album

    def add_artist(self, artist_name):
        artist = db.Artist(name=artist_name)
        self.session.add(artist)
        self.session.commit()

        return artist

    def get_artist(self, artist_name):
        try:
            return self.session.query(db.Artist).filter(db.Artist.name == artist_name).one()
        except exc.NoResultFound:
            return self.add_artist(artist_name)
        except exc.MultipleResultsFound:
            print("This shouldn't happen.")
            exit()

    def get_album(self, album_name, album_year, album_artist):
        try:
            return self.session.query(db.Album).filter(and_(db.Album.name == album_name,
                                                            db.Album.year == album_year,
                                                            db.Album.artist_id == album_artist.id)).one()
        except exc.NoResultFound:
            return self.add_album(album_name, album_year, album_artist)
        except exc.MultipleResultsFound:
            print("This shouldn't happen.")
            exit()