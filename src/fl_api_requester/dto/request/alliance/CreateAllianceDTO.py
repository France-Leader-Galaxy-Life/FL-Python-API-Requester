from ...DTO import DTO

class CreateAllianceDTO(DTO):
    """
    An alliance creation request.
    """

    def __init__(self, name: str) -> None:
        self.name = name
