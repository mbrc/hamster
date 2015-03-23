import os.path
from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    def __repr__(self):
        return "<Artist(name='%s')>" % (self.name)


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


basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'hamster.db'))

Base.metadata.create_all(engine)


# INSERT DUMMY DATA
'''
Session = sessionmaker(bind=engine)
session = Session()

new_artist = Artist(name='Pantera')
session.add(new_artist)
session.commit()

new_album = Album(name='Vulgar Display of Power', year='1992', artist=new_artist)
session.add(new_album)
session.commit()

new_song = Song(name='Rise', album=new_album)
session.add(new_song)
session.commit()

print(new_song)
'''
