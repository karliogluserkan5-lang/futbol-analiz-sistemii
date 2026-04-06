import numpy as np

def hesapla_xg(shots, shots_on_target, goals, possession):
    # Gelişmiş xG hesaplama (ağırlıklı)
    xg = (shots_on_target * 0.35) + (shots * 0.05) + (goals * 0.15) + (possession * 0.02)
    return round(min(xg, 4.0), 2)

def takim_xg(son_maclar):
    if not son_maclar:
        return 1.5
    toplam = 0
    for mac in son_maclar[-5:]:  # son 5 maç
        toplam += hesapla_xg(
            mac.get('shots', 10),
            mac.get('shots_on_target', 4),
            mac.get('goals', 1),
            mac.get('possession', 50)
        )
    return round(toplam / min(5, len(son_maclar)), 2)

def mac_xg(home_stats, away_stats):
    home_xg = takim_xg(home_stats)
    away_xg = takim_xg(away_stats)
    return home_xg, away_xg

if __name__ == "__main__":
    print(f"Örnek xG: {hesapla_xg(12, 5, 2, 55)}")
