from ...DTO import DTO

class RemovePlanetDTO(DTO):
    """
    Request sent to remove a planet from a player.
    """

    def __init__(self, player: str, label: str) -> None:
        self.player = player
        self.label = label
