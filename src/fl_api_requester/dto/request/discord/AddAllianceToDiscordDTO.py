from typing import List
from ...DTO import DTO

class AddAllianceToDiscordDTO(DTO):
    """
    Request sent to add alliances to a Discord server.
    """

    def __init__(self, discord_id: int, alliances: List[str]) -> None:
        self.discord_id = discord_id
        self.alliances = alliances
