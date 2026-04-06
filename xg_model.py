import requests
import config

def sportmonks_xg(team_id):
    url = f"https://soccer.sportmonks.com/api/v2.0/teams/{team_id}?api_token={config.SPORTMONKS_API_KEY}&include=xg"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        xg = data.get('data', {}).get('xg', {}).get('total', 1.6)
        return round(float(xg), 2)
    return 1.6

def takim_xg(team_name):
    return sportmonks_xg(team_name)  # team_id eşlemesi gerekecek

def mac_xg(ev, dep):
    ev_xg = takim_xg(ev)
    dep_xg = takim_xg(dep)
    return ev_xg, dep_xg
