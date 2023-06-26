from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class AddPlanetDTO(DTO):
    """
    Request sent to add a planet to a player.
    """

    player: str
    label: str
    x: int
    y: int
