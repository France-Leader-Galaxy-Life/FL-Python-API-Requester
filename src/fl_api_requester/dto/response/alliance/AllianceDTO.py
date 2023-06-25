from typing import List
from ...DTO import DTO
from ...response.war.WarDTO import WarDTO

class AllianceDTO(DTO):
    """
    Contains the data of a Galaxy Life alliance.
    """

    def __init__(self, name: str, players: List[str], wars: List[WarDTO]) -> None:
        self.name = name
        self.players = players
        self.wars = wars