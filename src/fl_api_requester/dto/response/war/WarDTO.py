from dataclasses import dataclass
from ...DTO import DTO
from ...response.alliance.AllianceNameDTO import AllianceNameDTO

@dataclass
class WarDTO(DTO):
    """
    Represents a Galaxy Life war.
    """

    alliance: AllianceNameDTO 
    opponent: AllianceNameDTO 
    alliancePoints: int 
    opponentPoints: int 
    status: str
