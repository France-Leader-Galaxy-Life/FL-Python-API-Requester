from dataclasses import dataclass
from typing import List
from ...DTO import DTO

@dataclass
class AddAllianceToDiscordDTO(DTO):
    """
    Request sent to add alliances to a Discord server.
    """

    discordId: int
    alliances: List[str]
