from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class AuthenticationRequestDTO(DTO):
    """
    Represents a login request.
    """

    login: str
    password: str
