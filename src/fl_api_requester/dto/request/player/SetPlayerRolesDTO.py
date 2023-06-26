from dataclasses import dataclass
from typing import List
from ...DTO import DTO

@dataclass
class SetPlayerRolesDTO(DTO):
    """
    Request that contains some API roles to associate to a player.
    """

    player: str
    roles: List[str]
