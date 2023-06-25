# Intallation

```
pip install fl-api-requester
```

# Usage

```python
from fl_api_requester import *

connection_data = FLAPIConnectionData()
connection_data.set_credentials("username", "password")

try:
    # Login
    api_requester = FLAPIRequester()
    connection_data.set_token(api_requester.login(connection_data).token)

    # Get some data
    player = api_requester.get_player("Galactifer", connection_data)
    alliance = api_requester.get_alliance("France Leader", connection_data)

    print(player)
    print(len(alliance.players))

    # Start a War
    war = api_requester.start_war(StartWarDTO("Luxure Culinaire"), connection_data)

    print(war.alliance, war.opponent)
except APIErrorException as e:
    print(e.api_error)
```
