from dataclasses import dataclass
from datetime import datetime
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
    respawnTimer: int
    status: str
    startTimestamp: int

    def timestamp_to_datetime(self) -> datetime:
        return datetime.fromtimestamp(float(self.startTimestamp) / 1000)
