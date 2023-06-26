from dataclasses import dataclass
from typing import List
from ...DTO import DTO

@dataclass
class AddAllianceToDiscordDTO(DTO):
    """
    Request sent to add alliances to a Discord server.
    """

    discord_id: int
    alliances: List[str]
