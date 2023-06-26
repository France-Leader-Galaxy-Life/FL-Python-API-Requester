from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class CreateAllianceDTO(DTO):
    """
    An alliance creation request.
    """

    name: str
