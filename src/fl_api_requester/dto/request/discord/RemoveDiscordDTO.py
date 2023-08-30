from dataclasses import dataclass
from typing import List
from ...DTO import DTO

@dataclass
class RemoveDiscordDTO(DTO):
    """
    Request sent to remove a Discord server.
    """

    discordId: int
