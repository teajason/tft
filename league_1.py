import requests
import pprint

key = {"X-Riot-Token": "RGAPI-24115607-e824-4657-b49d-759f807ea4b7"}
base = 'https://'
NA = 'na1.api.riotgames.com'


challenger = base + NA + '/tft/league/v1/challenger'

res = requests.get(challenger, headers=key)
content = res.json()
pprint.pprint(content)
