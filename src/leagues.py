import requests
import pprint

from datetime import datetime
from pathlib import Path

"""
End points
/tft/league/v1/challenger
/tft/league/v1/grandmaster
/tft/league/v1/master
/tft/league/v1/entries/{tier}/{division}
/tft/league/v1/leagues/{leagueId}
/tft/league/v1/entries/by-summoner/{encryptedSummonerId}
"""

class Leagues:
    """
    Master, Grandmaster, and Challenger have their own end points
    and they do not have the concept of a division
    #
    Init Leagues(config)
    """

    tiers = ["iron", "bronze", "silver",
            "gold", "platinum", "diamond",
            "master", "grandmaster", "challenger"]

    master_plus = {'challenger','grandmaster','master'}

    divisions = ["i", "ii", "iii", "iv"]

    def __init__(self, **kwargs):
        self.data = []
        self.api_key = {'X-Riot-Token': kwargs.get('api_key', None)}
        self.base = kwargs.get('base', 'https://')
        self.platform = kwargs.get('platform', 'na1.api.riotgames.com')
        self.tier = kwargs.get('tier', 'challenger')
        self.division = kwargs.get('division', '')

        if(self.api_key is None):
            print("Did you forget an API key??")

    def get(self, **kwargs):
        """ Retrieves current players by platform, tier and division """
        if(self.tier in self.master_plus):
            req = self.base + self.platform + '/tft/league/v1/' + self.tier
        else:
            req = self.base + self.platform + self.tier + self.division
        res = requests.get(req, headers=self.api_key)
        self.data = res.json()

    def save_data(self):
        """
        Save data to a file in YYYYMMDD:24HR_REGION_TIER_DIVISION format
        """
        date_string = datetime.now().strftime("%Y-%m-%d_%H:%M%S.%f")
        if(self.division):
            filename = date_string + '_' + self.platform + '_' + self.tier + '_' + self.division
        else:
            filename = date_string + '_' + self.platform + '_' + self.tier
        filename += '.data'
        path = Path.cwd().parent / 'data' / filename
        with open(path, "w") as save_file:
            save_file.write(pprint.pformat(self.data))

    def show(self):
        pprint.pprint(self.data)

    def show_parameters(self):
        """ Show me the attributes for debugging """
        print("Region: " + self.platform + "\n",
              "Tier: " + self.tier + "\n",
              "Division: " + self.division)

    def get_names(self):
        names = []
        for entry in ch.data['entries']:
            print(entry['summonerName'])
            names.append(entry['summonerName'])

        return names
