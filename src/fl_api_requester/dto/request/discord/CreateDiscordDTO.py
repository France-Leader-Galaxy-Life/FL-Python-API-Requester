from dataclasses import dataclass
from typing import List
from ...DTO import DTO

@dataclass
class CreateDiscordDTO(DTO):
    """
    Request sent to create a Discord.
    """

    id: int
    alliances: List[str]
