from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class CreatePlayerDTO(DTO):
    """
    Player creation request.
    """

    nickname: str
