from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class DiscordChannelResponseDTO(DTO):
    """
    Represent a Discord server's channel.
    """

    id: int
    type: str
