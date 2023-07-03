from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ..discord_channel.DiscordChannelRequestDTO import DiscordChannelRequestDTO

@dataclass
class CreateDiscordDTO(DTO):
    """
    Request sent to create a Discord.
    """

    id: int
    alliances: List[str]
    channels: List[DiscordChannelRequestDTO]
