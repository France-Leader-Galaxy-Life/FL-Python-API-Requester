from typing import List
from ...DTO import DTO

class CreateDiscordDTO(DTO):
    """
    Request sent to create a Discord.
    """

    def __init__(self, id: int, alliances: List[str]) -> None:
        self.id = id
        self.alliances = alliances
