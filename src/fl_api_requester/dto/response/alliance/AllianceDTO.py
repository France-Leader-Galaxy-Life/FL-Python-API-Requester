from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.war.WarDTO import WarDTO
from ...response.player.PlayerDTO import PlayerDTO

@dataclass
class AllianceDTO(DTO):
    """
    Contains the data of a Galaxy Life alliance.
    """

    name: str
    players: List[PlayerDTO]
    wars: List[WarDTO]