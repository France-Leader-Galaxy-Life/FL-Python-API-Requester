from ...DTO import DTO

class WarAttackRequestDTO(DTO):
    """
    Request sent to indicates that a player attacked a planet during a war.
    """

    def __init__(self, attacker: str, defender: str, planet_label: str) -> None:
        self.attacker = attacker
        self.defender = defender
        self.planetLabel = planet_label
