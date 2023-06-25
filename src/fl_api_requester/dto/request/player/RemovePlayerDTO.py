from ...DTO import DTO

class RemovePlayerDTO(DTO):
    """
    Request sent to delete a player.
    """

    def __init__(self, nickname: str) -> None:
        self.nickname = nickname
