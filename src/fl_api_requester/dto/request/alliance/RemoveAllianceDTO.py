from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class RemoveAllianceDTO(DTO):
    """
    Request made to remove an alliance.
    """

    name: str
