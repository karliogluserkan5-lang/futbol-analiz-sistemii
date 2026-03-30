def hesapla_xg(shots, shots_on_target, goals, possesion):
    xg = (shots_on_target * 0.35) + (shots * 0.05) + (goals * 0.1) + (possesion * 0.01)
    return round(xg, 2)

def takim_xg(son_maclar):
    toplam = 0
    for mac in son_maclar:
        toplam += hesapla_xg(mac['shots'], mac['shots_on_target'], mac['goals'], mac['possesion'])
    return round(toplam / len(son_maclar), 2) if son_maclar else 0

if __name__ == "__main__":
    print(hesapla_xg(12, 5, 2, 55))
