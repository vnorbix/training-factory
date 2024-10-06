import json
import xml.etree.ElementTree as et

class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist

def _get_serializer(format):
    if format == 'JSON':
        return _serialize_json
    elif format == 'XML':
        return _serialize_xml
    else:
        raise ValueError(format)

def _serialize_json(song):
    song_info = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(song_info)
    
def _serialize_xml(song):
    song_info = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_info, 'title')
    title.text = song.title
    artist = et.SubElement(song_info, 'artist')
    artist.text = song.artist
    return et.tostring(song_info, encoding='unicode')

class SongSerializer:
    def serialize(self, song, format):
        serializer = _get_serializer(format)
        return serializer(song)

song = Song('1', 'Water of Love', 'Dire Straits')
serializer = SongSerializer()
print(serializer.serialize(song, 'JSON'))
print(serializer.serialize(song, 'XML'))
serializer.serialize(song, 'YAML')