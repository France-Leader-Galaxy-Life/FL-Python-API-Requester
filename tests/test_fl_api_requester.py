import pytest
from fl_api_requester import FLAPIConnectionData, FLAPIRequester, APIErrorException
from .Env import Env

@pytest.fixture
def api_requester():
	Env.load_env()
	connection_data = FLAPIConnectionData()
	connection_data.api_uri = Env.get(Env.API_URI)
	connection_data.set_credentials(Env.get(Env.API_USER), Env.get(Env.API_PASSWORD))
	fl_api = FLAPIRequester(connection_data)
	fl_api.login()
	return fl_api


	############
	# Alliance #
	############

def test_get_alliance_PASSED(api_requester):
	response = api_requester.get_alliance(name="France Leader")
	assert response is not APIErrorException


def test_get_alliance_FAILED(api_requester):
	with pytest.raises(APIErrorException):
		response = api_requester.get_alliance(name="France Leader XXX")


	##########
	# Player #
	##########


def test_get_player_PASSED(api_requester):
	response = api_requester.get_player(nickname="galactifer")
	assert response is not APIErrorException


def test_get_player_FAILED(api_requester):
	with pytest.raises(APIErrorException):
		response = api_requester.get_player(nickname="galactipaladium")



		##########
		# Planet #
		##########

def test_get_planet_PASSED(api_requester):
	response = api_requester.get_planet(nickname="galactifer",label="c5")
	assert response is not APIErrorException

def test_get_planet_FAILED_label(api_requester):
	with pytest.raises(APIErrorException):
		response = api_requester.get_planet(nickname="galactifer",label="afz")
	
def test_get_planet_FAILED_nickname(api_requester):
	with pytest.raises(APIErrorException):
		response = api_requester.get_planet(nickname="galactipaladium",label="c1")
	

		###########
		# Discord #
		###########

def test_get_discord_PASSED(api_requester):
	response = api_requester.get_discord(discord_id="1012059930695573605")
	assert response is not APIErrorException

def test_get_discord_FAILED(api_requester):
	with pytest.raises(APIErrorException):
		response = api_requester.get_discord(discord_id="643521984651")
