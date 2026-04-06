import requests
import config
from team_id_map import TEAM_IDS

def sportmonks_xg(team_id):
    url = f"https://soccer.sportmonks.com/api/v2.0/teams/{team_id}?api_token={config.SPORTMONKS_API_KEY}&include=xg"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        xg = data.get('data', {}).get('xg', {}).get('total', 1.6)
        return round(float(xg), 2)
    return 1.6

def takim_xg(team_name):
    # Takım adını kısalt (örn: "Udinese Calcio" -> "Udinese")
    short_name = team_name.split()[0]
    team_id = TEAM_IDS.get(short_name, 129)
    return sportmonks_xg(team_id)

def mac_xg(ev, dep):
    ev_xg = takim_xg(ev)
    dep_xg = takim_xg(dep)
    return ev_xg, dep_xg
