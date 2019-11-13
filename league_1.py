import requests
import pprint

key = {"X-Riot-Token": "YOUR_TOKEN"}
base = 'https://'
NA = 'na1.api.riotgames.com'


challenger = base + NA + '/tft/league/v1/challenger'

res = requests.get(challenger, headers=key)
content = res.json()
pprint.pprint(content)
