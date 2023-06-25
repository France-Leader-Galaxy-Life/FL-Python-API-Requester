from ...DTO import DTO

class AllianceNameDTO(DTO):
    """
    Contains an alliance's name.
    """

    def __init__(self, name: str) -> None:
        self.name = name