import requests
from bs4 import BeautifulSoup
import json

def understat_xg(team_name):
    try:
        # Understat ana sayfasından lig verilerini çek
        url = "https://understat.com/league/EPL"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # JSON verisini bul
        scripts = soup.find_all("script")
        for script in scripts:
            if "teamsData" in str(script):
                json_str = str(script).split("teamsData = ")[1].split(";")[0]
                data = json.loads(json_str)
                
                # Takım adını bul
                for team_id, team_data in data.items():
                    if team_name.lower() in team_data["title"].lower():
                        xg = float(team_data["total"]["xG"])
                        return round(xg / team_data["total"]["played"], 2)
        return 1.6
    except:
        return 1.6

def takim_xg(team_name):
    return understat_xg(team_name)

def mac_xg(ev, dep):
    ev_xg = takim_xg(ev)
    dep_xg = takim_xg(dep)
    return ev_xg, dep_xg
