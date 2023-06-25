from typing import List
from ...DTO import DTO
from ...response.alliance.AllianceDTO import AllianceDTO

class DiscordDTO(DTO):
    """
    Associates a Discord server to its alliances.
    """

    def __init__(self, id: int, alliances: List[AllianceDTO]) -> None:
        self.id = id
        self.alliances = alliances