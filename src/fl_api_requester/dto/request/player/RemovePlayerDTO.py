from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class RemovePlayerDTO(DTO):
    """
    Request sent to delete a player.
    """
    
    nickname: str
