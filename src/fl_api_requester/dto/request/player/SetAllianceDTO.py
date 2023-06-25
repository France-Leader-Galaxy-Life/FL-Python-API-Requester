from ...DTO import DTO

class SetAllianceDTO(DTO):
    """
    The request made to set the player alliance.
    """

    def __init__(self, player: str, alliance: str) -> None:
        self.player = player
        self.alliance = alliance
