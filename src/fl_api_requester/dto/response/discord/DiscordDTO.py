from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.alliance.AllianceDTO import AllianceDTO
from ...response.discord_channel.DiscordChannelResponseDTO import DiscordChannelResponseDTO

@dataclass
class DiscordDTO(DTO):
    """
    Associates a Discord server to its alliances.
    """

    id: int
    alliances: List[AllianceDTO]
    channel: List[DiscordChannelResponseDTO]
