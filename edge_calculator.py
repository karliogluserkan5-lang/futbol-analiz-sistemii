def edge_hesapla(orani, ihtimal):
    return round(((ihtimal / 100) * orani - 1) * 100, 2)

def onerilen_bahis(ev_i, ber_i, dep_i, ev_o, ber_o, dep_o):
    sonuc = []
    e = edge_hesapla(ev_o, ev_i)
    if e >= 5: sonuc.append(f"Ev (1) Edge: %{e}")
    e = edge_hesapla(ber_o, ber_i)
    if e >= 5: sonuc.append(f"Beraberlik (0) Edge: %{e}")
    e = edge_hesapla(dep_o, dep_i)
    if e >= 5: sonuc.append(f"Deplasman (2) Edge: %{e}")
    return sonuc
