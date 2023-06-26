from dataclasses import dataclass
from ...DTO import DTO
from ...response.planet.PlanetDTO import PlanetDTO

@dataclass
class PlanetOwnerDTO(DTO):
    """
    A DTO that associates a planet to its owner.
    """

    owner: str
    planet: PlanetDTO
