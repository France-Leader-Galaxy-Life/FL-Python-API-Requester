from ...DTO import DTO

class PlanetDTO(DTO):
    """
    Contains the data of a Galaxy Life planet (don't contain the planet owner).
    """

    def __init__(self, label: str, x: int, y: int) -> None:
        self.label = label
        self.x = x
        self.y = y
