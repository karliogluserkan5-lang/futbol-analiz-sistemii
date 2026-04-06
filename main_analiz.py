from datetime import datetime
from poisson_model import poisson_skor
from xg_model import mac_xg
from edge_calculator import edge_hesapla
import requests
import config

def get_fixtures():
    url = f"https://api.football-data.org/v4/matches"
    headers = {"X-Auth-Token": config.FOOTBALL_DATA_API}
    response = requests.get(url, headers=headers)
    return response.json().get("matches", [])

def main():
    print(f"=== FUTBOL ANALIZ SISTEMI ===")
    print(f"Calisma zamani: {datetime.now()}\n")

    maclar = get_fixtures()
    print(f"{len(maclar)} mac bulundu.\n")

    for mac in maclar[:5]:
        ev = mac["homeTeam"]["name"]
        deplasman = mac["awayTeam"]["name"]

        ev_xg, dep_xg = mac_xg([], [])
        print(f"{ev} vs {deplasman}")
        print(f"  xG: {ev_xg} - {dep_xg}")

        skorlar = poisson_skor(ev_xg, dep_xg)
        print(f"  En olası skor: {max(skorlar, key=skorlar.get)}")

        edge = edge_hesapla(ev_xg, dep_xg)
        if edge > 5:
            print(f"  VALUE BET! Edge: %{edge:.1f}")
        print()

if __name__ == "__main__":
    main()
