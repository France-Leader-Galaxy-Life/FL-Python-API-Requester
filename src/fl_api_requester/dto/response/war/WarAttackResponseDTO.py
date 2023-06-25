from ...DTO import DTO
from ...response.player.PlayerDTO import PlayerDTO
from ...response.war.WarDTO import WarDTO

class WarAttackResponseDTO(DTO):
    """
    An attack made during a war.
    """

    def __init__(self, war: WarDTO, attacker: PlayerDTO, defender: str, attackedPlanet: str) -> None:
        self.war = war
        self.attacker = attacker
        self.defender = defender
        self.attacked_planet = attackedPlanet
