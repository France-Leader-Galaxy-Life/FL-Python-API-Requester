from typing import List
from ...DTO import DTO
from ...response.alliance.AllianceNameDTO import AllianceNameDTO
from ...response.planet.PlanetDTO import PlanetDTO

class PlayerDTO(DTO):
    """
    Contains the data of a Galaxy Life player.
    """

    def __init__(self, nickname: str, alliance: AllianceNameDTO, planets: List[PlanetDTO]) -> None:
        self.nickname = nickname
        self.alliance = alliance
        self.planets = planets
