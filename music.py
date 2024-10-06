from music_service_provider import MusicService, MusicServiceBuilder, MusicServiceConfig, MusicServiceProvider
from typing import Any, Optional



class SpotifyService(MusicService):

    def __init__(self, access_code: str) -> None:
        self._access_code = access_code

    def test_connection(self):
        print(f'Accessing Spotify with {self._access_code}')

class SpotifyServiceBuilder(MusicServiceBuilder):

    def __init__(self) -> None:
        self._instance: Optional[SpotifyService] = None

    def build(self, config: MusicServiceConfig) -> SpotifyService:
        if not self._instance:
            access_code = self.authorize(
                config.spotify_client_key, config.spotify_client_secret
            )
            self._instance = SpotifyService(access_code)
        return self._instance

    def authorize(self, key: str, secret: str):
        return "SPOTIFY ACCESS CODE"

class PandoraService(MusicService):
    def __init__(self, consumer_key: str, consumer_secret: str) -> None:
        self._key = consumer_key
        self._secret = consumer_secret

    def test_connection(self):
        print(f"Accessing Pandora with {self._key} and {self._secret}")

class PandoraServiceBuilder(MusicServiceBuilder):
    def __init__(self) -> None:
        self._instance: Optional[PandoraService] = None

    def build(self, config: MusicServiceConfig) -> Any:
        if not self._instance:
            consumer_key, consumer_secret = self.authorize(
                config.pandora_client_key, config.pandora_client_secret
            )
            self._instance = PandoraService(consumer_key, consumer_secret)
        return self._instance

    def authorize(self, key: str, secret: str):
        return "PANDORA_CONSUMER_KEY", "PANDORA_CONSUMER_SECRET"

class LocalService(MusicService):
    def __init__(self, location: str) -> None:
        self._location = location

    def test_connection(self):
        print(f'accessing local music at {self._location}')

class LocalServiceBuilder(MusicServiceBuilder):
    def build(self, config: MusicServiceConfig) -> MusicService:
        return LocalService(config.local_music_location)

services = MusicServiceProvider()
services.register_service_builder("SPOTIFY", SpotifyServiceBuilder())
services.register_service_builder("PANDORA", PandoraServiceBuilder())
services.register_service_builder("LOCAL", LocalServiceBuilder())