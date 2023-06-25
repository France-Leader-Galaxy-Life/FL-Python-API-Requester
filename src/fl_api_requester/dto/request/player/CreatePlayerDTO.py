from ...DTO import DTO

class CreatePlayerDTO(DTO):
    """
    Player creation request.
    """

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
