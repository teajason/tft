import config
import leagues

if __name__ == '__main__':
    """
    # Set config defaults
    # Get American Challengers
    Get names
    Get build summoners profiles
    Grab UUID
    Grab matches
    """
    config = config.Conf()
    ch = leagues.Leagues(region=config.region, api_key=config.api_key)
    ch.get(tier='challengers')
    ch.save_data()

def global_best(data):
    ''' Find the top 200 players across all regions '''
    pass

def find_meta(data):
    ''' Find the most frequently appearing trait amongst a collection '''
    pass
