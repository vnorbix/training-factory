from music_service_provider import MusicServiceConfig
from music import services 

config = MusicServiceConfig(
    'THE_SPOTIFY_CLIENT_KEY',
    'THE_SPOTIFY_CLIENT_SECRET',
    'THE_PANDORA_CLIENT_KEY',
    'THE_PANDORA_CLIENT_SECRET',
    '/usr/data/music'
)

pandora = services.get("PANDORA", config)
pandora.test_connection()

spotify = services.get("SPOTIFY", config)
spotify.test_connection()

local = services.get("LOCAL", config)
local.test_connection()

pandora2 = services.get("PANDORA", config)
print(f"{(id(pandora) == id(pandora2))=}")

spotify2 = services.get("SPOTIFY", config)
print(f"{(id(spotify) == id(spotify2))=}")

local2 = services.get("LOCAL", config)
print(f"{(id(local) == id(local2))=}")