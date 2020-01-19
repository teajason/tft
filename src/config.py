from os import getcwd

from collections import OrderedDict

class Conf:
    """
    Depending on your request, you might need a platform or a region
    """
    platforms = OrderedDict()
    platforms['BR1'] = 'br1.api.riotgames.com'
    platforms['EUN1'] = 'eun1.api.riotgames.com'
    platforms['EUW1'] = 'euw1.api.riotgames.com'
    platforms['JP1'] = 'jp1.api.riotgames.com'
    platforms['KR'] = 'kr.api.riotgames.com'
    platforms['LA1'] = 'la1.api.riotgames.com'
    platforms['LA2'] = 'la2.api.riotgames.com'
    platforms['NA1'] = 'na1.api.riotgames.com'
    platforms['OC1'] = 'oc1.api.riotgames.com'
    platforms['TR1'] = 'tr1.api.riotgames.com'
    platforms['RU'] = 'ru.api.riotgames.com'

    regions = OrderedDict()
    regions['AMERICAS'] = 'americas.api.riotgames.com'
    regions['ASIA'] = 'asia.api.riotgames.com'
    regions['EUROPE'] = 'europe.api.riotgames.com'

    base = 'https://'
    api_key = ''
    region = ''
    region_key = ''
    platform = ''
    platform_key = ''

    def __init__(self, **kwargs):
        """
        Default is currently American challengers
        # Should do some input validation
        """
        self.api_key = self.access_token()
        self.region_key = 'AMERICAS'
        self.region = self.regions['AMERICAS']
        self.platform_key = 'NA1'
        self.platform = self.platforms['NA1']

    def access_token(self):
        #TODO: allow for env_var to be access token
        secret_file = getcwd() + '/key.secret'
        with open(secret_file, 'r') as secret:
            api_key = secret.readline()

        if('\n' in api_key):
            return api_key.rstrip('\n')

        return api_key

    def set_region(self, region):
        region = region.upper()
        if(region not in self.regions):
            print("Not a valid region. Region is currently: " + self.region_key)
            print("Options are: ")
            for reg in self.regions:
                print(reg)
            return None
        self.region = region
        print("Region is now set to: " + self.region)

    def set_platform(self, platform):
        platform = platform.upper()
        if(platform not in self.platforms):
            print("Not a valid platform. Platform is currently: " + self.platform_key)
            print("Options are: ")
            for plat in self.platforms:
                print(plat)
            return None
        self.platform = platform
        print("Platform is now set to: " + self.platform)

    def show(self):
        values = [("base: ", self.base), ("region_key: ", self.region_key),
                ("region: ", self.region), ("platform_key: ", self.platform_key),
                ("platform: ", self.platform),]
        for val in values:
            print(val)
