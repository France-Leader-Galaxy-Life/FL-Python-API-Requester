from dataclasses import dataclass
from ...DTO import DTO

@dataclass
class AuthenticationResponseDTO(DTO):
    """
    Represents the response sent to an authenticated user. It contains the token to use to make requests to the API.
    """

    token: str