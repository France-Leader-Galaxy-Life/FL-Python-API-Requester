from dataclasses import dataclass
from typing import List
from ...DTO import DTO
from ...request.discord_channel.DiscordChannelRequestDTO import DiscordChannelRequestDTO

@dataclass
class AddChannelsToDiscordDTO(DTO):
    """
    Request sent to add some channels to a Discord server.
    """

    discordId: int
    channels: List[DiscordChannelRequestDTO]
