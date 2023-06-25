from ...DTO import DTO

class RemoveAllianceDTO(DTO):
    """
    Request made to remove an alliance.
    """

    def __init__(self, name: str) -> None:
        self.name = name
