# TODO: Write a file comment.

import os.path
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
DATABASE_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'hamster.db')


class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __repr__(self):
        return "<Artist(name='%s')>" % self.name


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    year = Column(Integer, nullable=True)
    artist_id = Column(Integer, ForeignKey('artist.id'))
    artist = relationship(Artist)

    def __repr__(self):
        return "<Album(name='%s', year='%s', artist='%s')>" % (self.name, self.year, self.artist)


class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    album_id = Column(Integer, ForeignKey('album.id'))
    album = relationship(Album)

    def __repr__(self):
        return "<Song(name='%s', album='%s')>" % (self.name, self.album)


def create_schema():
    engine = get_engine()
    Base.metadata.create_all(engine)


def get_engine():
    db_path = 'sqlite:///' + DATABASE_PATH
    return create_engine(db_path)


def is_sqlite3(filename):
    if not os.path.isfile(filename):
        return False
    if os.path.getsize(filename) < 100:
        return False

    with open(filename, 'rb') as fp:
        header = fp.read(100)

    return header[0:16] == b'SQLite format 3\000'