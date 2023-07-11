from typing import Dict, List
from dacite import from_dict
import requests

from . import FLAPIConnectionData
from .dto.DTO import DTO
from .dto.request.discord.AddChannelsToDiscordDTO import AddChannelsToDiscordDTO
from .dto.request.discord.RemoveChannelsFromDiscordDTO import RemoveChannelsFromDiscordDTO
from .dto.request.alliance.CreateAllianceDTO import CreateAllianceDTO
from .dto.request.alliance.RemoveAllianceDTO import RemoveAllianceDTO
from .dto.request.authentication.AuthenticationRequestDTO import AuthenticationRequestDTO
from .dto.request.discord.AddAllianceToDiscordDTO import AddAllianceToDiscordDTO
from .dto.request.discord.CreateDiscordDTO import CreateDiscordDTO
from .dto.request.discord.RemoveDiscordDTO import RemoveDiscordDTO
from .dto.request.planet.AddPlanetDTO import AddPlanetDTO
from .dto.request.planet.RemovePlanetDTO import RemovePlanetDTO
from .dto.request.planet.RemoveSpecificPlanetDTO import RemoveSpecificPlanetDTO
from .dto.request.player.CreatePlayerDTO import CreatePlayerDTO
from .dto.request.player.RemovePlayerDTO import RemovePlayerDTO
from .dto.request.player.SetAllianceDTO import SetAllianceDTO
from .dto.request.player.SetPlayerRolesDTO import SetPlayerRolesDTO
from .dto.request.war.StartWarDTO import StartWarDTO
from .dto.request.war.StopWarDTO import StopWarDTO
from .dto.request.war.WarAttackRequestDTO import WarAttackRequestDTO
from .dto.response.alliance.AllianceDTO import AllianceDTO
from .dto.response.authentication.AuthenticationResponseDTO import AuthenticationResponseDTO
from .dto.response.discord.DiscordDTO import DiscordDTO
from .dto.response.planet.PlanetDTO import PlanetDTO
from .dto.response.player.PlayerDTO import PlayerDTO
from .dto.response.war.WarAttackResponseDTO import WarAttackResponseDTO
from .dto.response.war.WarDTO import WarDTO
from .exception.APIErrorException import APIErrorException

class FLAPIRequester:
    """
    The France Leader API requester.
    """

    def __init__(self, connection_data: FLAPIConnectionData) -> None:
        self.connection_data = connection_data

    ##################
    # Authentication #
    ##################

    def login(self) -> AuthenticationResponseDTO:
        (login, password) = self.connection_data.get_credentials()
        response = from_dict(
            AuthenticationResponseDTO, 
            self.__send_request("/login", "POST", AuthenticationRequestDTO(login, password))
        )
        self.connection_data.token = response.token
    
    ############
    # Alliance #
    ############

    def get_alliance(self, name: str) -> AllianceDTO:
        return from_dict(AllianceDTO, self.__send_request(f"/alliance/get/{name}"))
    
    def create_alliance(self, alliance_data: CreateAllianceDTO) -> AllianceDTO:
        return from_dict(AllianceDTO, self.__send_request("/alliance/create", "POST", alliance_data))
    
    def remove_alliance(self, alliance_data: RemoveAllianceDTO) -> AllianceDTO:
        return from_dict(AllianceDTO, self.__send_request("/alliance/remove", "DELETE", alliance_data))

    ##########
    # Player #
    ##########

    def get_player(self, nickname: str) -> PlayerDTO:
        return from_dict(PlayerDTO, self.__send_request(f"/player/get/{nickname}"))
    
    def create_player(self, player_data: CreatePlayerDTO) -> PlayerDTO:
        return from_dict(PlayerDTO, self.__send_request("/player/create", "POST", player_data))
    
    def set_player_alliance(self, player_data: SetAllianceDTO) -> PlayerDTO:
        return from_dict(PlayerDTO, self.__send_request("/player/set-alliance", "POST", player_data))
    
    def set_player_roles(self, player_data: SetPlayerRolesDTO) -> PlayerDTO:
        return from_dict(PlayerDTO, self.__send_request("/player/set-roles", "POST", player_data))
    
    def remove_player(self, player_data: RemovePlayerDTO) -> PlayerDTO:
        return from_dict(PlayerDTO, self.__send_request("/player/remove", "DELETE", player_data))

    ##########
    # Planet #
    ##########

    def get_planet(self, nickname: str, label: str) -> List[PlanetDTO]:
        return [
            from_dict(PlanetDTO, planet) 
            for planet in self.__send_request(f"/planet/get/{nickname}/{label}")
        ]
    
    def add_planet(self, planet_data: AddPlanetDTO) -> PlanetDTO:
        return from_dict(PlanetDTO, self.__send_request("/planet/add", "POST", planet_data))
    
    def remove_planet(self, planet_data: RemovePlanetDTO) -> PlanetDTO:
        return from_dict(PlanetDTO, self.__send_request("/planet/remove", "DELETE", planet_data))
    
    def remove_specific_planet(self, planet_data: RemoveSpecificPlanetDTO) -> PlanetDTO:
        return from_dict(PlanetDTO, self.__send_request("/planet/specific-remove", "DELETE", planet_data))

    #######
    # War #
    #######

    def get_war(self, alliance: str) -> WarDTO:
        return from_dict(WarDTO, self.__send_request(f"/war/get/{alliance}"))
    
    def start_war(self, war_data: StartWarDTO) -> WarDTO:
        return from_dict(WarDTO, self.__send_request("/war/start", "POST", war_data))
    
    def stop_war(self, war_data: StopWarDTO) -> WarDTO:
        return from_dict(WarDTO, self.__send_request("/war/stop", "POST", war_data))
    
    def attack(self, attack_data: WarAttackRequestDTO) -> WarAttackResponseDTO:
        return from_dict(WarAttackResponseDTO, self.__send_request("/war/attack", "POST", attack_data))
    
    def get_player_attacks(self, nickname: str) -> List[WarAttackResponseDTO]:
        return [
            from_dict(WarAttackResponseDTO, attack) 
            for attack in self.__send_request(f"/war/attacks/{nickname}")
        ]

    ###########
    # Discord #
    ###########

    def get_discord(self, discord_id: int) -> DiscordDTO:
        return [
            from_dict(DiscordDTO, alliance) 
            for alliance in self.__send_request(f"/discord/get/{discord_id}")
        ]
    
    def create_discord(self, discord_data: CreateDiscordDTO) -> DiscordDTO:
        return from_dict(DiscordDTO, self.__send_request("/discord/create", "POST", discord_data))

    def add_alliance_to_discord(self, discord_data: AddAllianceToDiscordDTO) -> DiscordDTO:
        return from_dict(DiscordDTO, self.__send_request("/discord/add-alliance", "POST", discord_data))

    def add_discord_channels(self, channels_data: AddChannelsToDiscordDTO) -> DiscordDTO:
        return from_dict(DiscordDTO, self.__send_request("/discord/add-channel", "POST", channels_data))
    
    def remove_discord_channels(self, channels_data: RemoveChannelsFromDiscordDTO) -> DiscordDTO:
        return from_dict(DiscordDTO, self.__send_request("/discord/remove-channel", "DELETE", channels_data))

    def remove_discord(self, discord_data: RemoveDiscordDTO) -> DiscordDTO:
        return from_dict(DiscordDTO, self.__send_request("/discord/remove", "DELETE", discord_data))

    #######################
    # Getters and setters #
    #######################

    def get_connection_data(self) -> FLAPIConnectionData:
        return self.connection_data
    
    def set_connection_data(self, connection_data: FLAPIConnectionData) -> None:
        self.connection_data = connection_data

    ###################
    # Private methods #
    ###################

    def __send_request(self, endpoint: str, method: str = "GET", data: DTO = None) -> Dict:
        # Determine the function to use depending on the method
        match method:
            case "GET": send_request_method = requests.get
            case "POST": send_request_method = requests.post
            case "DELETE": send_request_method = requests.delete
            case other: raise "Invalid HTTP method (use GET, POST or DELETE)"

        # Send the request
        token = self.connection_data.get_token()
        discord_id = self.connection_data.get_discord_id()
        response = send_request_method(
            f"{self.connection_data.api_uri}{endpoint}",
            headers = {
                "Authorization": None if token == None else f"Bearer {token}",
                "X-From-Discord": None if discord_id == None else f"{discord_id}"
            },
            json = None if data == None else data.__dict__
        )
        json_response = response.json()

        # Check the error
        if response.status_code >= 400:
            raise APIErrorException("An API error occured.", json_response)

        # Parse the JSON dictionnary to an object
        return json_response
