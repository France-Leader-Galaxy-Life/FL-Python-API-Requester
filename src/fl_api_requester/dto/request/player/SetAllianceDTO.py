from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class SetAllianceDTO(DTO):
    """
    The request made to set the player alliance.
    """

    player: str
    alliance: str
