import os
from collections import OrderedDict
from dotenv import dotenv_values

class Env:
	"""
	Class used to load the envirnoment needed by the application.
	"""

	"""
	Environment variable key for the Discord application token. 
	"""
	APPLICATION_TOKEN: str = "APPLICATION_TOKEN"

	"""
	Environment variable key for the FL API connection. 
	"""
	API_URI: str = "API_URI"
	API_USER: str = "API_USER"
	API_PASSWORD: str = "API_PASSWORD"
	

	"""
	Dictionnaries containing the application environment once it's loaded.
	"""
	_env: OrderedDict = OrderedDict()

	@classmethod
	def load_env(cls, env_file: str = None, system: bool = True):
		"""
		Load the environment specified inside the given env_file. If no env_file is specified, all the files beggining 
		with .env at the project root will be loaded. If an env_file has already been loaded, you can call load_env
		again but all the already existing keys will be replaced in case of conflict. 

		Parameters
		------
		- env_file : `str` 
			The env_file to parse and add to the environment.
		- system : `bool` 
			Specify if we should use the system environment or not. 
		"""
		if env_file != None:
			# If a .env file is specified then we load it
			cls._env.update(dotenv_values(env_file, verbose = True))
		else:
			# Otherwise we load all the env files at the project root
			env_files = [f for f in os.listdir(".") if os.path.isfile(f) and f.startswith(".env")]
			for env_file in env_files:
				cls._env.update(dotenv_values(env_file))

		# Load the system environment if needed
		if system:
			cls._env.update(os.environ)

	@classmethod
	def get(cls, key: str) -> str:
		"""
		Returns the env value associated to the given key.
		Precondition: Environment must be loaded (cf. load_env).

		Parameters
		------    
		- key : `str`
			The name of the env variable you want to get the value.
		"""
		if cls._env == None:
			return None
		return cls._env.get(key)