from ...DTO import DTO

class StartWarDTO(DTO):
    """
    Request made to start a war.
    """

    def __init__(self, alliance: str) -> None:
        self.alliance = alliance
