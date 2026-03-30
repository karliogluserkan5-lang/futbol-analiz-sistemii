def form_puani(maclar):
    puan = 0
    for s in maclar:
        if s == 'G': puan += 3
        elif s == 'B': puan += 1
    return puan

def trend_analizi(maclar):
    son5 = form_puani(maclar[:5])
    onceki5 = form_puani(maclar[5:10]) if len(maclar) >= 10 else 0
    if son5 > onceki5: return "YÜKSELİŞ"
    elif son5 < onceki5: return "DÜŞÜŞ"
    return "STABİL"
