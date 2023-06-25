from ...DTO import DTO

class AuthenticationResponseDTO(DTO):
    """
    Represents the response sent to an authenticated user. It contains the token to use to make requests to the API.
    """

    def __init__(self, token: str) -> None:
        self.token = token