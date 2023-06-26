from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class StopWarDTO(DTO):
    """
    Request made to stop a war.
    """

    alliance: str
