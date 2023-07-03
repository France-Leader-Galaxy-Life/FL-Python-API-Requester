from dataclasses import dataclass
from datetime import datetime
from ...DTO import DTO
from ...response.player.PlayerDTO import PlayerDTO
from ...response.war.WarDTO import WarDTO

@dataclass
class WarAttackResponseDTO(DTO):
    """
    An attack made during a war.
    """

    war: WarDTO
    attacker: PlayerDTO
    defender: str
    attackedPlanet: str
    timestamp: int

    def timestamp_to_datetime(self) -> datetime:
        return datetime.fromtimestamp(float(self.timestamp) / 1000)
