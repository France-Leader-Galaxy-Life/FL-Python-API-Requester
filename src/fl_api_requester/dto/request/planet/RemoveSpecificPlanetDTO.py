from ...DTO import DTO

class RemoveSpecificPlanetDTO(DTO):
    """
    Request sent to remove a planet from a player.
    """

    def __init__(self, player: str, label: str, x: int, y: int) -> None:
        self.player = player
        self.label = label
        self.x = x
        self.y = y
