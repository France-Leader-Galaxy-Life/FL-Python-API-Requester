from ...DTO import DTO

class AddPlanetDTO(DTO):
    """
    Request sent to add a planet to a player.
    """

    def __init__(self, player: str, label: str, x: int, y: int) -> None:
        self.player = player
        self.label = label
        self.x = x
        self.y = y
