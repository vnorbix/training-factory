from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Dict

@dataclass
class MusicServiceConfig:
    spotify_client_key: str
    spotify_client_secret: str
    pandora_client_key: str
    pandora_client_secret: str
    local_music_location: str

class MusicService(ABC):
    
    @abstractmethod
    def test_connection(self) -> None:
        raise NotImplementedError()

class MusicServiceBuilder(ABC):
    
    @abstractmethod
    def build(self, config: MusicServiceConfig) -> MusicService:
        raise NotImplementedError()

class MusicServiceProvider:
    def __init__(self) -> None:
        self._builders: Dict[str, MusicServiceBuilder] = {}

    def register_service_builder(self, key: str, builder: MusicServiceBuilder) -> None:
        self._builders[key] = builder

    def get(self, key, config: MusicServiceConfig) -> MusicService:
        builder = self._builders.get(key)
        if not builder:
            raise ValueError(key)
        return builder.build(config)