from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class AllianceNameDTO(DTO):
    """
    Contains an alliance's name.
    """

    id: int
    name: str
