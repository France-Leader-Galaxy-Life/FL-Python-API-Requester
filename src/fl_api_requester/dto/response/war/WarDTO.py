from ...DTO import DTO
from ...response.alliance.AllianceNameDTO import AllianceNameDTO

class WarDTO(DTO):
    """
    Represents a Galaxy Life war.
    """

    def __init__(
        self, 
        alliance: AllianceNameDTO, 
        opponent: AllianceNameDTO, 
        alliancePoints: int, 
        opponentPoints: int, 
        status: str
    ) -> None:
        self.alliance = alliance
        self.opponent = opponent
        self.alliancePoints = alliancePoints
        self.opponentPoints = opponentPoints
        self.status = status