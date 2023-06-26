class FLAPIConnectionData:
    """
    Contains all the connection data of the API (credentials, Discord server's ID...).
    """

    def __init__(self) -> None:
        self.api_uri = None
        self.username = None
        self.password = None
        self.token = None
        self.discord_id = None

    def get_api_uri(self) -> str:
        """
        Returns the defined API URI.
        """
        return self.api_uri

    def get_credentials(self) -> tuple[str, str]:
        """
        Returns the user credentials as a tuple. The tuples is formatted as following : (username, password).
        The tuple values can be None if the credentials hasn't been set.
        """
        return (self.username, self.password)
    
    def get_token(self) -> str:
        """
        Returns the current connection token. Returns None if the token hasn't been set.
        """
        return self.token

    def get_discord_id(self) -> int:
        """
        Returns the Discord server's ID that make the request. Returns None if the ID hasn't been set.
        """
        return self.discord_id

    def set_api_uri(self, api_uri: str) -> None:
        """
        Set the API URI.

        Parameters
        ----------
        - api_uri: `str`
            The API URI to define.
        """
        self.api_uri = api_uri

    def set_credentials(self, username: str, password: str) -> None:
        """
        Set the current connection credentials.

        Parameters
        ----------
        - username: `str`
            The username of the user that make the request.
        - password: `str`
            The password of the user that make the request.
        """
        self.username = username
        self.password = password

    def set_token(self, token: str) -> None:
        """
        Set the current connection token.

        Parameters
        ----------
        - token: `str`
            The token value.
        """
        self.token = token

    def set_discord_id(self, id: int) -> None:
        """
        Set the current connection Discord server's ID.

        Parameters
        ----------
        - id: `int`
            The Discord server's ID.
        """
        self.discord_id = id
