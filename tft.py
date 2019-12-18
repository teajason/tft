import leagues

if __name__ == '__main__':
    print("Welcome to main!")
    ch = leagues.Leagues()
    ch.get_challengers()

    name = []
    for entry in ch.data['entries']:
        print(entry['summonerName'])
        name.append(entry['summonerName'])

def analyze(data):
    pass
