from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class DiscordChannelRequestDTO(DTO):
    """
    Object sent to create or add a channel to a Discord server.
    """

    id: int
    type: str
    allianceId: int
