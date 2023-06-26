from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class PlanetDTO(DTO):
    """
    Contains the data of a Galaxy Life planet (don't contain the planet owner).
    """

    label: str
    x: int
    y: int
