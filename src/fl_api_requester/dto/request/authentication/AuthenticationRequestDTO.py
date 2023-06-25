from ...DTO import DTO

class AuthenticationRequestDTO(DTO):
    """
    Represents a login request.
    """

    def __init__(self, login: str, password: str) -> None:
        self.login = login
        self.password = password
