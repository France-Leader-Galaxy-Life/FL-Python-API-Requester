from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class WarAttackRequestDTO(DTO):
    """
    Request sent to indicates that a player attacked a planet during a war.
    """

    attacker: str
    defender: str
    planetLabel: str
