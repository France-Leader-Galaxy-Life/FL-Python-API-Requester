from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class SetRespawnTimerDTO(DTO):
    """
    Request made to update a war respawn timer value.
    """

    alliance: str
    value: int