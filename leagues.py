import requests
import pprint

key = {"X-Riot-Token": "RGAPI-24115607-e824-4657-b49d-759f807ea4b7"}
base = 'https://'
def_region = 'na1.api.riotgames.com'
def_league = '/tft/league/v1/challenger'

"""
End points
/tft/league/v1/challenger
/tft/league/v1/entries/by-summoner/{encryptedSummonerId}
/tft/league/v1/entries/{tier}/{division}
/tft/league/v1/grandmaster
/tft/league/v1/leagues/{leagueId}
/tft/league/v1/master
"""

class Leagues:
    """ Ask questions about a set of players """
    def __init__(self, region=def_region, tier=def_league, division="I"):
        self.data = []
        self.region = region
        self.tier = tier
        self.division = division

    def show_parameters(self):
        print("Region: " + self.region + "\n",
                "Tier: " + self.tier + "\n",
                "Division: " + self.division)

    def get_challengers(self):
        """ Loads todays challengers """
        req = base + region + league
        res = requests.get(req, headers=key)
        self.data = res.json()

    def get_masters(self):
        """ Loads todays masters """
        req = base + region + league
        res = requests.get(req, headers=key)
        self.data = res.json()

    def show(self):
        pprint.pprint(self.data)

    def meta(placement=1):
        """Return most common trait amongst placement"""
        pass
