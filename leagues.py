import requests
import os
from datetime import datetime
import pprint

key = {"X-Riot-Token": "RGAPI-8bd41547-e741-4623-af4d-24b13d4f2365"}
base = 'https://'
def_region = 'na1.api.riotgames.com'
def_tier = '/tft/league/v1/challenger'

"""
End points
/tft/league/v1/master
/tft/league/v1/grandmaster
/tft/league/v1/challenger
/tft/league/v1/entries/{tier}/{division}
/tft/league/v1/leagues/{leagueId}
/tft/league/v1/entries/by-summoner/{encryptedSummonerId}
"""

class Leagues:
    """
    ### Collect current data of a league/division
    TODO: Better description
    """

    ''' Master, Grandmaster, and Challenger have their own end points '''

    tiers = ["iron", "bronze", "silver",
            "gold", "platinum", "diamond",]

    divisions = ["i", "ii", "iii", "iv"]


    def __init__(self, region=def_region, tier=def_tier, division="i"):
        self.data = []
        self.region = region
        self.tier = tier
        self.division = division

    def get_grandmasters(self):
        """ Loads todays masters """
        req = base + self.region + self.tier 
        res = requests.get(req, headers=key)
        self.data = res.json()

    def get_masters(self):
        """ Loads todays masters """
        req = base + self.region + self.tier 
        res = requests.get(req, headers=key)
        self.data = res.json()

    def get_challengers(self):
        """ Loads todays challengers """
        req = base + self.region + self.tier 
        res = requests.get(req, headers=key)
        self.data = res.json()

    def save_data(self):
        """
        Save data to a file in YYYYMMDD:24HR_REGION_TIER_DIVISION format
        # TODO: REGION is divided by platform/region -- need to refactor
        """
        date_string = datetime.now().strftime("%Y-%m-%d_%H:%M%S.%f")
        filename = date_string + "_AMERICAS" + "_CHALLENGERS"
        path = os.getcwd() + '/data/'
        path += filename
        with open(path, "w") as save_file:
            save_file.write(pprint.pformat(self.data))

    def show(self):
        pprint.pprint(self.data)

    def show_parameters(self):
        """ Show me the attributes for debugging """
        print("Region: " + self.region + "\n",
              "Tier: " + self.tier + "\n",
              "Division: " + self.division)
