from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.alliance.AllianceDTO import AllianceDTO

@dataclass
class DiscordDTO(DTO):
    """
    Associates a Discord server to its alliances.
    """

    id: int
    alliances: List[AllianceDTO]
