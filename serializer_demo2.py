import songs
import serializers

song = songs.Song('1', 'Water of Love', 'Dire Straits')
serializer = serializers.ObjectSerializer()
print(serializer.serialize(song, "JSON"))
print(serializer.serialize(song, "XML"))
print(serializer.serialize(song, "YAML"))