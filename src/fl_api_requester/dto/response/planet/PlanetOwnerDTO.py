from ...DTO import DTO
from ...response.planet.PlanetDTO import PlanetDTO

class PlanetOwnerDTO(DTO):
    """
    A DTO that associates a planet to its owner.
    """

    def __init__(self, owner: str, planet: PlanetDTO) -> None:
        self.owner = owner
        self.planet = planet
