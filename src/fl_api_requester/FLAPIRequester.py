from typing import List
from munch import Munch
import requests

from . import FLAPIConnectionData
from .dto.DTO import DTO
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

    """
    The France Leader API URI.
    """
    FL_API_URI: str = "http://51.210.254.14:8080"

    def __init__(self) -> None:
        ...

    ##################
    # Authentication #
    ##################

    def login(self, connection_data: FLAPIConnectionData) -> AuthenticationResponseDTO:
        (login, password) = connection_data.get_credentials()
        return self._send_post_request("/login", AuthenticationRequestDTO(login, password), connection_data)
    
    ############
    # Alliance #
    ############

    def get_alliance(self, name: str, connection_data: FLAPIConnectionData) -> AllianceDTO:
        return self._send_get_request(f"/alliance/get/{name}", connection_data)
    
    def create_alliance(self, alliance_data: CreateAllianceDTO, connection_data: FLAPIConnectionData) -> AllianceDTO:
        return self._send_post_request("/alliance/create", alliance_data, connection_data)
    
    def remove_alliance(self, alliance_data: RemoveAllianceDTO, connection_data: FLAPIConnectionData) -> AllianceDTO:
        return self._send_delete_request("/alliance/remove", alliance_data, connection_data)

    ##########
    # Player #
    ##########

    def get_player(self, nickname: str, connection_data: FLAPIConnectionData) -> PlayerDTO:
        return self._send_get_request(f"/player/get/{nickname}", connection_data)
    
    def create_player(self, player_data: CreatePlayerDTO, connection_data: FLAPIConnectionData) -> PlayerDTO:
        return self._send_post_request("/player/create", player_data, connection_data)
    
    def set_player_alliance(self, player_data: SetAllianceDTO, connection_data: FLAPIConnectionData) -> PlayerDTO:
        return self._send_post_request("/player/set-alliance", player_data, connection_data)
    
    def set_player_roles(self, player_data: SetPlayerRolesDTO, connection_data: FLAPIConnectionData) -> PlayerDTO:
        return self._send_post_request("/player/set-roles", player_data, connection_data)
    
    def remove_player(self, player_data: RemovePlayerDTO, connection_data: FLAPIConnectionData) -> PlayerDTO:
        return self._send_delete_request("/player/remove", player_data, connection_data)

    ##########
    # Planet #
    ##########

    def get_planet(self, nickname: str, label: str, connection_data: FLAPIConnectionData) -> PlanetDTO:
        return self._send_get_request(f"/planet/get/{nickname}/{label}", connection_data)
    
    def add_planet(self, planet_data: AddPlanetDTO, connection_data: FLAPIConnectionData) -> PlanetDTO:
        return self._send_post_request("/planet/add", planet_data, connection_data)
    
    def remove_planet(self, planet_data: RemovePlanetDTO, connection_data: FLAPIConnectionData) -> PlanetDTO:
        return self._send_delete_request("/planet/remove", planet_data, connection_data)
    
    def remove_specific_planet(
        self, 
        planet_data: RemoveSpecificPlanetDTO, 
        connection_data: FLAPIConnectionData
    ) -> PlanetDTO:
        return self._send_delete_request("/planet/specific-remove", planet_data, connection_data)

    #######
    # War #
    #######

    def get_war(self, alliance: str, connection_data: FLAPIConnectionData) -> WarDTO:
        return self._send_get_request(f"/war/get/{alliance}", connection_data)
    
    def start_war(self, war_data: StartWarDTO, connection_data: FLAPIConnectionData) -> WarDTO:
        return self._send_post_request("/war/start", war_data, connection_data)
    
    def stop_war(self, war_data: StopWarDTO, connection_data: FLAPIConnectionData) -> WarDTO:
        return self._send_post_request("/war/stop", war_data, connection_data)
    
    def attack(self, attack_data: WarAttackRequestDTO, connection_data: FLAPIConnectionData) -> WarAttackResponseDTO:
        return self._send_post_request("/war/attack", attack_data, connection_data)
    
    def get_player_attacks(self, nickname: str, connection_data: FLAPIConnectionData) -> WarDTO:
        return self._send_get_request(f"/war/attacks/{nickname}", connection_data)

    ###########
    # Discord #
    ###########

    def get_discord_alliances(self, discord_id: int, connection_data: FLAPIConnectionData) -> List[AllianceDTO]:
        return self._send_get_request(f"/discord/{discord_id}/alliances", connection_data)
    
    def create_discord(self, discord_data: CreateDiscordDTO, connection_data: FLAPIConnectionData) -> DiscordDTO:
        return self._send_post_request("/discord/create", discord_data, connection_data)

    def add_alliance_to_discord(
        self, 
        discord_data: AddAllianceToDiscordDTO, 
        connection_data: FLAPIConnectionData
    ) -> DiscordDTO:
        return self._send_post_request("/discord/add-alliance", discord_data, connection_data)

    def remove_discord(self, discord_data: RemoveDiscordDTO, connection_data: FLAPIConnectionData) -> DiscordDTO:
        return self._send_delete_request("/discord/remove", discord_data, connection_data)

    ###################
    # Private methods #
    ###################

    def _send_get_request(self, endpoint: str, connection_data: FLAPIConnectionData) -> DTO:
        # Send the request
        token = connection_data.get_token()
        discord_id = connection_data.get_discord_id()
        response = requests.get(
            f"{self.FL_API_URI}{endpoint}",
            headers = {
                "Authorization": None if token == None else f"Bearer {token}",
                "X-From-Discord": None if discord_id == None else f"{discord_id}"
            }
        )
        json_response = response.json()

        # Check the error
        if response.status_code >= 400:
            raise APIErrorException("An API error occured.", json_response)

        # Parse the JSON dictionnary to an object
        return Munch.fromDict(json_response)
    
    def _send_post_request(
        self,
        endpoint: str,
        data: DTO, 
        connection_data: FLAPIConnectionData
    ) -> DTO:        
        # Send the request
        token = connection_data.get_token()
        discord_id = connection_data.get_discord_id()
        response = requests.post(
            f"{self.FL_API_URI}{endpoint}",
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
        return Munch.fromDict(json_response)
    
    def _send_delete_request(
        self,
        endpoint: str,
        data: DTO, 
        connection_data: FLAPIConnectionData
    ) -> DTO:        
        # Send the request
        token = connection_data.get_token()
        discord_id = connection_data.get_discord_id()
        response = requests.delete(
            f"{self.FL_API_URI}{endpoint}",
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
        return Munch.fromDict(json_response)
