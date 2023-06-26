from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.alliance.AllianceNameDTO import AllianceNameDTO
from ...response.planet.PlanetDTO import PlanetDTO

@dataclass
class PlayerDTO(DTO):
    """
    Contains the data of a Galaxy Life player.
    """

    nickname: str
    alliance: AllianceNameDTO
    planets: List[PlanetDTO]
    currentWarPoints: int
