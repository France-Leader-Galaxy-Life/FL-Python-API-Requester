from typing import List
from ...DTO import DTO

class SetPlayerRolesDTO(DTO):
    """
    Request that contains some API roles to associate to a player.
    """

    def __init__(self, player: str, roles: List[str]) -> None:
        self.player = player
        self.roles = roles
