import requests
from bs4 import BeautifulSoup

def understat_xg(team_name):
    # Understat'dan takım xG'sini çeker (basit örnek)
    # Gerçek scrape için daha detaylı kod gerekir
    return 1.8  # geçici

def takim_xg(team_name):
    xg = understat_xg(team_name)
    return xg

def mac_xg(ev, dep):
    ev_xg = takim_xg(ev)
    dep_xg = takim_xg(dep)
    return ev_xg, dep_xg
