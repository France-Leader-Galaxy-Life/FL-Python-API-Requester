from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class StartWarDTO(DTO):
    """
    Request made to start a war.
    """

    alliance: str
