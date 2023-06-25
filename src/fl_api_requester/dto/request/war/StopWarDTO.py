from ...DTO import DTO

class StopWarDTO(DTO):
    """
    Request made to stop a war.
    """

    def __init__(self, alliance: str) -> None:
        self.alliance = alliance
