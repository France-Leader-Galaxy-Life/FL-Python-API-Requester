from typing import List
from ...DTO import DTO

class RemoveDiscordDTO(DTO):
    """
    Request sent to remove a Discord server.
    """

    def __init__(self, discordId: int) -> None:
        self.discordId = discordId
