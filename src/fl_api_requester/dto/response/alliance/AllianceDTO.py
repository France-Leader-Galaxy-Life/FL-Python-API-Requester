from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...response.war.WarDTO import WarDTO
from ...response.player.PlayerDTO import PlayerDTO
from ...response.discord_channel.DiscordChannelResponseDTO import DiscordChannelResponseDTO

@dataclass
class AllianceDTO(DTO):
    """
    Contains the data of a Galaxy Life alliance.
    """

    id: int
    name: str
    players: List[PlayerDTO]
    wars: List[WarDTO]
    channels: List[DiscordChannelResponseDTO]
