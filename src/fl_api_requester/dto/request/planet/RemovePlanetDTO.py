from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class RemovePlanetDTO(DTO):
    """
    Request sent to remove a planet from a player.
    """

    player: str
    label: str
