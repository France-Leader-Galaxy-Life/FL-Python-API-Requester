from dataclasses import dataclass
from typing import List
from ...DTO import DTO

@dataclass
class RemoveChannelsFromDiscordDTO(DTO):
    """
    Request sent to remove some channels from a Discord server.
    """

    discordId: int
    channels: List[int]
